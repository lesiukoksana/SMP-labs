import requests
import json
import csv
import re
import unittest
from termcolor import colored

# Singleton Pattern
class APIClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(APIClient, cls).__new__(cls, *args, **kwargs)
            cls._instance.api_url = 'https://catfact.ninja/facts'
        return cls._instance

    def fetch_data(self):
        if not self.api_url:
            raise ValueError("API URL is not configured")

        try:
            response = requests.get(self.api_url)
            if response.status_code == 200:
                return response.json()['data']
            else:
                raise Exception(f"Failed to fetch data: {response.status_code}")
        except Exception as e:
            raise Exception(f"Error fetching data: {e}")
