import os

from src.bll.classes.lab3.AsciiArtGenerator import AsciiArtGenerator
from src.bll.classes.lab3.AsciiArtSettings import AsciiArtSettings
from src.bll.classes.lab3.FileManager import FileManager
from src.bll.classes.lab3.SettingsManager import SettingsManager
from src.bll.shared.menu import Menu

class ArtMenu(Menu):
    """Main menu for the ASCII art generator."""
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.settings = AsciiArtSettings()
        self.generator = AsciiArtGenerator(self.settings)

    def display_menu(self):
        print("\nASCII Art Generator Menu:")
        print("1. Create ASCII Art")
        print("2. Change Settings")
        print("3. Save Art")
        print("4. Load Art")
        print("5. Quit")

    def handle_choice(self, choice):
        match choice:
            case "1":
                self.create_ascii_art()
            case "2":
                self.change_settings()
            case "3":
                self.save_art()
            case "4":
                self.load_art()
            case "5":
                print("Exiting...")
                return False
            case _:
                print("Invalid choice. Please try again.")
        return True

    def create_ascii_art(self):
        phrase = input("Enter a phrase: ")
        try:
            art = self.generator.generate_art(phrase)
            print("\nGenerated ASCII Art:")
            print(art)
        except ValueError as e:
            print(f"Error: {e}")

    def change_settings(self):
        print("\nChange Settings:")
        self.settings.font = SettingsManager.select_font()
        self.settings.size = SettingsManager.set_size()
        self.settings.symbols = SettingsManager.set_symbols()
        self.settings.color = SettingsManager.set_color()
        print("Settings updated.")

    def save_art(self):
        art = self.generator.generate_art(input("Enter a phrase for saving: "))
        FileManager.save_art(self.folder_path, art)

    def load_art(self):
        FileManager.load_art(self.folder_path)


def main():
    """Entry point for the application."""
    folder_path = "./ascii_art/"
    os.makedirs(folder_path, exist_ok=True)

    menu = Menu(folder_path)
    running = True

    while running:
        menu.display_menu()
        user_choice = input("Choose an option: ")
        running = menu.handle_choice(user_choice)


if __name__ == "__main__":
    main()