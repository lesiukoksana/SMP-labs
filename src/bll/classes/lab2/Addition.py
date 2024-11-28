from src.bll.classes.lab2.Operation import Operation

class Addition(Operation):
    """Performs addition."""

    def execute(self, a: float, b: float) -> float:
        return a + b