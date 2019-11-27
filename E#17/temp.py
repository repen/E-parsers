'''
name:   E#17
author: Andrey Plugin
email:  9keepa@gmail.com
link:   https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw
github: https://github.com/repen/E-parsers
'''


import requests, json

def save_json(path, data):
    with open(path, "w", encoding="utf8") as f:
        json.dump(data, f)

headers = '''
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/47.0.2526.70 Mobile/13C71 Safari/601.1.460
Accept: */*
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
x-client-app-version: 201911.15.132749
x-csrf-token: 41ab8a5cb20867461c066b720df26a56c3967960b455b48b
x-requested-with: fetch
content-type: application/json
Origin: https://auto.ru
DNT: 1
Connection: keep-alive
Cookie: suid=3f7377f2c7b6f8da4a83196b787ea3e8.e30892c70373a256b1f1a75988adc928; _ym_uid=1572380208347807999; _ym_d=1573977516; _csrf_token=41ab8a5cb20867461c066b720df26a56c3967960b455b48b; from_lifetime=1573977516501; from=morda; autoru_sid=a%3Ag5dd0f70e221icfi0go57fck6m9vcbv2.62c5a974f09df4cc20571a1e2dd2488b%7C1573975822024.604800.eXp_NovCThAgrmtGeifSjA.99wg45XwFNaKPWWPw3kgm9-OBghIP4YcWuSpEKzHXOo; autoruuid=g5dd0f70e221icfi0go57fck6m9vcbv2.62c5a974f09df4cc20571a1e2dd2488b; X-Vertis-DC=myt; my=YwA%3D; crookie=tGSxf3gQd5zEwhAw74RaDhIHVaAD6kDX3goevm7rY7YtrCHHVAUI9AIgsp0FZpa6LRqdbqp5grBWSk3pj7EI8G1Z0xQ=; cmtchd=MTU3Mzk3NTgyODM3OQ==; navigation_promo_seen-recalls=true; los=1; bltsr=1
Pragma: no-cache
Cache-Control: no-cache
'''.strip()
headers_dict = {}
for x in headers.split("\n"):
    header = x.split(": ")
    headers_dict[header[0]] = header[-1]

url = "https://auto.ru/-/ajax/desktop/listing/"

offers = []
for page in range(1, 5):
    params = {"year_from": 2008, "year_to": 2010,
              "catalog_filter": [{"mark": "VAZ", "model": "2114"}],
              "section": "all", "category": "cars", "sort": "fresh_relevance_1-desc", "page": page}
    response = requests.post(url, json=params, headers=headers_dict)
    offers.extend(response.json()['offers'])
    print("current page: ", page)

save_json("data.json", offers)
