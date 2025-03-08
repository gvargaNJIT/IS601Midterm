#Calculator History

from typing import List
from calculations.calculationClass import Calculation


class CalcHistory:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history

    @classmethod
    def clear_history(cls):
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        if cls.history:
            return cls.history[-1]
        return None
    