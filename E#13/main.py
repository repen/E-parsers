'''
name: E#13
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw
'''
import requests
from bs4 import BeautifulSoup

url = "https://azku.ru/russkie-narodnie-skazki/index.php"

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

elements = soup.select("div.mycontent")

stories = []

for element in elements:
    name = element.select("a")[0].text
    url = element.select("a")[0]['href']
    like = element.select("span.likes")[0].text
    stories.append([name, url, like])


string = ""
for story in stories:
    string += '\t<li><a href="{1}"> {0} </a> <span>рейтинг: {2}</span> </li>\n'.format(story[0], story[1], story[2])

ul = '''<ul>
    {}
</ul>'''.format(string)

with open("index.html", "w", encoding="utf8") as f:
    f.write(ul)