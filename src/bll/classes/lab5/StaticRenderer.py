import os
import time
import json
from math import sin, cos
from abc import ABC, abstractmethod
from colorama import Fore, init as colorama_init

from src.bll.classes.lab5.Cube import Cube
from src.bll.classes.lab5.RendererBase import RendererBase

# Initialize colorama
colorama_init(autoreset=True)

class StaticRenderer(RendererBase):
    """Renderer for static 3D shapes."""

    def render_frame(self):
        """Render a static frame."""
        self.clear_screen()
        self.initialize_arrays()
        Cube(self.settings).render(self.char_array, self.depth_array)
        self.display_frame()