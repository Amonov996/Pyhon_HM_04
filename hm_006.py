from main import data
# 6 - masala "Assistant" lar soni nechtaligini hisoblang
count =0
for i in data:
    if "Assistant" in i["position"] :
        count += 1

print(f"Assistantlar soni {count} ta.")