import json
import pkg_resources
import random

def load_data(filename):
    resource_path = pkg_resources.resource_filename(__name__, f'../data/{filename}')
    with open(resource_path, 'r') as file:
        return json.load(file)

data = load_data('countries.json')['countries']

def generate_city(country=None):
    if country and country in [c['name'] for c in data]:
        country_data = next(c for c in data if c['name'] == country)
        return generate_item(country_data['cities'])
    else:
        country_data = generate_item(data)
        return generate_item(country_data['cities'])

# Pick an item (city) at random
def generate_item(items):
    return random.choice(items)
