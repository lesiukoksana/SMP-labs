import requests
import json
import csv
import re
import unittest
from termcolor import colored

from src.bll.classes.lab7.APIClient import APIClient
from src.bll.classes.lab7.HistoryLogger import HistoryLogger
from src.bll.classes.lab7.DisplayFactory import DisplayFactory

class Application:
    def __init__(self):
        self.api_client = APIClient()
        self.history_logger = HistoryLogger()

    def fetch_and_display_data(self, strategy_type):
        try:
            data = self.api_client.fetch_data()
            display_strategy = DisplayFactory().get_display_strategy(strategy_type)
            display_strategy.display(data)
            self.history_logger.log_query("fetch_and_display_data", data)
        except Exception as e:
            print(f"Error: {e}")

    def save_data(self, data, format_type):
        try:
            if format_type == 'json':
                with open('data.json', 'w') as f:
                    json.dump(data, f, indent=4)
            elif format_type == 'csv':
                with open('data.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Fact'])
                    for item in data:
                        writer.writerow([item['fact']])
            elif format_type == 'txt':
                with open('data.txt', 'w') as f:
                    for item in data:
                        f.write(f"{item['fact']}\n")
            print(f"Data saved to {format_type.upper()} format.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def show_history(self):
        self.history_logger.show_history()

    def parse_input(input_str, pattern):
        match = re.match(pattern, input_str)
        if match:
            return match.groups()
        else:
            return None

    def validate_input(self, prompt, pattern):
        user_input = input(prompt)
        while not self.parse_input(user_input, pattern):
            print("Invalid input. Please try again.")
            user_input = input(prompt)
        return user_input


if __name__ == '__main__':
    app = Application()