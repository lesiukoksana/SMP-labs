from os import name

from src.ui.lab9.LabRunner import LabRunner
from src.ui.lab9.UserInputHandler import UserInputHandler

class Runner:
    """Головний клас"""

    def __init__(self, max_lab_number=9):
        self.lab_runner = LabRunner(max_lab_number)
        self.input_handler = UserInputHandler(max_lab_number)

    def run(self):
        while (lab_number := self.input_handler.get_user_input()) is not None:
            self.lab_runner.run_lab(lab_number)

if name == "main":
    Runner().run()