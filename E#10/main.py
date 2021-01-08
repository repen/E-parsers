'''
name: E#10
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw

MIT License https://github.com/repen/E-parsers/blob/master/License
'''
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, quote_plus

base_url = "https://useraudio.net/search/"

query = quote_plus("prodigy")

response = requests.get(base_url + query)

html = response.text
# print(html)

soup = BeautifulSoup(html, "html.parser")

songs = soup.select("div.title_wrap[id]")

all_songs = []
for song in songs:
    url = "https://useraudio.net/?do=getById&id=" + song["data-songid"]
    name = song.select("span.title-name")[0].text + ".mp3"
    all_songs.append([url, name])

for e, song in enumerate(all_songs):
    if e == 5:
        break
    with open(song[1], "wb") as f:
        response = requests.get(song[0]).content
        f.write(response)



