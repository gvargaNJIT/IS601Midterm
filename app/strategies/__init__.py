from abc import ABC, abstractmethod

class MenuStrategy(ABC):
    @abstractmethod
    def display(self):
        pass

class MenuContext:
    def __init__(self, strategy: MenuStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: MenuStrategy):
        self.strategy = strategy

    def show_menu(self):
        self.strategy.display()

class MainMenuStrategy(MenuStrategy):
    def display(self):
        print("Here are the options this program has:\n")
        print("add - Starts addition operation\n")
        print("subtract - Starts subtraction operation\n")
        print("divide - Starts division operation\n")
        print("multiply - Starts multiplication operation\n")
        print("history - Manage calculator history\n")
        print("exit - Exits program\n")
        print("menu - Shows options in this program\n")

class HistoryMenuStrategy(MenuStrategy):
    def display(self):
        print(f"Welcome to the calculator history menu! Type one of the options from below:\n")
        print("view history - Shows calculator history\n")
        print("get latest - Shows last operation saved to the history\n")
        print("delete history - Deletes all calculator history that was recorded\n")
        print("back - Returns to calculator program\n")