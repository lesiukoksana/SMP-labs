from src.bll.classes.lab2.Operation import Operation

class Division(Operation):
    """Performs division."""

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b