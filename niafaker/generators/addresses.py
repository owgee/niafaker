import json
import pkg_resources
import random

def load_data(filename):
    resource_path = pkg_resources.resource_filename(__name__, f'../data/{filename}')
    with open(resource_path, 'r') as file:
        return json.load(file)

data = load_data('addresses.json')['addresses']

def generate_address(country=None, city=None):
    if country and country in data:
        if city and city in data[country]:
            return generate_item(data[country][city])
        else:
            city = generate_item(list(data[country].keys()))
            return generate_item(data[country][city])
    else:
        country = generate_item(list(data.keys()))
        city = generate_item(list(data[country].keys()))
        return generate_item(data[country][city])

def generate_item(items):
    return random.choice(items)
