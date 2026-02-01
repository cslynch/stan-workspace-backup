#!/bin/bash
# Monitor API usage from session logs

SESSION_FILE="/home/clawdbot/.openclaw/agents/main/sessions/21979c5e-92eb-45ef-af0f-99028d8d0976.jsonl"

echo "=== API Usage Monitor ==="
echo "Time: $(date)"
echo ""

# Extract usage data
grep -o '"usage":{[^}]*}' "$SESSION_FILE" > /tmp/current_usage.txt

# Count calls
CALL_COUNT=$(wc -l < /tmp/current_usage.txt)
echo "Total API calls: $CALL_COUNT"

# Extract token counts and costs
cat /tmp/current_usage.txt | grep -o '"input":[0-9]*' | grep -o '[0-9]*$' > /tmp/in.txt
cat /tmp/current_usage.txt | grep -o '"output":[0-9]*' | grep -o '[0-9]*$' > /tmp/out.txt
cat /tmp/current_usage.txt | grep -o '"cacheRead":[0-9]*' | grep -o '[0-9]*$' > /tmp/cr.txt
cat /tmp/current_usage.txt | grep -o '"cacheWrite":[0-9]*' | grep -o '[0-9]*$' > /tmp/cw.txt
cat /tmp/current_usage.txt | grep -o '"total":[0-9.]*' | grep -o '[0-9.]*$' > /tmp/cost.txt

# Calculate using Python
python3 << 'EOF'
import sys

def read_numbers(filename):
    try:
        with open(filename) as f:
            return [float(x.strip()) for x in f if x.strip()]
    except:
        return []

inputs = read_numbers('/tmp/in.txt')
outputs = read_numbers('/tmp/out.txt')
cache_reads = read_numbers('/tmp/cr.txt')
cache_writes = read_numbers('/tmp/cw.txt')
costs = read_numbers('/tmp/cost.txt')

count = len(costs)
if count > 0:
    print(f"\nAverages per message:")
    print(f"  Cache read: {sum(cache_reads[:count])/count:,.0f} tokens")
    print(f"  Output:     {sum(outputs[:count])/count:,.0f} tokens")
    print(f"  Cost:       ${sum(costs)/count:.4f}")
    
    print(f"\nTotals:")
    print(f"  Total cost: ${sum(costs):.2f}")
    print(f"  Messages:   {count}")
    
    # Check for bloat
    avg_cache = sum(cache_reads[:count])/count
    if avg_cache > 30000:
        print(f"\n⚠️  WARNING: Cache bloat detected ({avg_cache:,.0f} > 30,000)")
    else:
        print(f"\n✓ Context healthy ({avg_cache:,.0f} < 30,000)")
EOF

echo ""
echo "---"
