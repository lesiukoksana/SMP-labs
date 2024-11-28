import unittest

from src.bll.classes.lab7.APIClient import APIClient
from src.bll.classes.lab7.Application import Application

class TestAPIIntegration(unittest.TestCase):
    def test_fetch_data(self):
        api_client = APIClient()
        data = api_client.fetch_data()
        self.assertTrue(isinstance(data, list))
        self.assertTrue('fact' in data[0])

    def test_invalid_input(self):
        app = Application()
        result = app.validate_input("Enter a date (YYYY-MM-DD): ", r"\d{4}-\d{2}-\d{2}")
        self.assertIsNotNone(result)


if __name__ == '__main__':
    app = Application()

    # Displaying data in table format
    app.fetch_and_display_data('table')

    # Saving data in JSON format
    app.save_data([{'fact': "Cats sleep for 70% of their lives."}], 'json')

    # Showing query history
    app.show_history()

    # Running Unit Tests
    unittest.main()