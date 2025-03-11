# History PlugIn

from app.commands import Command

class HistoryCommand(Command):
    def execute(self):
        print(f"Welcome to the calculator history menu! Type one of the options from below:\n")
        print("view history - Shows calculator history\n")
        print("get latest - Shows last operation saved to the history\n")
        print("delete history - Deletes all calculator history that was recorded\n")
        print("back - Returns to calculator program\n")
        return 0