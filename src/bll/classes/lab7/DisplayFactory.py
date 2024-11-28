from src.bll.classes.lab7.TableDisplay import TableDisplay
from src.bll.classes.lab7.ListDisplay import ListDisplay

class DisplayFactory:
    def get_display_strategy(self, strategy_type):
        if strategy_type == "table":
            return TableDisplay()
        elif strategy_type == "list":
            return ListDisplay()
        else:
            raise ValueError("Invalid display strategy")