'''
name: E#12
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw
readme method HEAD: http://lib.ru/WEBMASTER/rfc2068/section-9.html#p4
'''
import requests

url = "https://www.liveinternet.ru/rating/ru//today.tsv?"

response = requests.get(url)

html = response.text

lines = html.split("\n")


for line in lines[1:-2]:
    try:
        url = "https://" + line.split("\t")[1]
        response = requests.head(url)
        print(url)
        print(response.headers)
    except:
        print("ERORR")
    print('=============')