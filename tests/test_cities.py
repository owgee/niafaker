import unittest
from niafaker.generators.cities import get_city

class TestCities(unittest.TestCase):
    def test_get_city(self):
        self.assertIsInstance(get_city(), str)
        self.assertIsInstance(get_city('Nigeria'), str)

if __name__ == '__main__':
    unittest.main()
