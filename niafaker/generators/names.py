import json
import random

def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

data = load_data('niafaker/data/names.json')

def get_name(gender=None):
    if gender == 'male':
        return random.choice(data['male_first_names'])
    elif gender == 'female':
        return random.choice(data['female_first_names'])
    else:
        return random.choice(data['male_first_names'] + data['female_first_names'])

def get_last_name():
    return random.choice(data['last_names'])
