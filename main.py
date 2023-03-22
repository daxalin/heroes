from pprint import pprint
import json
import requests

def most_intelligence_hero(smart_heroes: list):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    resp = requests.get(url)
    data = resp.json()
    dic_of_heroes = {}
    for hero in data:
        if hero['name'] in smart_heroes:
            dic_of_heroes[hero['name']] = hero['powerstats']['intelligence']

    for hero, intelligence in dic_of_heroes.items():
        most = {}
        max_int = 0
        if intelligence > max_int:
            max_int = intelligence
        most[intelligence] = most.get(intelligence, [hero])
        the_hero = most[intelligence]

    return print(f'Самый умный супергерой - {the_hero}')


if __name__ == '__main__':
    most_intelligence_hero(['Hulk', 'Captain America', 'Thanos'])
