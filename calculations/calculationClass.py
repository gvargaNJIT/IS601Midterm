#Calculation Class

from decimal import Decimal
from typing import Callable



class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation

    def get_result(self):
        return self.operation(self.a, self.b)
        
    def __str__(self):
        operation_map = {
            'add': '+',
            'subtract': '-',
            'multiply': '*',
            'divide': '/',
        }

        result = self.get_result()
        operation_symbol = operation_map.get(self.operation.__name__, self.operation.__name__)
        return f"{self.a} {operation_symbol} {self.b} = {result}"
