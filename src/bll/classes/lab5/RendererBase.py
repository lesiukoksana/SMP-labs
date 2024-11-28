import os
import time
import json
from math import sin, cos
from abc import ABC, abstractmethod
from colorama import Fore, init as colorama_init

# Initialize colorama
colorama_init(autoreset=True)

class RendererBase(ABC):
    """Abstract base class for renderers."""

    def __init__(self, settings):
        self.settings = settings
        self.width = settings['screen']['width']
        self.height = settings['screen']['height']
        self.char_array = [' '] * (self.width * self.height)
        self.depth_array = [0] * (self.width * self.height)

    @abstractmethod
    def render_frame(self):
        """Render a single frame."""
        pass

    def clear_screen(self):
        """Clear terminal screen."""
        os.system('clear')

    def display_frame(self):
        """Display the rendered frame on the screen."""
        print("\033[H", end="")
        for idx, char in enumerate(self.char_array):
            if idx % self.width == 0:
                print()
            print(self.settings['color'] + char, end="")

    def initialize_arrays(self):
        """Reset character and depth arrays."""
        self.char_array = [' '] * (self.width * self.height)
        self.depth_array = [0] * (self.width * self.height)