import requests


class SuperHero:
    def __init__(self, name):
        self.name = name
        self.api = "https://superheroapi.com/api/2619421814940190/search/" + self.name

    def intelligence(self):
        response = requests.get(self.api)
        hero_intelligence = response.json()
        hero_intelligence = int(hero_intelligence['results'][0]['powerstats']['intelligence'])
        return hero_intelligence

    def __gt__(self, other):
        return self.intelligence() > other.intelligence()


super_heroes = ["Hulk", "Thanos", "Captain America"]
super_hero = ''
intelligence = 0

for hero in super_heroes:
    print(SuperHero(hero).name, SuperHero(hero).intelligence())
    if SuperHero(hero).intelligence() > intelligence:
        intelligence = SuperHero(hero).intelligence()
        super_hero = SuperHero(hero).name
print(f"Самый умный супергерой -  {super_hero}")
