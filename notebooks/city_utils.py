import json


def load_cities():
    """
    Load city list from 'us-cities.json'
    """
    with open('us-cities.json', 'r') as f:
        cities = json.load(f)
    return cities


def save_cities(cities, filename):
    """
    Save the city list in a JSON file
    """
    with open(filename, 'w') as f:
        json.dump(cities, f)
        
        
number_of_cities = 1000


print('Hey I am a module!')