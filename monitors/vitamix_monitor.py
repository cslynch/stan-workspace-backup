#!/usr/bin/env python3
"""
Vitamix Certified Reconditioned Monitor
Tracks stock + price, alerts on state changes only (in-stock or price drop)
Persists state to disk to detect transitions between runs
"""

import json
import os
import sys
import time
from datetime import datetime, timezone
import re
from pathlib import Path

# Try importing requests; fall back to urllib
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    import urllib.request
    HAS_REQUESTS = False

# State file
STATE_FILE = Path.home() / ".openclaw" / "workspace" / "monitors" / "vitamix_state.json"
STATE_FILE.parent.mkdir(parents=True, exist_ok=True)

# Product definitions
PRODUCTS = {
    "propel_750": {
        "name": "Certified Reconditioned Propel 750",
        "url": "https://www.vitamix.com/us/en_us/products/certified-reconditioned-propel-750",
        "alert_price_threshold": 229.95,
        "priority_threshold": None,
    },
    "venturist": {
        "name": "Certified Reconditioned Venturist V1200",
        "url": "https://www.vitamix.com/us/en_us/products/certified-reconditioned-v1200",
        "alert_price_threshold": 239.95,
        "priority_threshold": 200.00,
    },
}

SHOP_URL = "https://www.vitamix.com/us/en_us/shop/certified-reconditioned"
TELEGRAM_ALERT = True  # Set to False to suppress actual alerts during testing

def fetch_url(url):
    """Fetch URL content."""
    try:
        if HAS_REQUESTS:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                return resp.text
        else:
            with urllib.request.urlopen(url, timeout=10) as resp:
                return resp.read().decode('utf-8')
    except Exception as e:
        print(f"[ERROR] Failed to fetch {url}: {e}", file=sys.stderr)
        return None

def load_state():
    """Load last-known state from disk."""
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE) as f:
                return json.load(f)
        except:
            pass
    return {
        "products": {},
        "last_check": None,
        "consecutive_failures": 0,
    }

def save_state(state):
    """Persist state to disk."""
    state["last_check"] = datetime.now(timezone.utc).isoformat()
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def extract_price_and_stock(html, product_name):
    """
    Extract price and stock status from product HTML.
    Looks for: price JSON ("price", "regularPrice"), stock indicators.
    Returns (price_float or None, is_in_stock_bool)
    """
    if not html:
        return None, False

    # Look for price in JSON-like structures or direct patterns
    # Vitamix uses various formats: "price": 229.95 or similar
    price = None
    
    # Try JSON price field patterns
    price_patterns = [
        r'["\']price["\']\s*:\s*([\d.]+)',
        r'["\']regularPrice["\']\s*:\s*([\d.]+)',
        r'\$([\d]+\.\d{2})',
    ]
    
    for pattern in price_patterns:
        match = re.search(pattern, html)
        if match:
            try:
                price = float(match.group(1))
                break
            except (ValueError, IndexError):
                continue

    # Check for stock status
    out_of_stock_indicators = [
        r'out\s+of\s+stock',
        r'unavailable',
        r'coming soon',
        r'out of inventory',
        r'\"availability\"\s*:\s*\"OutOfStock\"',
        r'InStock[\"\']\s*:\s*false',
    ]
    
    is_out_of_stock = any(
        re.search(ind, html, re.IGNORECASE) for ind in out_of_stock_indicators
    )
    
    # Default to in_stock unless explicitly marked out
    is_in_stock = not is_out_of_stock
    
    # But if we see "InStock" explicitly, use that
    in_stock_match = re.search(r'["\']InStock["\']\s*:\s*(true|false)', html, re.IGNORECASE)
    if in_stock_match:
        is_in_stock = in_stock_match.group(1).lower() == 'true'

    return price, is_in_stock

def search_products_on_shop(html):
    """
    Parse the shop listing page to find product URLs.
    Returns dict of {product_key: url}
    """
    found = {}
    
    for key, product in PRODUCTS.items():
        search_term = product["search_term"]
        # Look for links containing the product name
        pattern = rf'href=["\'](https://www\.vitamix\.com[^\s"\']*{re.escape(search_term)}\w*[^\s"\']*)["\']'
        matches = re.findall(pattern, html, re.IGNORECASE)
        
        if matches:
            found[key] = matches[0]
            print(f"[FOUND] {product['name']}: {found[key]}")
        else:
            print(f"[WARN] Could not locate {product['name']} on shop page")
    
    return found

def check_products(state):
    """Poll each product and detect state changes."""
    alerts = []
    failures = 0

    # Check each product
    for key, product in PRODUCTS.items():
        print(f"[CHECK] {product['name']}...")
        html = fetch_url(product["url"])
        
        if not html:
            failures += 1
            print(f"[FAIL] Could not fetch {product['name']}")
            continue

        price, is_in_stock = extract_price_and_stock(html, product["name"])
        print(f"  -> Price: ${price if price else 'N/A'}, In Stock: {is_in_stock}")

        # Ensure state record exists
        if key not in state["products"]:
            state["products"][key] = {
                "url": product["url"],
                "last_price": None,
                "last_in_stock": False,
            }

        old_state = state["products"][key]

        # Detect state changes
        state_changed = (
            old_state.get("last_in_stock") != is_in_stock or
            old_state.get("last_price") != price
        )

        # Check alert conditions
        alert = None
        if is_in_stock and price is not None:
            if price <= product["alert_price_threshold"]:
                priority = (
                    product["priority_threshold"] and
                    price <= product["priority_threshold"]
                )
                alert = {
                    "product": product["name"],
                    "price": price,
                    "in_stock": True,
                    "url": product["url"],
                    "priority": priority,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }

        if state_changed and alert:
            alerts.append(alert)
            print(f"[ALERT] {product['name']}: ${price:.2f} in stock!")
        elif state_changed:
            print(f"[STATE CHANGE] {product['name']} (no alert threshold met)")

        # Update state
        state["products"][key]["last_price"] = price
        state["products"][key]["last_in_stock"] = is_in_stock

    state["consecutive_failures"] = failures
    return alerts, state

def send_telegram_alert(alert):
    """Send alert to Casey's Telegram."""
    try:
        # Import message tool via exec context (would be called from main)
        prefix = "[PRIORITY] " if alert.get("priority") else ""
        message_text = (
            f"{prefix}Vitamix Alert\n\n"
            f"📦 {alert['product']}\n"
            f"💵 ${alert['price']:.2f}\n"
            f"✅ In Stock\n\n"
            f"🔗 {alert['url']}\n"
            f"⏰ {alert['timestamp']}"
        )
        print(f"[TELEGRAM] Would send: {message_text}")
        # Actual send would happen via message tool call from wrapper
        return message_text
    except Exception as e:
        print(f"[ERROR] Failed to format alert: {e}", file=sys.stderr)
        return None

def send_unavailable_alert(state):
    """Alert user that monitor can't reach Vitamix (2 failures in a row)."""
    print("[ALERT] Cannot reach Vitamix for 2 consecutive checks")
    message_text = (
        "⚠️ Vitamix Monitor\n\n"
        "Unable to reach certified-reconditioned shop for 2 checks in a row.\n"
        "Monitor is paused until pages are reachable.\n\n"
        "Check: https://www.vitamix.com/us/en_us/shop/certified-reconditioned"
    )
    return message_text

def main():
    print(f"\n[START] Vitamix monitor @ {datetime.now(timezone.utc).isoformat()}")
    
    state = load_state()
    alerts, state = check_products(state)
    
    save_state(state)

    # Handle consecutive failures
    if state["consecutive_failures"] >= 2:
        if state.get("previous_failures", 0) >= 1:
            print("[FAILURE] 2 consecutive check failures — sending unavailability alert")
            msg = send_unavailable_alert(state)
            # Return alert for parent to send via message tool
            state["previous_failures"] = 0
            save_state(state)
            return {"unavailable_alert": msg}
        else:
            state["previous_failures"] = state.get("previous_failures", 0) + 1
            save_state(state)
    else:
        state["previous_failures"] = 0
        save_state(state)

    # Return alerts for parent to dispatch
    if alerts:
        return {"alerts": alerts}
    else:
        print("[OK] No alerts (no state changes)")
        return {"alerts": []}

if __name__ == "__main__":
    result = main()
    print(json.dumps(result, indent=2))
