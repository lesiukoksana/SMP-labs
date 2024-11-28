from abc import ABC, abstractmethod
from typing import Optional
import math

from src.bll.classes.lab2.Operation import Operation

class Remainder(Operation):
    """Performs remainder (modulus)."""

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a % b