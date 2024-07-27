
# NiaFaker

NiaFaker is a Python package that generates fake data localized for African contexts. It can generate names, emails, phone numbers, addresses, cities, and countries. 

## Installation

To install NiaFaker, use pip:

```bash
pip install niafaker
```

## Usage

Here's how to use NiaFaker to generate various types of fake data:

### Generate a Random Name

```python
import niafaker

name = niafaker.generate_name()
print(name)
```

### Generate a Random Email

```python
import niafaker

email = niafaker.generate_email()
print(email)
```

### Generate a Random Phone Number

```python
import niafaker

phone_number = niafaker.generate_phone_number()
print(phone_number)
```

### Generate a Random Address

```python
import niafaker

address = niafaker.generate_address()
print(address)
```

### Generate a Random Address for a Specific Country and City

```python
import niafaker

address = niafaker.generate_address('Kenya', 'Nairobi')
print(address)
```

### Generate a Random City

```python
import niafaker

city = niafaker.generate_city()
print(city)
```

### Generate a Random City for a Specific Country

```python
import niafaker

city = niafaker.generate_city('Nigeria')
print(city)
```

### Generate a Random Country

```python
import niafaker

country = niafaker.generate_country()
print(country)
```
### Running Tests
To run the tests for NiaFaker, use the following command:

```bash python -m unittest discover tests ```
#### - Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

#### - License
This project is licensed under the MIT License. See the `LICENSE` file for details.
## Author

Owden Godson (OG) - [africahomeforever@gmail.com](mailto:africahomeforever@gmail.com)
