import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestDiscount(unittest.TestCase):

    def test_discount(self):
        cart1 = Cart(80)

        cart1.add_dvd(DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 20))
        cart1.add_dvd(DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 20))
        cart1.add_dvd(DigitalVideoDisc("Aladdin", "Animation", cost=60))

        print(f"Total cost: {cart1.total_cost():.2f} $")

        self.assertTrue(cart1.total_cost() == 80)

        with self.assertRaises(ValueError) as context:
            Cart(150)


if __name__ == "__main__":
    unittest.main()