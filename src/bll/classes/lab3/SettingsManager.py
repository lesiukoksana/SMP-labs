import os
from pyfiglet import Figlet
from colorama import Fore, init as colorama_init

# Ініціалізація Colorama
colorama_init(autoreset=True)

class SettingsManager:
    """Manages user interaction for configuring ASCII art settings."""
    @staticmethod
    def select_font():
        fonts = Figlet().getFonts()
        print("\nAvailable fonts:")
        for idx, font in enumerate(fonts, 1):
            print(f"{idx}. {font}")
        choice = int(input("Choose a font number: ")) - 1
        return fonts[choice]

    @staticmethod
    def set_size():
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        return width, height

    @staticmethod
    def set_symbols():
        regular_symbol = input("Enter the replacement symbol: ")
        shadow_symbol = input("Enter the shadow symbol (optional): ") or None
        return regular_symbol, shadow_symbol

    @staticmethod
    def set_color():
        print("\nAvailable colors:")
        for idx, color in enumerate(Fore.__dict__.keys(), 1):
            print(f"{idx}. {color}")
        choice = int(input("Choose a color number: ")) - 1
        color_name = list(Fore.__dict__.keys())[choice]
        return Fore.__dict__[color_name]