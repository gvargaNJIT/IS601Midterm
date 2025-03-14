'''Faker Python Test'''

from decimal import Decimal
from faker import Faker
from calculations.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    '''Having strings match operations in a set'''
    operation_mappings = {
        'add' : add,
        'subtract' : subtract,
        'multiply' : multiply,
        'divide': divide
    }

    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements = list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        if operation_func is divide:
            b = Decimal('1') if b == Decimal('0') else b
        try:
            if operation_func is divide and b == Decimal('0'):
                expected = "Undefined"
            else:
                expected = operation_func(a,b)
        except ZeroDivisionError:
            expected = "Undefined"
        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    '''Setting text instructions of when a faker test is generated with pytest'''
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    '''Setting parameters for the faker pytest'''
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
