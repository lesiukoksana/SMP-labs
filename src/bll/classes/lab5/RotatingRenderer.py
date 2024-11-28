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

class RotatingRenderer(RendererBase):
    """Renderer for rotating 3D shapes."""

    def render_frame(self):
        """Render continuously rotating frames."""
        cube = Cube(self.settings)
        while True:
            self.clear_screen()
            self.initialize_arrays()
            cube.render(self.char_array, self.depth_array)
            self.display_frame()
            cube.update_angles()
            time.sleep(0.05)