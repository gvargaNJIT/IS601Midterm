# Deletion History PlugIn

import logging
from app.commands import Command
from calculations.calcHistory import CalcHistory

class DeleteCommand(Command):
    def execute(self):
        CalcHistory.clear_history()
        logging.info(f"Cleared calculator history")