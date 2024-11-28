from typing import Optional

from src.bll.classes.lab2.Addition import Addition
from src.bll.classes.lab2.Division import Division
from src.bll.classes.lab2.Multiplication import Multiplication
from src.bll.classes.lab2.Power import Power
from src.bll.classes.lab2.Remainder import Remainder
from src.bll.classes.lab2.SquareRoot import SquareRoot
from src.bll.classes.lab2.Subtraction import Subtraction


class Calculator:
    """Singleton Calculator class for performing operations."""

    _instance = None

    OPERATIONS = {
        '+': Addition(),
        '-': Subtraction(),
        '*': Multiplication(),
        '/': Division(),
        '^': Power(),
        '√': SquareRoot(),
        '%': Remainder(),
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calculate(self, a: float, operator: str, b: Optional[float] = None) -> float:
        """Performs calculation based on the operator."""
        operation = self.OPERATIONS.get(operator)
        if not operation:
            raise ValueError(f"Invalid operator: {operator}")
        return operation.execute(a, b)