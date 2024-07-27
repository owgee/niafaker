import json
import random

def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

data = load_data('niafaker/data/addresses.json')

def get_address(country=None, city=None):
    if country and country in data:
        if city and city in data[country]:
            return random.choice(data[country][city])
        else:
            city = random.choice(list(data[country].keys()))
            return random.choice(data[country][city])
    else:
        country = random.choice(list(data.keys()))
        city = random.choice(list(data[country].keys()))
        return random.choice(data[country][city])
