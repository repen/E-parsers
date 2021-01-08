'''
name:   E#17
author: Andrey Plugin
email:  9keepa@gmail.com
link:   https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw
github: https://github.com/repen/E-parsers

MIT License https://github.com/repen/E-parsers/blob/master/License
'''
import requests, json



headers = '''
Host: auto.ru
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: */*
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://auto.ru/cars/vaz/2114/all/?output_type=list&page=3
x-client-app-version: 202012.04.170215
x-page-request-id: 7bc7a1c830b9a3eaf343779a7a503ecf
x-client-date: 1607175337370
x-csrf-token: 58b9bf17d302f4fbbf3287a2bf30dda4fe2fb72585b563f2
x-requested-with: fetch
content-type: application/json
Origin: https://auto.ru
Content-Length: 114
DNT: 1
Connection: keep-alive
Cookie: _csrf_token=58b9bf17d302f4fbbf3287a2bf30dda4fe2fb72585b563f2; autoru_sid=a%3Ag5fcb8bc02sbhlh52qn9n4lu0pp9j5un.554b8700bc90755ef49149fec0c1286a%7C1607175104363.604800.f9IX1HCBLa9YqgknRnpRWg.JIZvbONlVKA_4r9c5mZnaTm-onpLMj1zz5lcbgVw2uQ; autoruuid=g5fcb8bc02sbhlh52qn9n4lu0pp9j5un.554b8700bc90755ef49149fec0c1286a; suid=afbc21b5f67f69334d1804ebb97ba74d.b539c93b813155527740bdb39af11ec6; from_lifetime=1607175327785; from=google-search; counter_ga_all7=1; yuidcs=1; X-Vertis-DC=myt; yuidlt=1; yandexuid=493122311571839213; my=YwA%3D; crookie=fjp0nU5rP3C5KUj8EbcOnpYc8V1fb2zvfGJu5b1Dt0lkSY6EG3ml6+uV6Tc2PpdLX0xQkhebFuoJCZedFlNlexUqHvc=; cmtchd=MTYwNzE3NTExMDUxNQ==; bltsr=1
'''.strip().split("\n")

url = "https://auto.ru/-/ajax/desktop/listing/"
dict_headers = {}
for header in headers:
    key, value = header.split(': ')
    dict_headers[key] = value
# print(dict_headers)
offers = []
for x in range(3, 12):
    param = {
        "year_from":2008,
        "year_to":2010,
        "catalog_filter":[{"mark":"VAZ","model":"2114"}],
        "section":"all",
        "category":"cars",
        "sort":"fresh_relevance_1-desc",
        "page":x,
    }
    response = requests.post(url, json=param, headers = dict_headers)
    data = response.json()
    offers.extend(data['offers'])
    print("current page: ", x)

with open("data.json", "w", encoding="utf8") as f:
    json.dump(offers, f)