import re
import json

path = r"C:\Users\Jalica Macalabo\.gemini\antigravity\brain\312cb222-e586-453a-ac33-0afcc3b968b1\.system_generated\steps\72\content.md"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Let's search for categories and their products
categories = []
cat_matches = re.finditer(r'"RestaurantMenuCategory:[0-9]+":\{"__typename":"RestaurantMenuCategory","id":"[0-9]+","code":"[^"]+","title":"([^"]+)","masterCategory":\{"__ref":"[^"]+"\},"description":"([^"]*)","partner":null,"products":(\[[^\]]+\])\}', text)

for cm in cat_matches:
    cat_title = cm.group(1)
    cat_desc = cm.group(2)
    prod_refs = json.loads(cm.group(3))
    prod_ids = [p["__ref"].split(":")[-1] for p in prod_refs]
    categories.append({
        "category": cat_title,
        "description": cat_desc,
        "product_ids": prod_ids
    })

# Extract all products
products_dict = {}
prod_matches = re.finditer(r'"RestaurantProductData:([0-9]+)":\{"__typename":"RestaurantProductData","id":"[0-9]+","code":"[^"]+","title":"([^"]+)","description":"([^"]*)","image":\{"__typename":"ProductImage","url":"([^"]*)"\}', text)

for pm in prod_matches:
    pid = pm.group(1)
    title = pm.group(2)
    desc = pm.group(3)
    img = pm.group(4).replace(r"\u002F", "/")
    
    # search around product in text for variation / price
    idx = text.find(f'"RestaurantProductData:{pid}"')
    chunk = text[idx:idx+3500] if idx != -1 else ""
    
    # Try finding price
    price_val = "₱..."
    p_match = re.search(r'"price":\{"__typename":"ProductPrice","regular":\{"__typename":"RegularPrice","formatted":"([^"]+)"', chunk)
    if p_match:
        price_val = p_match.group(1)
    else:
        p_match2 = re.search(r'"formatted":"(₱[^"]+)"', chunk)
        if p_match2:
            price_val = p_match2.group(1)
        else:
            p_match3 = re.search(r'"price":([0-9]+(?:\.[0-9]+)?)', chunk)
            if p_match3:
                price_val = f"₱{float(p_match3.group(1)):.2f}"

    products_dict[pid] = {
        "id": pid,
        "title": title,
        "description": desc,
        "image": img,
        "price": price_val
    }

menu_output = {
    "categories": categories,
    "products": products_dict
}

with open("hungry_pair_menu.json", "w", encoding="utf-8") as out:
    json.dump(menu_output, out, indent=2, ensure_ascii=False)

print("Saved hungry_pair_menu.json! Total categories:", len(categories), "Total products:", len(products_dict))
for cat in categories:
    print(f"\n--- {cat['category']} ({len(cat['product_ids'])} items) ---")
    for pid in cat['product_ids']:
        if pid in products_dict:
            p = products_dict[pid]
            print(f"  * {p['title']} [{p['price']}] - {p['description'][:60]}... Img: {p['image']}")
