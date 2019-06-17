'''
name: E#14
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw
'''
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

tags01 = soup.find_all(True)

print(len(tags01))

tags02 = []
for tag in tags01:
    tags02.append(tag.name)

tags03 = set(tags02)

result = []
for tag in tags03:
    res = tags02.count(tag)
    result.append([tag, res])

print(result)