#Back Plugin

import logging
from app.commands import Command, Data

class BackCommand(Command):
    def execute(self):
        Data.kill_it(self)
        logging.info(f"Went back to main calculator")
        print("Welcome to the Calculator! Enter an operation or type 'exit' to leave the program")