'''
name:   E#17
author: Andrey Plugin
email:  9keepa@gmail.com
link:   https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw
github: https://github.com/repen/E-parsers
'''
import requests, json



headers = '''
Host: auto.ru
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: */*
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://auto.ru/cars/vaz/2114/all/?year_from=2008&year_to=2010&sort=fresh_relevance_1-desc&page=2
x-client-app-version: 201911.26.155818
x-csrf-token: a5446446051b69f4b14cb18507b6ebb9954c6cf76b93027f
x-requested-with: fetch
content-type: application/json
Origin: https://auto.ru
Content-Length: 157
DNT: 1
Connection: keep-alive
Cookie: _csrf_token=a5446446051b69f4b14cb18507b6ebb9954c6cf76b93027f; autoru_sid=a%3Ag5dde33da257four8ct4hhlt0a17h00o.5bc9aa797010bf795c3fae4e20dd2eef%7C1574843354139.604800.PHszmA0eR_XZhCgieItl5g.WeKyrJqm5x5NmWaOBK-TLSEyI0wo2Z27miqpLLFwee8; autoruuid=g5dde33da257four8ct4hhlt0a17h00o.5bc9aa797010bf795c3fae4e20dd2eef; suid=d6c67bcdfb90c719a1008ae312af2fc9.f9f984e280d08277d997ce0fac3c604c; from_lifetime=1574843440313; from=google-search; counter_ga_all7=1; X-Vertis-DC=sas; navigation_promo_seen-recalls=true
Pragma: no-cache
Cache-Control: no-cache
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

with open("data.json", "w") as f:
    json.dump(offers, f)