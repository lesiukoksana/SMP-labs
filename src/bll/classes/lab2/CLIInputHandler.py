from abc import ABC, abstractmethod
from typing import Optional
import math

from src.bll.classes.lab2.InputHandler import InputHandler

class CLIInputHandler(InputHandler):
    """Handles input from the command line interface."""

    VALID_OPERATORS = ['+', '-', '*', '/', '^', '√', '%']

    def get_numbers(self):
        """Get numbers from user."""
        try:
            a = float(input("Enter the first number: "))
            b = None
            operator = self.get_operator()
            if operator not in ('√',):
                b = float(input("Enter the second number: "))
            return a, operator, b
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return self.get_numbers()

    def get_operator(self):
        """Get operator from user."""
        operator = input(f"Enter an operator ({', '.join(self.VALID_OPERATORS)}): ")
        if operator not in self.VALID_OPERATORS:
            print("Invalid operator. Please try again.")
            return self.get_operator()
        return operator