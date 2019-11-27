import json

with open("data.json", "r", encoding="utf8") as f:
    data = json.load(f)
print(len(data))
price = []
for offer in data:
    if offer['price_info']:
        price.append(offer['price_info']['price'])

average = sum(price) / len(price)
print("Average: ", int(average))
# price = []
# for d in data:
#     if d['price_info']:
#         price.append(d['price_info']['price'])
#
# average = sum(price) / len(price)
# print(average)

