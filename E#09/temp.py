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
space = "/space?page=4"

response = requests.get(base_url + space)

html = response.text

# print(html)
soup = BeautifulSoup(html, "html.parser")

conteiner = soup.find("div", {"class":"pics"})

images = conteiner.find_all("p")

urls_images = []
for image in images:
    id_img = image.a["href"].split("-")[-1].replace(".html","")
    urls_images.append("https://wallpapershome.com/images/pages/pic_h/" + id_img + ".jpg")
    # break

images_byte = []
for url in urls_images:
    images = requests.get(url)
    images_byte.append(images.content)
    # break

for e, image in enumerate(images_byte):
    # print(image)
    with open("image{}.jpg".format(e), "wb") as f:
        f.write(image)