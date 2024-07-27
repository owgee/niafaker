import json
import pkg_resources
import random

def load_data(filename):
    resource_path = pkg_resources.resource_filename(__name__, f'../data/{filename}')
    with open(resource_path, 'r') as file:
        return json.load(file)

data = load_data('names.json')

def generate_name(gender=None):
    if gender == 'male':
        first_name = generate_item(data['male_first_names'])
    elif gender == 'female':
        first_name = generate_item(data['female_first_names'])
    else:
        first_name = generate_item(data['male_first_names'] + data['female_first_names'])
    last_name = generate_last_name()
    return f"{first_name} {last_name}"

def generate_last_name():
    return generate_item(data['last_names'])

def generate_email():
    first_name = random.choice(data['male_first_names'] + data['female_first_names'])
    last_name = random.choice(data['last_names'])
    domain = random.choice(['example.com', 'email.com', 'mail.com', 'test.com'])
    email = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 100)}@{domain}"
    return email

def generate_phone_number():
    return generate_item(data['phone_numbers'])

def generate_item(items):
    return random.choice(items)
