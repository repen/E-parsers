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

query = quote_plus("5fiesta")

response = requests.get(base_url + query)

html = response.text
# print(html)

soup = BeautifulSoup(html, "html.parser")

song_ids = soup.select("div[id].title_wrap")

for e, s_id in enumerate(song_ids):
    if e == 5:
        break
    name_song = s_id.select("span.title-name")[0].text
    with open("{}.mp3".format(name_song), "wb") as f:
        song_url = "https://useraudio.net/?do=getById&id={}".format(s_id["data-songid"])
        content = requests.get(song_url).content
        print("\t length: %10.2f МБ" % (len(content) / 2**20))
        f.write(content)
    print("Status parse: {}".format(len(song_ids) - e))
    print("\t Download: {}.mp3".format(name_song))


