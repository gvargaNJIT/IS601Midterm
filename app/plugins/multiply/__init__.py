#Multiplication Plug_In

import logging
from app.commands import Command, NumberInput, Data
from calculations import Calculator
from decimal import Decimal

class MultiplyCommand(Command):
    def __init__(self):
        self.number_input = NumberInput()

    def execute(self):
        a = self.number_input.list_number(input("Number 1: "))
        if not isinstance(a, Decimal):
            return 0
        else:
            logging.info(f"{a} was entered as Number 1 for multiplication operation")
        b = self.number_input.list_number(input("Number 2: "))
        if not isinstance(b, Decimal):
            return 0
        else:
            logging.info(f"{b} was entered as Number 2 for multiplication operation")
        result = Calculator.multiply(a, b)
        Data.write_data(self)
        logging.info(f"The result is {result}")
        print(f"The result is {result}")