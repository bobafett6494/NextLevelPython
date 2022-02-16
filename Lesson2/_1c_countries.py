"""
A program that takes a letter and prints
all of the countries that start with that letter
"""

# Todo: Read data/countries.txt and save all countries
with open("data/countries.txt", "r") as file:
    list_countries = []
    for line in file.readlines():
        list_countries.append(line)

# Get user to provide a letter
letter = input('Number of countries that start with letter: ')
letter = letter.capitalize()

# Todo: Print the number of countries that start with the letter
#count = 0
list_countries_startwithletter = []
for country in list_countries:
    if country.startswith(letter): #Or country[0].upper() == letter
        #count +=1
        list_countries_startwithletter.append(country)
print(f"Number of countries starting with chosen letter '{letter}': {len(list_countries_startwithletter)}")

# Todo: Print the countries that start with the letter

print(f"List of countries starting with chosen letter: {list_countries_startwithletter}")
