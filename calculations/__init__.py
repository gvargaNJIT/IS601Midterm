#Operation Definitions/Classes

from calculations.calculationClass import Calculation
from calculations.operations import add, subtract, multiply, divide
from calculations.calcHistory import CalcHistory
from decimal import Decimal
from typing import Callable

class Calculator:

    @staticmethod
    def performOperation(a: Decimal, b: Decimal, operation: Callable [[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation(a, b, operation)
        CalcHistory.add_calculation(calculation)
        return calculation.get_result()

    @staticmethod
    def add(a,b):
        return Calculator.performOperation(a, b, add)
    
    @staticmethod
    def subtract(a,b):
        return Calculator.performOperation(a, b, subtract)
    
    @staticmethod
    def multiply(a,b):
        return Calculator.performOperation(a, b, multiply)
    
    @staticmethod
    def divide(a,b):
        return Calculator.performOperation(a, b, divide)