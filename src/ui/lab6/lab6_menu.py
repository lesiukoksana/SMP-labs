import unittest

from src.bll.classes.lab6.test_calculator import UnitTestCalculator
from src.bll.shared.menu import Menu

class TestMenu(Menu):
    def display_menu(self):
        print("\n=== Test Menu ===")
        print("1. Run all tests")
        print("0. Exit")

    def handle_choice(self, choice):
        match choice:
            case '1':
                self.run_tests()
            case '0':
                print("Exiting...")
                return False
            case _:
                print("Invalid choice! Please try again.")
        return True


    def run_tests(self, test_name=None):
        loader = unittest.TestLoader()
        if test_name:
            suite = loader.loadTestsFromName(test_name)
        else:
            suite = loader.loadTestsFromTestCase(TestCalculator)

        runner = unittest.TextTestRunner()
        print("\nRunning tests...\n")
        runner.run(suite)

if __name__ == "__main__":
    test_menu = TestMenu()
    test_menu.menu()