from abc import ABC, abstractmethod

class ASCIIArtGenerator(ABC):
    @abstractmethod
    def generate_art(self, text: str) -> str:
        pass

    @abstractmethod
    def save_to_file(self, art: str, file_name: str) -> None:
        pass

    @abstractmethod
    def preview_art(self, art: str) -> None:
        pass
