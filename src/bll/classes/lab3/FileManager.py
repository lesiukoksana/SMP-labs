import os
from pyfiglet import Figlet
from colorama import Fore, init as colorama_init

# Ініціалізація Colorama
colorama_init(autoreset=True)

class FileManager:
    """Handles saving and loading ASCII art."""
    @staticmethod
    def save_art(folder_path, art):
        file_name = input("Enter a file name to save: ")
        file_path = os.path.join(folder_path, f"{file_name}.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(art)
        print(f"Art saved to {file_path}")

    @staticmethod
    def load_art(folder_path):
        file_name = input("Enter the file name to load: ")
        file_path = os.path.join(folder_path, f"{file_name}.txt")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                print(file.read())
        except FileNotFoundError:
            print(f"File {file_path} not found.")