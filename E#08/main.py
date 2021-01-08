'''
name: E#08
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw

MIT License https://github.com/repen/E-parsers/blob/master/License
'''
import json
import requests
from bs4 import BeautifulSoup

base_url = "https://www.autoscout24.com"

query = "/lst/renault?sort=price&desc=0&ustate=N%2CU&size=20&page={}&fregfrom=2015&atype=C&"

all_elements = []

for x in range(1, 21):

    response = requests.get(base_url + query.format(x))

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    elements = soup.find_all("div", {"class":"cl-list-element-gap"})

    for element in elements:
        name = element.find("div", {"class":"cldt-summary-title"}).text
        price = element.find("div", {"class":"cldt-summary-payment"}).text
        mileage = element.find("ul", {"data-item-name":"vehicle-details"}).find_all("li")[0].text
        year = element.find("ul", {"data-item-name":"vehicle-details"}).find_all("li")[1].text
        link = element.find("a", {"data-item-name":"detail-page-link"})["href"]
        all_elements.append([name, price, mileage, year, link])

    print("Status message: page = {}".format(x))


with open("data.json", "w", encoding="utf8") as f:
    json.dump(all_elements, f)

print("result: ", len(all_elements))


# with open("data.json", "r", encoding="utf8") as f:
#     data = json.load(f)

# print(len(data))