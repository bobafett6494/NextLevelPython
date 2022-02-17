"""
A program that takes a continent and prints
all of the countries on that continent
"""

# todo: Read data/continents.csv and save all countries by continent
import csv

with open("data/continents.csv", "r") as file:
     reader = csv.DictReader(file)

print(reader)

continent_countries={}
for line in reader:
    continent_countries['XX'] = 'New capital'

continents = [
    'Africa',
    'Asia',
    'Europe',
    'North America',
    'Oceania',
    'South America'
]

# Todo: Get user to provide a continent by inputting a number
print('Choose a continent:')
print('1: Africa, 2: Asia, 3: Europe, 4: North America, 5: Oceania, 6: South America')

# Todo: Print the number of countries on that continent

# Todo: Print each of the countries on that continent to the console
