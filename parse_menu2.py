import json
import re

path = r"C:\Users\Jalica Macalabo\.gemini\antigravity\brain\312cb222-e586-453a-ac33-0afcc3b968b1\.system_generated\steps\72\content.md"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Let's search for JSON data in text
# In foodpanda HTML, products are often in state JSON:
matches = re.findall(r'(\{"name":"[^"]+","description":"[^"]*",[^}]+?\})', text)
print("JSON item matches:", len(matches))

# Let's search for menu sections in text
all_names = re.findall(r'"name":"([^"]+)"', text)
# filter out non-dish names
dish_candidates = [n for n in all_names if len(n) > 3 and not n.startswith("http") and not n.startswith("GTM") and not n.startswith("PH") and n not in ["Home", "Calamba Laguna", "Hungry Pair - Burgos Street", "Seafood", "Chicken", "Rice Dishes", "Rice Bowl", "Chicken Wings"]]
print("Dish candidates:", len(dish_candidates))
for d in set(dish_candidates):
    print(" -", d)

# Also let's extract price and description associated with them
for d in list(set(dish_candidates))[:30]:
    pattern = rf'"{re.escape(d)}"[^}}]+?"description":"([^"]*)"[^}}]*?"price":([0-9.]+)'
    m = re.search(pattern, text)
    if m:
        print(f"Details: {d} | Desc: {m.group(1)} | Price: {m.group(2)}")
    else:
        pattern2 = rf'"{re.escape(d)}".*?([0-9]{{2,4}}\.[0-9]{{2}})'
        m2 = re.search(pattern2, text[:50000])
        # print(f"Alt: {d}")
