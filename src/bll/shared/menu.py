from abc import ABC, abstractmethod

class Menu(ABC):
    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def handle_choice(self, choice):
        pass

    def menu(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if not self.handle_choice(choice):
                break