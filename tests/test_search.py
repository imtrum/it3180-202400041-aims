import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearchByTitle(unittest.TestCase):

    def setUp(self):
        self.dvds = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Spider-Man", "Action"),
        ]

    def test_search_case_insensitive(self):
        result = search_by_title(self.dvds, "lion")
        self.assertEqual([dvd.title for dvd in result], ["The Lion King"])

    def test_search_no_match(self):
        result = search_by_title(self.dvds, "avatar")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()