#Division Plug-In

from decimal import Decimal
import logging
from app.commands import Command, NumberInput, Data
from calculations.calcHistory import CalcHistory
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
            logging.error(f"The result is undefined. Exiting operation")
            print(f"The result is undefined")
            CalcHistory.add_calculation(f"{a} / 0 = Undefined")
            Data.write_data(self)
            return 0
        elif not isinstance(b, Decimal):
            return 0
        else:
            logging.info(f"{b} was entered as Number 2 for division operation")
            result = Calculator.divide(a, b)
            Data.write_data(self)
            logging.info(f"The result is {result}")
            print(f"The result is {result}")