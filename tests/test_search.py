import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title, search_by_category


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.dvds = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Spider-Man", "Action"),
            DigitalVideoDisc("Finding Nemo", "Animation"),
        ]

    def test_search_by_title(self):
        result = search_by_title(self.dvds, "lion")

        self.assertEqual(
            [dvd.title for dvd in result],
            ["The Lion King"]
        )

    def test_search_by_category(self):
        result = search_by_category(self.dvds, "animation")

        self.assertEqual(
            [dvd.title for dvd in result],
            ["The Lion King", "Finding Nemo"]
        )


if __name__ == "__main__":
    unittest.main()