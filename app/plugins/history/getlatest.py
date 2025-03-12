# Get Latest History PlugIn

import logging
from app.commands import Command, Data
from calculations.calcHistory import CalcHistory

class LatestCommand(Command):
    def execute(self):
        Data.kill_it(self)
        latest = CalcHistory.get_latest()
        logging.info(f"Latest Operation is {latest}")
        print(latest)
