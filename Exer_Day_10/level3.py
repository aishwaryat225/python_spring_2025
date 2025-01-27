# Assuming countries.py contains a list called `countries`
from data.countries import countries

land_countries = [country for country in countries if 'land' in country]
print("Countries containing 'land':", land_countries)


fruits = ['banana', 'orange', 'mango', 'lemon']


reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print("Reversed fruit list:", reversed_fruits)


# Assuming countries_data.py contains a list called `countries_data`
from data.countries_data import countries_data

languages = set()
for country in countries_data:
    languages.update(country['languages'])

print("Total number of languages:", len(languages))

from collections import Counter

language_counter = Counter()
for country in countries_data:
    language_counter.update(country['languages'])

most_spoken_languages = language_counter.most_common(10)
print("Ten most spoken languages:")
for language, count in most_spoken_languages:
    print(f"{language}: {count} countries")

