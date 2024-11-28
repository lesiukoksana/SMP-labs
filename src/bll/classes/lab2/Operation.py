from abc import ABC, abstractmethod
from typing import Optional
import math

class Operation(ABC):
    """Abstract base class for mathematical operations."""

    @abstractmethod
    def execute(self, a: float, b: Optional[float] = None) -> float:
        pass