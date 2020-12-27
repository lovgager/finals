import unittest
from pizza_menu import *


class TestPizza(unittest.TestCase):

    def test_cmp1(self):
        self.assertNotEqual(Pepperoni(), Pepperoni('XL'))

    def test_cmp2(self):
        self.assertEqual(Margherita(), Margherita('L'))

    def test_cmp3(self):
        self.assertNotEqual(Hawaiian(), 123)

    def test_wrong_size(self):
        with self.assertRaises(ValueError):
            Pepperoni('XXL')

    def test_receipt(self):
        self.assertEqual(Hawaiian().dict(), {
                'tomato sauce': 111,
                'mozzarella': 123,
                'chicken': 111,
                'pineapples': 123
            })


if __name__ == '__main__':
    unittest.main()