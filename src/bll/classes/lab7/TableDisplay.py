import requests
import json
import csv
import re
import unittest
from termcolor import colored

from src.bll.classes.lab7.DisplayStrategy import DisplayStrategy

class TableDisplay(DisplayStrategy):
    def display(self, data):
        print(colored("Cat Facts Table", "blue"))
        for item in data:
            print(f"Fact: {item['fact']}")