'''
name: E#11
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw
'''
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.liveinternet.ru/stat/ru/oses.html"
query_string = "?date={}&period=month&per_page=20"

data = []

for x in range(1,4):

    date = "2019-0{}-01".format(x)

    response = requests.get(url + query_string.format(date))

    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table", {"bgcolor": "#e8e8e8"})

    lines = table.find_all("tr")

    current = {date: []}

    for line in lines[1:-4]:
        name = line.find_all("td")[1].text.strip()
        count = line.find_all("td")[2].text.strip().replace(",","")
        current[date].append([name, count])

    data.append(current)

with open("data.json", "w", encoding="utf8") as f:
    json.dump(data, f)


# with open("data.json", "r", encoding="utf8") as f:
#     data = json.load(f)

# print(data[0])
# print(data[1])
# print(data[1])




