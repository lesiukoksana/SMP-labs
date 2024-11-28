class AsciiArtSettings:
    """Class to store settings for ASCII art generation."""
    def __init__(self, color, symbols, size, alignment, is_3d):
        self.color = color
        self.symbols = symbols  # (regular_symbol, shadow_symbol)
        self.size = size  # (width, height)
        self.alignment = alignment  # 'left', 'center', 'right'
        self.is_3d = is_3d  # True or False