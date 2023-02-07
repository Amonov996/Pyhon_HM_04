# 1 - masala: Human Resources Manager bo'limida nechta odam ishlashini hisoblang
from main import data

count =0
searchingPosition = "Human Resources Manager"

for i in data:
    if i["position"] in searchingPosition:
        count+=1
print(count)
