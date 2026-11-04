import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):

    def test_dvd_limit(self):
        cart = Cart()

        for i in range(19):
            cart.items.append(i)

        dvd = DigitalVideoDisc(
            "Star Wars", "Science Fiction", "George Lucas", 87, 24.95
        )

        self.assertFalse(cart.add_dvd(dvd))


if __name__ == "__main__":
    unittest.main()