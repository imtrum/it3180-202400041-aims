
import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCartSorting(unittest.TestCase):

    def setUp(self):
        """Create a cart with sample DVDs before each test."""
        self.cart = Cart()

        self.dvd1 = DigitalVideoDisc(
            "The Lion King", "Animation", "Roger Allers", 87, 19.95
        )
        self.dvd2 = DigitalVideoDisc(
            "Aladdin", "Animation", "Ron Clements", 90, 18.99
        )
        self.dvd3 = DigitalVideoDisc(
            "Star Wars", "Science Fiction", "George Lucas", 121, 24.95
        )

        self.cart.add_dvd(self.dvd1)
        self.cart.add_dvd(self.dvd2)
        self.cart.add_dvd(self.dvd3)

    def test_sort_by_title(self):
        self.cart.sort_by_title()

        expected = ["Aladdin", "Star Wars", "The Lion King"]
        actual = [dvd.title for dvd in self.cart.items]

        self.assertEqual(actual, expected)

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()

        expected = [18.99, 19.95, 24.95]
        actual = [dvd.cost for dvd in self.cart.items]

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
