import requests
from bs4 import BeautifulSoup


url = "http://statistic.su/blog/earth_distance/2010-07-14-7"

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

uls = soup.find_all("ul")

arr_data = []

for ul in uls:
    if "Меркурий" in ul.text:
        data = ul.text.strip().split("\n")

for d in data:
    temp = d.replace(" ","").split("-")
    temp[1] = int(float(temp[1]) * 1000000)
    arr_data.append(temp)


arr_data = sorted(arr_data, key=lambda x: x[1], reverse=True)

string = "Наименьшее расстояние от этих планет до Земли: \n"

i = 1
for data in arr_data:
    string += "\t{}. {} {} км. \n".format(i, data[0], data[1])
    i += 1

with open("data.txt", "w", encoding="utf8") as f_obj:
    f_obj.write(string)