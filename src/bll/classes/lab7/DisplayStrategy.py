import requests
import json
import csv
import re
import unittest
from termcolor import colored

# Strategy Pattern
class DisplayStrategy:
    def display(self, data):
        raise NotImplementedError("Subclasses should implement this method")

class ListDisplay(DisplayStrategy):
    def display(self, data):
        print(colored("Cat Facts List", "green"))
        for item in data:
            print(f"{item['fact']}")
