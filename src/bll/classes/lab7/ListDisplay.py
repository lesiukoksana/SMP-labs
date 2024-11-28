import requests
import json
import csv
import re
import unittest
from termcolor import colored

from src.bll.classes.lab7.DisplayStrategy import DisplayStrategy

class ListDisplay(DisplayStrategy):
    def display(self, data):
        print(colored("Cat Facts List", "green"))
        for item in data:
            print(f"{item['fact']}")