'''
name: E#14
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw

MIT License https://github.com/repen/E-parsers/blob/master/License
'''
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

all_tags = soup.find_all(True)

print(len(all_tags))
tags = []

for tag in all_tags:
    tags.append(tag.name)

stat_tags = sorted([[x, tags.count(x)] for x in set(tags)], key = lambda x : x[1], reverse = True)
print(stat_tags)