
# NiaFaker

NiaFaker is a Python package that generates fake data localized for African contexts. It can generate names, emails, phone numbers, addresses, cities, and countries. 

## Installation

To install NiaFaker, use pip:

\`\`\`bash
pip install .
\`\`\`

## Usage

Here's how to use NiaFaker to generate various types of fake data:

### Generate a Random Name

\`\`\`python
import niafaker

name = niafaker.generate_name()
print(name)
\`\`\`

### Generate a Random Email

\`\`\`python
import niafaker

email = niafaker.generate_email()
print(email)
\`\`\`

### Generate a Random Phone Number

\`\`\`python
import niafaker

phone_number = niafaker.generate_phone_number()
print(phone_number)
\`\`\`

### Generate a Random Address

\`\`\`python
import niafaker

address = niafaker.generate_address()
print(address)
\`\`\`

### Generate a Random Address for a Specific Country and City

\`\`\`python
import niafaker

address = niafaker.generate_address('Kenya', 'Nairobi')
print(address)
\`\`\`

### Generate a Random City

\`\`\`python
import niafaker

city = niafaker.generate_city()
print(city)
\`\`\`

### Generate a Random City for a Specific Country

\`\`\`python
import niafaker

city = niafaker.generate_city('Nigeria')
print(city)
\`\`\`

### Generate a Random Country

\`\`\`python
import niafaker

country = niafaker.generate_country()
print(country)
\`\`\`

## Running Tests

To run the tests, use the following command:

\`\`\`bash
python -m unittest discover -s tests
\`\`\`

## Example Data

Ensure your JSON data files (`addresses.json` and `countries.json`) have the required data. For example:

### `countries.json`

\`\`\`json
{
  "countries": [
    {
      "name": "Tanzania",
      "cities": ["Arusha", "Dar es Salaam", "Tanga"]
    },
    {
      "name": "Nigeria",
      "cities": ["Lagos", "Abuja", "Kano"]
    }
  ]
}
\`\`\`

### `addresses.json`

\`\`\`json
{
  "addresses": {
    "Kenya": {
      "Nairobi": ["123 Nairobi St, Nairobi", "456 Central Ave, Nairobi"],
      "Mombasa": ["789 Beach Rd, Mombasa"],
      "Kisumu": ["101 Lake View, Kisumu"]
    },
    "Nigeria": {
      "Lagos": ["123 Lagos Blvd, Lagos", "456 Market St, Lagos"],
      "Abuja": ["789 Capital Rd, Abuja"],
      "Kano": ["101 Desert Dr, Kano"]
    }
  }
}
\`\`\`

## Author


Owden Godson (OG) - [africahomeforever@gmail.com](mailto:africahomeforever@gmail.com)
