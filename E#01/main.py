'''
name: E#01
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/user/9keepa/videos
'''

import requests
from bs4 import BeautifulSoup

url = "http://light-science.ru/kosmos/vselennaya/top-10-samyh-bolshih-zvezd-vo-vselennoj.html"

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; \
                                x64; rv:47.0) Gecko/20100101 Firefox/48.0'}

response = requests.get(url, headers=header)

html = response.text

soup = BeautifulSoup(html, "html.parser")

conteiner = soup.find("div", {"class":"td-post-content"})

elements = conteiner.find_all("p")

string = "топ звезд самых больших: \n"


for element in elements:
    if element.find("strong"):
        string += "\t" + element.strong.text + "\n"

with open("data.txt", "w", encoding="utf8") as f:
    f.write(string)