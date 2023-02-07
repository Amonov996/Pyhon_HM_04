from main import data
# 7 - masala Barcha "Assistant" larni "Junior" pazitsiyaga o'tqazing
# misol -> "Assistant Professor" -> "Junior Professor"
# pprint.pprint(data[0])
dd = data.copy()
for i in dd:
    if "Assistant" in i["position"]:
        i["position"] = i["position"].replace("Assistant", "Junior")
        print(i)


