#Menu Plug-In

from app.commands import Command

class MenuCommand(Command):
    def execute(self):
        print("Here are the options this program has:\n")
        print("add - Starts addition operation\n")
        print("subract - Starts subtraction operation\n")
        print("divide - Starts division operation\n")
        print("multiply - Starts multiplication operation\n")
        print("exit - Exits program\n")
        print("menu - Shows options in this program\n")
        return 0