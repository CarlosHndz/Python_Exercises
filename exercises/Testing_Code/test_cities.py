import unittest
from city_functions import get_formatted_name

class TestCityNames(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_names(self):
        """Does city names like 'Santiago, Chile' work?"""
        formatted_name = get_formatted_name('santiago', 'chile')
        self.assertEqual(formatted_name, "Santiago, Chile")

unittest.main()
