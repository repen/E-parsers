'''
name:   E#18
author: Andrey Plugin
email:  9keepa@gmail.com
link:   https://www.youtube.com/channel/UCNN3bpPlWWUkUMB7gjcUFlw
github: https://github.com/repen/E-parsers
covid-19 api repo: https://github.com/pomber/covid19


Copyright (c) 2019 - 2021 Andrey Plugin
MIT License https://github.com/repen/E-parsers/blob/master/License
'''
import requests
from string import Template
covid_api19 = "https://pomber.github.io/covid19/timeseries.json"
response = requests.get(covid_api19)
data = response.json()


def read_template(path):
    with open(path, encoding="utf8") as f:
        html = f.read()
    return html

def output(html, path):
    with open( path , "w", encoding="utf8") as f:
        f.write( html )

def get_country(country):
    country = country.title()
    if country in data.keys():
        return data[ country ]
    else:
        print("sorry no such country")
        return False

def generate_chart_ver01(template_html, data, country):
    date = [x["date"] for x in data]
    confirmed = [x["confirmed"] for x in data]
    deaths = [x["deaths"] for x in data]
    recovered = [x["recovered"] for x in data]
    dataset_template = '''
    { 
        data: $array,
        label: "$field",
        borderColor: "$color",
        fill: false
    }
    '''.strip()
    dataset_template = Template( dataset_template )
    html = Template( template_html )

    template_array = [
        dataset_template.substitute(array=confirmed, field="confirmed", color="#A14C4C" ),
        dataset_template.substitute(array=deaths,    field="deaths", color="#583333" ),
        dataset_template.substitute(array=recovered, field="recovered", color="#4A9969" )
    ]

    join = ",\n".join( template_array )

    return html.substitute( datasets=join, country=country, labels=str(date) )

def generate_chart_ver02( template_html, data ):
    dataset_element = '''
    {
        label: "$country",
        backgroundColor: "#326fa8",
        borderColor: "#AC7979",
        borderWidth: 1,
        data: $data
    } 
    '''.strip()
    labels = ['confirmed', 'deaths', 'recovered']
    dataset_element = Template( dataset_element )
    template_html   = Template( template_html )
    build = []

    for country in data:
        temp = [x for x in country[1][-1].values()][1:]
        build.append( dataset_element.substitute( country=country[0], data=temp ) )

    join = ",\n".join( build )

    return template_html.substitute( labels = str( labels ), datasets = join )

# chart 1
html01   = read_template("template01.html")
italy    = get_country("russia")[-45:]
chart_01 = generate_chart_ver01(html01, italy, "Russia")
output( chart_01, "output01.html" )

# chart 2
# ===================
c = ["Italy", "Argentina"]
html02 = read_template("template02.html")
prepare_data = [ [k,v] for k,v in data.items() ]
prepare_data = list( filter( lambda x: x[0] in c, prepare_data) )
chart_02 = generate_chart_ver02( html02, prepare_data )
output( chart_02, "output02.html" )
