'''
name: E#06
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw
'''

import requests
from bs4 import BeautifulSoup
import random

random_url = "https://filmets.net/films/fantastika/page/{}/".format(random.randint(1,29))

response = requests.get(random_url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

films = soup.find_all("div", {"class":"film"})


film = random.choice(films)

name = film.find("div", {"class":"title"}).text
category = film.find("div", {"class":"category"}).text
rate = film.find("div", {"class":"rate"}).text
year = film.find("span", {"class":"sh_year"}).text
link = film.find("div", {"class":"title"}).a["href"]

string_info = "Случайный фильм: \n"
string_info += "\tНазвание: {} \n".format(name)
string_info += "\tКатегория: {} \n".format(category.replace(" ",""))
string_info += "\tРейтинг: {} \n".format(rate)
string_info += "\tГод: {} \n".format(year)
string_info += "\tСсылка: {} \n".format(link)

print(string_info)