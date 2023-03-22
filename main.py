from pprint import pprint

import json
import requests

def most_intelligence_hero():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    resp = requests.get(url)
    data = resp.json()
    list_of_heroes = ['Hulk', 'Captain America', 'Thanos']
    for hero in data:
        if hero['name'] in list_of_heroes:
            print(f'{hero['powerstats']['intelligence']}')

    #return data


pprint(most_intelligence_hero())

