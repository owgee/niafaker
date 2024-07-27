import unittest
import niafaker

class TestNiaFaker(unittest.TestCase):

    def test_generate_name(self):
        name = niafaker.generate_name()
        self.assertIsInstance(name, str)
        self.assertGreater(len(name.split()), 1)  # Ensure it contains both first and last name

    def test_generate_email(self):
        email = niafaker.generate_email()
        self.assertIsInstance(email, str)
        self.assertIn('@', email)
        self.assertIn('.', email.split('@')[1])

    def test_generate_phone_number(self):
        phone_number = niafaker.generate_phone_number()
        self.assertIsInstance(phone_number, str)
        self.assertTrue(phone_number.startswith('+'))
        self.assertGreater(len(phone_number), 8)  # Ensure it's a reasonably long phone number

    def test_generate_address(self):
        address = niafaker.generate_address()
        self.assertIsInstance(address, str)
        self.assertGreater(len(address), 5)  # Ensure it's a reasonably long address

    def test_generate_address_with_country_and_city(self):
        address = niafaker.generate_address('Kenya', 'Nairobi')
        self.assertIsInstance(address, str)
        self.assertGreater(len(address), 5)  # Ensure it's a reasonably long address

    def test_generate_city(self):
        city = niafaker.generate_city()
        self.assertIsInstance(city, str)
        self.assertGreater(len(city), 2)  # Ensure it's a reasonably long city name

    def test_generate_city_with_country(self):
        city = niafaker.generate_city('Nigeria')
        self.assertIsInstance(city, str)
        self.assertGreater(len(city), 2)  # Ensure it's a reasonably long city name

    def test_generate_country(self):
        country = niafaker.generate_country()
        self.assertIsInstance(country, str)
        self.assertGreater(len(country), 2)  # Ensure it's a reasonably long country name

if __name__ == '__main__':
    unittest.main()
