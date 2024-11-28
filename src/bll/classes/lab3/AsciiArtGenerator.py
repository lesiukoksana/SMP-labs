import os
from pyfiglet import Figlet
from colorama import Fore, init as colorama_init

# Ініціалізація Colorama
colorama_init(autoreset=True)

class AsciiArtGenerator:
    """Generates ASCII art based on user-defined settings."""
    def __init__(self, settings):
        self.settings = settings

    def generate_art(self, phrase):
        """Generate ASCII art with current settings."""
        art_engine = Figlet(font=self.settings.font, width=self.settings.size[0])
        art = art_engine.renderText(phrase)

        if self.settings.symbols:
            art = self._replace_symbols(art, self.settings.symbols[0])

        return self.settings.color + art

    @staticmethod
    def _replace_symbols(art, symbol):
        """Replace non-whitespace characters in the ASCII art with a symbol."""
        return ''.join(symbol if char not in ('\n', ' ') else char for char in art)
