# Shopping List System

Three ways to manage your shopping list:

## 1. Web App (Best for Mobile)
**File:** `shopping-app.html`

- Open in any browser (Chrome, Safari, Firefox)
- Works offline - saves to browser storage
- Filter by tags (groceries, amazon, house-stuff, etc.)
- Search items
- Check off completed items
- Export to markdown

**Features:**
- 📱 Mobile-friendly responsive design
- 🏷️ Tag system for organization
- 🔍 Real-time search
- ✅ Check off items
- 📄 Export to SHOPPING.md format

## 2. Markdown File (Best for Version Control)
**File:** `SHOPPING.md`

- Simple text file
- Git-tracked (auto-backed up daily at 2 AM)
- Edit directly or via Stan
- Organized by category

## 3. Chat with Stan (Best for Quick Adds)
Just message Stan:
- "Add milk to groceries"
- "Add shower cap to amazon list"
- "Show me the shopping list"
- "What's on the hardware list?"
- "Mark shower cap as bought"

## Data Flow

```
You add item via:
├─ Web App → localStorage → Export to SHOPPING.md
├─ Chat → Stan updates SHOPPING.md
└─ Direct edit → SHOPPING.md

All files backed up to GitHub daily at 2 AM
```

## Quick Start

1. **Mobile shopping in store:**
   - Open `shopping-app.html` on your phone
   - Bookmark it for easy access
   - Check off items as you shop

2. **Planning at home:**
   - Ask Stan to add items
   - Or edit SHOPPING.md directly
   - Or use the web app

3. **Keep in sync:**
   - Export from web app to update SHOPPING.md
   - Stan can read both sources

## Tags to Use

- `groceries` - Food and household consumables
- `amazon` - Items to order online
- `house-stuff` - Home improvement/decor
- `hardware` - Tools, fixtures, building materials
- `urgent` - Need it ASAP
- Add your own as needed!

## Future Enhancements (Optional)

Want any of these? Let Stan know:
- Todoist sync
- Amazon integration (auto-add from product searches)
- Google Shopping List sync
- Shared list with Rosa via cloud sync
- Price tracking
- Recipe ingredient import

---

Built: 2026-02-01 by Stan 🧭
