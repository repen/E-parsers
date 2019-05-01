from bs4 import BeautifulSoup
import requests


url = "http://wonderful-planet.ru/gidrosfera/22-reki.html?start=8"

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

table = soup.find("table")

lines = table.find_all("tr")

string = "Длина рек: \n"
for e, line in enumerate(lines):
    if e == 0:
        continue
    elements = line.find_all("td")
    name = elements[1].text.strip()
    length = elements[2].text.strip()
    string += "\t{}. {} {} км\n".format(e, name, length)

string += "End ======"

with open("data.txt", "w", encoding="utf8") as f_obj:
    f_obj.write(string)