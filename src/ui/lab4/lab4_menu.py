from src.bll.classes.lab3.AsciiArtGenerator import AsciiArtGenerator
from src.bll.classes.lab3.AsciiArtSettings import AsciiArtSettings
from src.bll.shared.ascii_utils import check_size, preview_art
from src.bll.shared.user_input_utils import get_phrase


class Menu:
    """Class to manage user interaction."""
    @staticmethod
    def show_menu(folder_path):
        """Display menu and handle user input."""
        print("Welcome to ASCII Art Generator!")
        language = input("Choose language (en - English, ukr - Ukrainian): ").strip().lower()
        settings = AsciiArtSettings(
            color="\033[31m",  # Example red color
            symbols=('#', '*'),
            size=(80, 16),
            alignment='center',
            is_3d=True
        )
        generator = AsciiArtGenerator(settings, language)
        while True:
            try:
                text = get_phrase()
                check_size(text, *settings.size)
                art = generator.render(text)
                preview_art(folder_path, art)
            except ValueError as err:
                print(f"Error: {err}")
            else:
                break

if __name__ == "__main__":
    FOLDER_PATH = "output_folder"
    Menu.show_menu(FOLDER_PATH)