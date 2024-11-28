import os
from pyfiglet import Figlet
from colorama import Fore, init as colorama_init

# Ініціалізація Colorama
colorama_init(autoreset=True)

class AsciiArtSettings:
    """Stores settings for ASCII art generation."""
    def __init__(self, font="slant", size=(80, 25), symbols=None, color=Fore.RESET):
        self.font = font
        self.size = size
        self.symbols = symbols
        self.color = color