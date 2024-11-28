from abc import ABC, abstractmethod
from typing import Optional
import math

class InputHandler(ABC):
    """Abstract base class for handling input."""

    @abstractmethod
    def get_numbers(self):
        pass

    @abstractmethod
    def get_operator(self):
        pass