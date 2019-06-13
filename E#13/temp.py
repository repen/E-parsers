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
    url = element.select("a")[0]["href"]
    like = int(element.select("span.likes")[0].text)
    
    stories.append([name, url, like])

stories_sort = stories

tags = ""
for story in stories_sort:
    tags += '<li><a href="{1}" target="_blank"> {0} </a> <span> рейтинг: {2} </span> </li>\n'.format(story[0], story[1], story[2])
print(tags)
ul ='''
      <ul>
        {}
      </ul>
    '''.format(tags)

print(ul)

with open("page.html", "w", encoding = "utf8") as f:
    f.write(ul)