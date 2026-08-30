import json
import re

path = r"C:\Users\Jalica Macalabo\.gemini\antigravity\brain\312cb222-e586-453a-ac33-0afcc3b968b1\.system_generated\steps\72\content.md"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

print("File size:", len(text))

# Let's search for JSON data in text (like __NEXT_DATA__ or state)
next_data = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', text, re.DOTALL)
if next_data:
    try:
        data = json.loads(next_data.group(1))
        print("Found NEXT_DATA successfully!")
        
        # Let's find menu categories and products in the JSON
        def search_dict(d, depth=0):
            if isinstance(d, dict):
                if "categories" in d or "menu_categories" in d or "products" in d:
                    print("Found menu structures at depth", depth, d.keys())
                for k, v in d.items():
                    if k in ["name", "description", "price", "category"]:
                        pass
                    search_dict(v, depth+1)
            elif isinstance(d, list):
                for item in d:
                    search_dict(item, depth+1)
        
        search_dict(data)
    except Exception as e:
        print("Error parsing JSON:", e)

# Also let's extract strings containing food items or keywords
# Find all occurrences of product names or dish names
patterns = [
    r'\{"id":[0-9]+,"name":"([^"]+)","description":"([^"]*)","price":([0-9.]+)',
    r'"name":"([^"]+)","description":"([^"]*)".*?"price":\{"regular":([0-9.]+)',
    r'class="dish-name"[^>]*>([^<]+)<',
    r'data-testid="menu-product-item"[^>]*>.*?<h3>([^<]+)</h3>',
]

for p in patterns:
    matches = re.findall(p, text, re.DOTALL)
    print(f"Pattern '{p[:30]}...' found {len(matches)} matches")
    for m in matches[:15]:
        print("  Match:", m)

# Let's search for seafood, chicken, wings, rice, etc.
keywords = ["Bucket", "Wing", "Seafood", "Shrimp", "Crab", "Rice", "Salmon", "Tuna", "Katsu", "Teriyaki", "Donburi", "Platter", "Pork", "Beef", "Pasta", "Milktea", "Drink"]
for kw in keywords:
    kw_matches = re.findall(rf'([A-Za-z0-9\s-]{{3,40}}{kw}[A-Za-z0-9\s-]{{0,40}})', text, re.IGNORECASE)
    unique = list(set([m.strip() for m in kw_matches if len(m.strip()) < 50]))
    if unique:
        print(f"Keyword '{kw}':", unique[:8])
