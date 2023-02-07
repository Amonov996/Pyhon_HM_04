# 5 - masala "position" keyning "valuesida" -> "senior" yoki "junior"
# satri bor barcha hodimlarni o'chirib tashlang
from pprint import pprint as print
from main import data
newData = data.copy()
newlist = []
print(len(newData))

# for i in newData:
#     if i['position'][0:6] in "Senior" or i['position'][:6] in "Junior":
#         i
for i in range(len(newlist)):
    if i['position'][0:6] != "Senior" or i['position'][:6] != "Junior":
        del i

# print(newData)
print(len(newData))
# print(data)
