'''
name: E#02
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw

MIT License https://github.com/repen/E-parsers/blob/master/License
'''

from bs4 import BeautifulSoup
import requests

url = "http://wonderful-planet.ru/gidrosfera/22-reki.html?start=8"

response = requests.get(url)

if response.status_code == 200:
    html = response.text

soup = BeautifulSoup(html, "html.parser")

table = soup.find("table")

trs = table.find_all("tr")

string = "Длина рек: \n"

for e, tr in enumerate(trs):
    if e == 0:
        continue
    tds = tr.find_all("td")
    name = tds[1].text.strip()
    length = tds[2].text.strip()
    string += "\t{}. {} {} км \n".format(e, name, length)

with open("data.txt", "w", encoding="utf8") as f:
    f.write(string)