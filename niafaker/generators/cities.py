import json
import random

def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

data = load_data('niafaker/data/cities.json')

def get_city(country=None):
    if country and country in data:
        return random.choice(data[country]['cities'])
    else:
        country = random.choice(list(data.keys()))
        return random.choice(data[country]['cities'])
