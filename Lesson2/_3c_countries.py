"""
A program that takes a continent and prints
all of the countries on that continent
"""

# todo: Read data/continents.csv and save all countries by continent
import csv

with open("data/continents.csv", "r") as file:
    reader = csv.DictReader(file)

    continent_countries={}

    for line in reader:
        #print(line["Continent"])
        list_countries = []
        if line["Continent"] not in continent_countries and line["Continent"] != "Continent":
            list_countries.append(line["Country"])
            continent_countries[line["Continent"]] = list_countries

        else:
            continent_countries[line["Continent"]].append(line["Country"])

    print(continent_countries)

continents = [
    'Africa',
    'Asia',
    'Europe',
    'North America',
    'Oceania',
    'South America'
]

# Todo: Get user to provide a continent by inputting a number
number_chosen = int(input('Choose a continent:'))
print('1: Africa, 2: Asia, 3: Europe, 4: North America, 5: Oceania, 6: South America')

# Todo: Print the number of countries on that continent
print(len(continent_countries.get(continents[number_chosen-1])))

# Todo: Print each of the countries on that continent to the console
print(continent_countries.get(continents[number_chosen-1]))