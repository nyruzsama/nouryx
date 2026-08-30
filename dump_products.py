import re
import json

path = r"C:\Users\Jalica Macalabo\.gemini\antigravity\brain\312cb222-e586-453a-ac33-0afcc3b968b1\.system_generated\steps\72\content.md"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Let's find all RestaurantProductData objects
products = re.findall(r'"RestaurantProductData:([0-9]+)":\{"__typename":"RestaurantProductData","id":"[0-9]+","code":"[^"]+","title":"([^"]+)","description":"([^"]*)","image":\{"__typename":"ProductImage","url":"([^"]*)"\}', text)

print("Found products count:", len(products))
all_prods = {}
for pid, title, desc, img in products:
    all_prods[pid] = {
        "id": pid,
        "title": title.strip(),
        "description": desc.strip(),
        "image": img.replace(r"\u002F", "/")
    }

# Also let's find prices in RestaurantVariationData
variations = re.findall(r'"RestaurantVariationData:([0-9]+)":\{"__typename":"RestaurantVariationData","id":"[0-9]+","code":"[^"]+","price":\{"__typename":"ProductPrice","regular":\{"__typename":"RegularPrice","formatted":"([^"]+)"', text)
print("Found variations:", len(variations))

# Let's also look for price mappings in the raw string
for pid, info in all_prods.items():
    # search around product id for price
    idx = text.find(f'"RestaurantProductData:{pid}"')
    price_match = re.search(r'"price":\{"__typename":"ProductPrice","regular":\{"__typename":"RegularPrice","formatted":"([^"]+)"', text[idx:idx+3000])
    if price_match:
        info["price"] = price_match.group(1)
    else:
        # try another price format
        price_match2 = re.search(r'"formatted":"(₱\s*[0-9,.]+)"', text[idx:idx+3000])
        if price_match2:
            info["price"] = price_match2.group(1)
        else:
            info["price"] = "₱..."

for pid, info in all_prods.items():
    print(f"ID: {pid} | Title: {info['title']} | Price: {info.get('price')} | Img: {info['image']}")
    print(f"   Desc: {info['description']}\n")

# Let's also find all menu categories:
cats = re.findall(r'"RestaurantMenuCategory:[0-9]+":\{"__typename":"RestaurantMenuCategory","id":"[0-9]+","code":"[^"]+","title":"([^"]+)"', text)
print("Categories:", set(cats))
