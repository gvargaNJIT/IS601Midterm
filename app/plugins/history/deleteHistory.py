# Deletion History PlugIn

import logging
from app.commands import Command, Data
from calculations.calcHistory import CalcHistory

class DeleteCommand(Command):
    def execute(self):
        CalcHistory.clear_history()
        Data.write_data(self)
        logging.info(f"Cleared calculator history")