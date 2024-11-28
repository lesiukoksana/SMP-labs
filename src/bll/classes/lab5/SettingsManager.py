import os
import time
import json
from math import sin, cos
from abc import ABC, abstractmethod
from colorama import Fore, init as colorama_init

# Initialize colorama
colorama_init(autoreset=True)


class SettingsManager:
    """Singleton class for managing settings."""
    _instance = None

    def __new__(cls, file_path):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.file_path = file_path
            cls._instance.settings = {}
        return cls._instance

    def load_settings(self):
        """Load settings from a JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                self.settings = json.load(file)
        except FileNotFoundError:
            self.settings = self.default_settings()

    def save_settings(self):
        """Save settings to a JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump(self.settings, file)

    @staticmethod
    def default_settings():
        """Default settings."""
        return {
            'cube_width': 20,
            'scale': 40,
            'color': '\x1b[39m',
            'angles': {'A': 0, 'B': 0, 'C': 0},
            'screen': {'width': 80, 'height': 24},
            'horizontal_offset': 0,
            'distance_from_viewer': 100,
            'increment_speed': 1,
        }