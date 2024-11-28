from abc import ABC, abstractmethod
from typing import Optional
import math

from src.bll.classes.lab2.Operation import Operation

class SquareRoot(Operation):
    """Performs square root."""

    def execute(self, a: float, b: Optional[float] = None) -> float:
        if a < 0:
            raise ValueError("Square root of negative number is not allowed.")
        return math.sqrt(a)