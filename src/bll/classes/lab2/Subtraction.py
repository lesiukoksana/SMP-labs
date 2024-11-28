from src.bll.classes.lab2.Operation import Operation

class Subtraction(Operation):
    """Performs subtraction."""

    def execute(self, a: float, b: float) -> float:
        return a - b