class HistoryManager:
    """Manages calculation history."""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def save_history(self, operation: str, result: float):
        """Save operation and result to file."""
        with open(self.file_path, 'a') as file:
            file.write(f"{operation} = {result}\n")

    def load_history(self):
        """Load history from file."""
        try:
            with open(self.file_path, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            return []

    def clear_history(self):
        """Clear history file."""
        open(self.file_path, 'w').close()