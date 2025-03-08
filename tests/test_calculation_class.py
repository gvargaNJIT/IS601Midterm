'''Calculation Definition Test'''

from decimal import Decimal
import pytest
from calculations.calculationClass import Calculation
from calculations.operations import divide


def test_calculations():
    '''Testing calculations'''
    test = Calculation(2, 4, divide)
    assert test.get_result() == 0.5

def test_undefined():
    '''Testing dividing by zero'''
    division_zero = Calculation(Decimal('3'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Undefined"):
        division_zero.get_result()
