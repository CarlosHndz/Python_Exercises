import unittest
from city_functions import get_formatted_name

class TestCityNames(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does city names like 'Santiago, Chile' work?"""
        formatted_name = get_formatted_name('santiago', 'chile')
        self.assertEqual(formatted_name, "Santiago, Chile")

    def test_city_country_population(self):
        """Does city, country, and population like "Santiago, Chile - Population 5000000" work?"""
        formatted_name = get_formatted_name('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, "Santiago, Chile - Population 5000000")

unittest.main()
