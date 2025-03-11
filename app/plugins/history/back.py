#Back Plugin

import logging
from app.commands import Command

class BackCommand(Command):
    def execute(self):
        logging.info(f"Went back to main calculator")
        print("Welcome to the Calculator! Enter an operation or type 'exit' to leave the program")