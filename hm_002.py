# 2 - "Riffpath" kompaniyasida ishlaydigan barcha
# hodimlarga qancha maosh to'lanishini hisoblang
# (maosh olida $ belgisi bor e'tiborli bo'ling)

from main import data
companyName = "Riffpath"

sumSalary = 0
for i in data:
    if i['company'] in companyName:
        print(i["salary"])
        sumSalary += float(i["salary"][1::])

print(sumSalary)