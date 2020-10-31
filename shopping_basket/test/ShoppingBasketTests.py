import unittest

from test.Item import Item
from test.ShoppingBasket import ShoppingBasket


class ShoppingBasketTests(unittest.TestCase):
    def test_empty_basket(self):
        basket = ShoppingBasket()
        self.assertEqual(basket.total(), 0.0)

    def test_single_item(self):
        basket = ShoppingBasket([Item(100.0, 1)])
        self.assertEqual(basket.total(), 100.0)

    def test_two_items(self):
        basket = ShoppingBasket([Item(100.0, 1), Item(200.0, 1)])
        self.assertEqual(basket.total(), 300.0)

    def test_multiple_quantity(self):
        basket = ShoppingBasket([Item(100.0, 2)])
        self.assertEqual(basket.total(), 200.0)


if __name__ == '__main__':
    unittest.main()
