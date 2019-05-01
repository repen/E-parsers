'''
name: E#04
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw
'''

import requests
from bs4 import BeautifulSoup

url = "https://www.worldfootball.net/teams/leicester-city/2013/3/"

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

table = soup.find("table", {"class":"standard_tabelle"})

lines = table.find_all("tr")

count = 0
i = 0
for line in lines:
    elements = line.find_all("td")
    if len(elements) == 8:
        count += int(elements[6].text.strip().split(":")[0])
        i += 1

mean = "{0:.2f}".format((count / i))
print(mean)