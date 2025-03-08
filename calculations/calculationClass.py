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