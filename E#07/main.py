'''
name: E#07
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw
'''

import requests
from bs4 import BeautifulSoup


url = "https://cz.mobileshop.eu/tablety/apple/"

cookie = {"Cookie": "__cfduid=d9ed411c2c3d886bad5652449685c5da31557408559; PHPSESSID=s87klemkcrkd4je1b7scplvj34; cookieNotification=true; SelCurrency=EUR"}

response = requests.get(url, cookies=cookie)

html = response.text

soup = BeautifulSoup(html, "html.parser")

conteiner = soup.find("ul", {"class":"products"})

products = conteiner.find_all("li")

print(len(products))

for product in products:
    name = product.find("span").text
    price = int(product.find("div", class_="price").text[:-2]) * 72
    print(name, price)