'''
name: E#09
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw

MIT License https://github.com/repen/E-parsers/blob/master/License
'''
import requests
from bs4 import BeautifulSoup

base_url = "https://wallpapershome.com"

space = "/space/?page=4"

response = requests.get(base_url + space)

html = response.text

soup = BeautifulSoup(html, "html.parser")

conteiner = soup.find("div", {"class":"pics"})

images = conteiner.find_all("p")

print(len(images))

urls_images = []
for image in images:
    id_image = image.a["href"].split("-")[-1].replace(".html","")
    urls_images.append("https://wallpapershome.com/images/pages/pic_h/{}.jpg".format(id_image))

for e, url in enumerate(urls_images, start = 1):
    image = requests.get(url).content
    with open("image_{}.jpg".format(e), "wb") as f:
        f.write(image)
