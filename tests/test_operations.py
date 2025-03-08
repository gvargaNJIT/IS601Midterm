'''Operations Test'''

from calculations.operations import add, subtract, multiply, divide

def test_add():
    '''Testing addition on operations'''
    assert add(2.0,7.0) == 9.0

def test_subtract():
    '''Testing subtraction on operations'''
    assert subtract(9.0,2.0) == 7.0

def test_multiply():
    '''Testing multiplication on operations'''
    assert multiply(5.0,6.0) == 30.0

def test_divide():
    '''Testing division on operations'''
    assert divide(4.0,4.0) == 1.0
