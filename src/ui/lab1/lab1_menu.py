from src.bll.shared import menu

class MyMenu(menu):
    def display_menu(self):
        print("\nOptions:")
        print("1. Perform calculation")
        print("2. View history")
        print("3. Quit")

    def handle_choice(self, choice):
        match choice:
            case '1':
                self.calculator()
            case '2':
                self.viewHistory()
            case '3':
                print("Exiting...")
                return False
            case _:
                print("Invalid choice. Please select a valid option (1/2/3).")
        return True
