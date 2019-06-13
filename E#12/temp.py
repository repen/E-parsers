'''
name: E#12
author: Andrey Plugin
email: 9keepa@gmail.com
link: https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw
'''
import requests

url = "https://www.liveinternet.ru/rating/ru//today.tsv?"

response = requests.get(url)

html = response.text

als = html.split("\n")

for al in als[1:10]:
    url = "https://" + al.split("\t")[1]
    print(url)
    try:
        header = requests.head(url)
        print(header.headers)
    except:
        print("ERROR")    
    print("===============")


