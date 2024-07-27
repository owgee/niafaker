import unittest
from niafaker.generators.addresses import get_address

class TestAddresses(unittest.TestCase):
    def test_get_address(self):
        self.assertIsInstance(get_address(), str)
        self.assertIsInstance(get_address('Nigeria'), str)
        self.assertIsInstance(get_address('Nigeria', 'Lagos'), str)

if __name__ == '__main__':
    unittest.main()
