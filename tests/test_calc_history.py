'''Calculator History Test'''

import pytest
from calculations.calcHistory import CalcHistory
from calculations.calculationClass import Calculation
from calculations.operations import add, multiply

@pytest.fixture
def setup_calc_history():
    '''Setup for Pytest by adding two calculations'''
    CalcHistory.add_calculation(Calculation(4,5,add))
    CalcHistory.add_calculation(Calculation(1,3,multiply))

def test_adding_to_list(setup_calc_history):
    '''Testing addition to list'''
    num = Calculation(3,3,multiply)
    CalcHistory.add_calculation(num)
    assert CalcHistory.get_latest() == num

def test_clear_list(setup_calc_history):
    '''Testing clearing list'''
    CalcHistory.clear_history()
    assert len(CalcHistory.get_history()) == 0

def test_get_history(setup_calc_history):
    '''Testing length of history'''
    assert len(CalcHistory.get_history()) == 2

def test_get_latest(setup_calc_history):
    '''Testing getting latest from list''' 
    first = CalcHistory.get_latest()
    assert first.a == 1 and first.b == 3

def test_latest_but_nothing(setup_calc_history):
    '''Testing if history is cleared nothing comes back when latest is called'''
    CalcHistory.clear_history()
    assert CalcHistory.get_latest() is None
