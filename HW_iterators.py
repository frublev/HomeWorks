import json


class Country:
    def __init__(self, countries):
        self.countries = countries
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start != len(self.countries):
            return self.countries[self.start]['name']['common']
        else:
            raise StopIteration


if __name__ == '__main__':
    with open("countries.json") as read_file:
        countries_info = json.load(read_file)
    countries_name = Country(countries_info)

    with open("country-link.txt", "w", encoding="utf8") as country_link:
        for country in countries_name:
            country_link.write(country + ' - ' + "https://en.wikipedia.org/wiki/" + country.replace(' ', '_') + '\n')
