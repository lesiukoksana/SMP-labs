from abc import ABC, abstractmethod
from typing import Optional
import math

from src.bll.classes.lab2.Operation import Operation

class Multiplication(Operation):
    """Performs multiplication."""

    def execute(self, a: float, b: float) -> float:
        return a * b