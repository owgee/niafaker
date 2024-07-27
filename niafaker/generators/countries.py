import json
import pkg_resources
import random

def load_data(filename):
    resource_path = pkg_resources.resource_filename(__name__, f'../data/{filename}')
    with open(resource_path, 'r') as file:
        return json.load(file)

data = load_data('countries.json')['countries']

def generate_country():
    return generate_item([country['name'] for country in data])

def generate_item(items):
    return random.choice(items)
