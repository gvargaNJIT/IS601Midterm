# View History PlugIn

import logging
from app.commands import Command
from calculations.calcHistory import CalcHistory

class ViewCommand(Command):
    def execute(self):
        logging.info(f"Calculator History has been listed")
        for item in CalcHistory.history:
            print(item)