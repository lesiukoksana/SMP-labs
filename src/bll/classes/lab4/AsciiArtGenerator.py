from colorama import init as colorama_init
from src.bll.classes.lab4.font8x8 import font8x8

# Initialize colorama
colorama_init(autoreset=True)

SPACE = 0
SYMBOL = 1
SHADOW = 2


class AsciiArtGenerator:
    """Main class for generating ASCII art."""
    def __init__(self, settings, language):
        self.settings = settings
        self.language = language
        self.font = font8x8

    def _str_to_ascii_list(self, text):
        """Convert a string to a list of ASCII or font indices."""
        return [ord(char) for char in text] if self.language == 'en' else self._map_ukr_to_font(text)

    @staticmethod
    def _map_ukr_to_font(text):
        """Map Ukrainian characters to font indices."""
        ukr_map = {'І': 0, 'і': 0, 'Д': 1, 'д': 1}
        return [ukr_map.get(char, ord(char)) for char in text]

    @staticmethod
    def _add_shadow(row):
        """Add shadow to a row by replacing spaces with shadow symbols."""
        return [SHADOW if row[i] == SYMBOL and row[i + 1] == SPACE else row[i] for i in range(len(row) - 1)] + [row[-1]]

    @staticmethod
    def _row_to_string(row, regular_symbol, shadow_symbol):
        """Convert row data to a string representation."""
        return ''.join(regular_symbol if item == SYMBOL else shadow_symbol if item == SHADOW else ' ' for item in row)

    @staticmethod
    def _align(alignment, width, row_length):
        """Calculate left padding for alignment."""
        if alignment == 'center':
            return (width - row_length) // 2
        if alignment == 'right':
            return width - row_length
        return 0

    def render(self, text):
        """Generate ASCII art for the given text."""
        char_list = self._str_to_ascii_list(text)
        width, height = self.settings.size
        lines = [char_list[i:i + width // 8] for i in range(0, len(char_list), width // 8)]
        art = ""

        for line in lines:
            for row_index in range(8):
                row = []
                for char_index in line:
                    bitmap = self.font[char_index]
                    row_data = [(bitmap[row_index] >> bit) & 1 for bit in range(8)]
                    if self.settings.is_3d:
                        row_data = [SPACE] * row_index + row_data
                    if self.settings.symbols[1]:
                        row_data = self._add_shadow(row_data)
                    row.extend(row_data)
                row_str = self._row_to_string(row, *self.settings.symbols)
                padding = self._align(self.settings.alignment, width, len(row_str))
                art += ' ' * padding + row_str + '\n'
        return self.settings.color + art