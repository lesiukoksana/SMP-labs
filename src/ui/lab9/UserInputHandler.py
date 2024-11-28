class UserInputHandler:
    """Обробник вводу користувача."""

    def __init__(self, max_lab_number):
        self.max_lab_number = max_lab_number

    def get_user_input(self):
        while True:
            user_input = input(f"\nSelect a lab (1-{self.max_lab_number}) or 'q' to quit: ").lower()
            if user_input == 'q':
                return None
            if user_input.isdigit() and 1 <= int(user_input) <= self.max_lab_number:
                return int(user_input)
            print(f"Please enter a number between 1 and {self.max_lab_number}.")