
# NiaFaker

NiaFaker is a Python package that generates fake data localized for African regions. It provides realistic names, cities, and addresses from various African countries, making it useful for testing and development purposes.

## Installation

To install NiaFaker, clone the repository and install it using pip:

\`\`\`bash
git clone https://github.com/owgee/niafaker.git
cd niafaker
pip install .
\`\`\`

## Usage

Here are some examples of how to use NiaFaker in your Python projects:

### Generate a Random Name

\`\`\`python
from niafaker import generate_name

# Generate a random name
print(generate_name())

# Generate a random male name
print(generate_name('male'))

# Generate a random female name
print(generate_name('female'))
\`\`\`

### Generate a Random Last Name

\`\`\`python
from niafaker import generate_last_name

# Generate a random last name
print(generate_last_name())
\`\`\`

### Generate a Random City

\`\`\`python
from niafaker import generate_city

# Generate a random city
print(generate_city())

# Generate a random city in Nigeria
print(generate_city('Nigeria'))
\`\`\`

### Generate a Random Address

\`\`\`python
from niafaker import generate_address

# Generate a random address
print(generate_address())

# Generate a random address in Nigeria
print(generate_address('Nigeria'))

# Generate a random address in Lagos, Nigeria
print(generate_address('Nigeria', 'Lagos'))
\`\`\`

## Running Tests

To run the tests for NiaFaker, use the following command:

\`\`\`bash
python -m unittest discover tests
\`\`\`

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the \`LICENSE\` file for details.

## Author

OG - [africahomeforever@gmail.com](mailto:africahomeforever@gmail.com)
