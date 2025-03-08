#Division Plug-In

from decimal import Decimal
from app.commands import Command, NumberInput
from calculations import Calculator

class DivideCommand(Command):
    def __init__(self):
        self.number_input = NumberInput()

    def execute(self):
        a = self.number_input.list_number(input("Number 1: "))
        if not isinstance(a, Decimal):
            return 0
        b = self.number_input.list_number(input("Number 2: "))
        if b == 0:
            print(f"The result is undefined")
            return 0
        elif not isinstance(b, Decimal):
            return 0
        else:
            result = Calculator.divide(a, b)
            print(f"The result is {result}")