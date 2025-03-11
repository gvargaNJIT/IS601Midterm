'''Calculator History Test'''

import pytest
from calculations.calcHistory import CalcHistory

@pytest.fixture
def setup_calc_history():
    '''Setup for Pytest by adding two calculations'''
    CalcHistory.add_calculation("3 - 3 = 0")
    CalcHistory.add_calculation("2 * 8 = 16")

def test_adding_to_list(setup_calc_history):
    '''Testing addition to list'''
    num = "2 + 2 = 4"
    CalcHistory.add_calculation(num)
    assert CalcHistory.get_latest() == num

def test_clear_list(setup_calc_history):
    '''Testing clearing list'''
    CalcHistory.clear_history()
    assert len(CalcHistory.history) == 0

def test_get_latest(setup_calc_history):
    '''Testing getting latest from list''' 
    first = CalcHistory.get_latest()
    assert first == "2 * 8 = 16"

def test_latest_but_nothing(setup_calc_history):
    '''Testing if history is cleared nothing comes back when latest is called'''
    CalcHistory.clear_history()
    assert CalcHistory.get_latest() is None
