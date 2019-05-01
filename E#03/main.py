'''
name: E#03
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/user/9keepa/videos
'''

import requests
from bs4 import BeautifulSoup

url = "http://statistic.su/blog/earth_distance/2010-07-14-7"

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

uls = soup.find_all("ul")

# print(len(uls))
arr_data = []
for ul in uls:
    if "Меркурий" in ul.text:
        data = ul.text.strip().split("\n")

for d in data:
    temp = d.replace(" ","").split("-")
    temp[1] = int(float(temp[1]) * 1000000)
    arr_data.append(temp)

arr_data = sorted(arr_data, key=lambda x: x[1], reverse=True)

# print(arr_data)
n = 1
print("Наименьшее растоняие от Земли до планет: ")
for data in arr_data:
    print("\t",n, data[0], data[1])
    n += 1