import importlib

class LabRunner:
    """Фасад для лабораторних робіт."""
    def __init__(self, max_lab_number=9):
        self.max_lab_number = max_lab_number

    def run_lab(self, lab_number):
        try:
            module_name = f"ui.lab{lab_number}.lab{lab_number}_menu"
            main_function = getattr(importlib.import_module(module_name), "main")
            if callable(main_function):
                main_function()
                print(f"Lab {lab_number} executed successfully.")
                return True
            else:
                print(f"Error: 'main' function not found in lab {lab_number}")
                return False
        except ImportError as e:
            print(f"Error importing lab {lab_number}: {e}")
            return False