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

soup = BeautifulSoup(html, "html.parser")

multiclass = "product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12".split(" ")

products = soup.find_all("div", {"class":"col-xs-12"})

all_products = []
for product in products:
    if product.attrs['class'] == multiclass:
        image = product.find("img").attrs["src"]
        name = product.find("div", class_="product-name").text.strip()
        code = product.find("div", class_="product-model").text.strip()
        description = product.find("div", class_="product-description").text.strip()
        price = product.find("p", class_="price").text.strip().replace("р.", "")
        all_products.append([name, description , code , price])


names = ["Наименование", "Описание", "Артикл", "Цена"]


with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(names)
    
    for product in all_products:
        writer.writerow(product)