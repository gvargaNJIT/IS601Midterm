#Division Plug-In

from decimal import Decimal
import logging
from app.commands import Command, NumberInput
from calculations import Calculator

class DivideCommand(Command):
    def __init__(self):
        self.number_input = NumberInput()

    def execute(self):
        a = self.number_input.list_number(input("Number 1: "))
        if not isinstance(a, Decimal):
            return 0
        else:
            logging.info(f"{a} was entered as Number 1 for division operation")
        b = self.number_input.list_number(input("Number 2: "))
        if b == 0:
            logging.error(f"The result is undefined")
            print(f"The result is undefined. Exiting operation")
            return 0
        elif not isinstance(b, Decimal):
            return 0
        else:
            logging.info(f"{b} was entered as Number 2 for division operation")
            result = Calculator.divide(a, b)
            logging.info(f"The result is {result}")
            print(f"The result is {result}")