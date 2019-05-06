'''
name: E#05
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw
'''

import csv
import requests
from bs4 import BeautifulSoup

url = "http://sportunit.ru/velosipedy?limit=100"

response = requests.get(url)

html = response.text

multi_class = "product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12".split(" ")

soup = BeautifulSoup(html, "html.parser")

products = soup.find_all("div", {"class":"col-xs-12"})

all_products = []
for product in products:
    if product.attrs["class"] == multi_class:
        image = product.find("img")["src"]
        name = product.find("div", {"class":"product-name"}).text
        code = product.find("div", {"class":"product-model"}).text
        description = product.find("div", {"class":"product-description"}).text
        price = product.find("p", {"class":"price"}).text.strip().replace("р.","")
        all_products.append([name, code, description, price])



names = ["Наименование", "Артикл", "Описание", "Цена"]

with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(names)
    
    for product in all_products:
        writer.writerow(product)