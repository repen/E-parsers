'''
name:   E#18
author: Andrey Plugin
email:  9keepa@gmail.com
link:   https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw
github: https://github.com/repen/E-parsers
covid-19 api repo: https://github.com/pomber/covid19

MIT License https://github.com/repen/E-parsers/blob/master/License
'''
import requests

covid19_api = "https://pomber.github.io/covid19/timeseries.json"

response = requests.get( covid19_api )
data = response.json()
country_list = data.keys()
print(country_list)
italy = data['Italy'][-1]
print( italy )