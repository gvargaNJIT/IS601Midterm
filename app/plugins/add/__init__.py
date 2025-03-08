#Addition Plug_In

from app.commands import Command, NumberInput
from calculations import Calculator
from decimal import Decimal

class AddCommand(Command):
    def __init__(self):
        self.number_input = NumberInput()

    def execute(self):
        a = self.number_input.list_number(input("Number 1: "))
        if not isinstance(a, Decimal):
            return 0
        b = self.number_input.list_number(input("Number 2: "))
        if not isinstance(b, Decimal):
            return 0
        result = Calculator.add(a, b)
        print(f"The result is {result}")