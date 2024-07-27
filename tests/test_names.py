import unittest
from niafaker.generators.names import get_name, get_last_name

class TestNames(unittest.TestCase):
    def test_get_name(self):
        self.assertIsInstance(get_name(), str)
        self.assertIsInstance(get_name('male'), str)
        self.assertIsInstance(get_name('female'), str)
    
    def test_get_last_name(self):
        self.assertIsInstance(get_last_name(), str)

if __name__ == '__main__':
    unittest.main()
