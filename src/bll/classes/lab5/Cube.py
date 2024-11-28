import os
import time
import json
from math import sin, cos
from abc import ABC, abstractmethod
from colorama import Fore, init as colorama_init

colorama_init(autoreset=True)

class Cube:
    """Class for rendering a cube."""

    def __init__(self, settings):
        self.settings = settings
        self.width = settings['cube_width']
        self.scale = settings['scale']
        self.angles = settings['angles']
        self.distance_from_viewer = settings['distance_from_viewer']

    def render(self, char_array, depth_array):
        """Render cube surfaces."""
        for x in range(-self.width, self.width, self.width // 10):
            for y in range(-self.width, self.width, self.width // 10):
                self._draw_surface(x, y, -self.width, '@', char_array, depth_array)
                self._draw_surface(self.width, y, x, '$', char_array, depth_array)

    def _draw_surface(self, x, y, z, char, char_array, depth_array):
        """Calculate and render a single surface."""
        x_proj, y_proj, depth = self._project(x, y, z)
        screen_x = int(self.settings['screen']['width'] // 2 + self.scale * depth * x_proj)
        screen_y = int(self.settings['screen']['height'] // 2 + self.scale * depth * y_proj)
        idx = screen_x + screen_y * self.settings['screen']['width']
        if 0 <= idx < len(char_array) and depth > depth_array[idx]:
            char_array[idx] = char
            depth_array[idx] = depth

    def _project(self, x, y, z):
        """Project 3D coordinates to 2D."""
        A, B, C = self.angles['A'], self.angles['B'], self.angles['C']
        z_proj = z + self.distance_from_viewer
        x_proj = x * cos(B) + z * sin(B)
        y_proj = y * cos(A) - z * sin(A)
        return x_proj, y_proj, 1 / z_proj

    def update_angles(self):
        """Update rotation angles."""
        self.angles['A'] += 0.05
        self.angles['B'] += 0.05
        self.angles['C'] += 0.01