import logging

from src.bll.shared.menu import Menu

class CalculatorMenu(Menu):
    """Menu for interacting with the calculator."""

    def __init__(self, calculator, history_manager):
        self.calculator = calculator
        self.history_manager = history_manager

        # Налаштування логування
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def display_menu(self):
        self.logger.info("Displaying menu options.")
        print("\nOptions:")
        print("1. Perform calculation")
        print("2. View history")
        print("3. Clear history")
        print("4. Quit")

    def handle_choice(self, choice):
        self.logger.info(f"User selected option: {choice}")
        match choice:
            case '1':
                self.perform_calculation()
            case '2':
                self.view_history()
            case '3':
                self.clear_history()
            case '4':
                self.logger.info("Exiting the menu.")
                print("Exiting...")
                return False
            case _:
                self.logger.warning("Invalid choice made by the user.")
                print("Invalid choice. Please select a valid option (1/2/3/4).")
        return True

    def perform_calculation(self):
        """Perform a calculation using the calculator."""
        try:
            self.logger.info("Performing calculation.")
            result = self.calculator.calculate()
            self.logger.info(f"Calculation successful: {result}")
            print("Calculation complete:", result)
        except Exception as e:
            self.logger.error(f"An error occurred during calculation: {e}")
            print(f"An error occurred during calculation: {e}")

    def view_history(self):
        """Display the calculation history."""
        self.logger.info("Displaying calculation history.")
        print("Calculation History:")
        self.history_manager.display_history()

    def clear_history(self):
        """Clear the calculation history."""
        self.logger.info("Clearing calculation history.")
        self.history_manager.clear_history()
        print("History cleared.")
