# 3 - Ismi "K" dan boshlanadigan hodimlarni oyligini 2-karra oshiring

from main import data

for i in data:
    if i["full_name"][0] in "K":
        i["salary"] = float( i["salary"][1::])*2
        print(i)
