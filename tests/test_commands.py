'''Command Testing Operations'''

from decimal import Decimal
import pytest
from app import App
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

def test_addition_command(capfd, monkeypatch):
    '''Testing addition command'''
    num1 = 10
    num2 = 12
    answers = iter([Decimal(num1), Decimal(num2)])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    command = AddCommand()
    command.execute()
    captured = capfd.readouterr()
    assert "The result is 22" in captured.out

def test_subtraction_command(capfd, monkeypatch):
    '''Testing subtraction command'''
    num1 = 33
    num2 = 19
    answers = iter([Decimal(num1), Decimal(num2)])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    command = SubtractCommand()
    command.execute()
    captured = capfd.readouterr()
    assert "The result is 14" in captured.out

def test_multiplication_command(capfd, monkeypatch):
    '''Testing multiplication command'''
    num1 = 3
    num2 = 9
    answers = iter([Decimal(num1), Decimal(num2)])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    command = MultiplyCommand()
    command.execute()
    captured = capfd.readouterr()
    assert "The result is 27" in captured.out

def test_division_command(capfd, monkeypatch):
    '''Testing division command'''
    num1 = 42
    num2 = 7
    answers = iter([Decimal(num1), Decimal(num2)])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    command = DivideCommand()
    command.execute()
    captured = capfd.readouterr()
    assert "The result is 6" in captured.out

def test_addition_app(capfd, monkeypatch):
    '''Testing the app's addition command'''
    operation = 'add'
    num1 = 11
    num2 = 2
    answers = iter([operation, Decimal(num1), Decimal(num2), 'exit'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "The result is 13" in captured.out

def test_subtraction_app(capfd, monkeypatch):
    '''Testing the app's subtraction command'''
    operation = 'subtract'
    num1 = 2.5
    num2 = 1
    answers = iter([operation, Decimal(num1), Decimal(num2), 'exit'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "The result is 1.5" in captured.out

def test_multiplication_app(capfd, monkeypatch):
    '''Testing the app's multiplication command'''
    operation = 'multiply'
    num1 = 4
    num2 = 1.5
    answers = iter([operation, Decimal(num1), Decimal(num2), 'exit'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "The result is 6" in captured.out

def test_division_app(capfd, monkeypatch):
    '''Testing the app's division command'''
    operation = 'divide'
    num1 = 22
    num2 = 2
    answers = iter([operation, Decimal(num1), Decimal(num2), 'exit'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "The result is 11" in captured.out

def test_division_error_app(capfd, monkeypatch):
    '''Testing dividing by zero'''
    operation = 'divide'
    num1 = 3
    num2 = 0
    answers = iter([operation, Decimal(num1), Decimal(num2), 'exit'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "The result is undefined" in captured.out

def test_number_one_error(capfd, monkeypatch):
    '''Testing first number error'''
    operation = 'multiply'
    num1 = 'a'
    answers = iter([operation, num1, 'exit'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "a is not a valid number" in captured.out

def test_number_two_error(capfd, monkeypatch):
    '''Testing second number error'''
    operation = 'subtract'
    num1 = 3
    num2 = 's'
    answers = iter([operation, Decimal(num1), num2, 'exit'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "s is not a valid number" in captured.out

def test_menu(capfd, monkeypatch):
    '''Testing Menu Command'''
    command = 'menu'
    answers = iter([command, 'exit'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "Here are the options this program has:" in captured.out

def test_back(capfd, monkeypatch):
    '''Testing Back Command'''
    command = 'back'
    answers = iter([command, 'exit'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "Welcome to the Calculator! Enter an operation or type 'exit' to leave the program" in captured.out

def test_history(capfd, monkeypatch):
    '''Testing History Command'''
    command = 'history'
    answers = iter([command, 'exit'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "Welcome to the calculator history menu! Type one of the options from below:" in captured.out

def test_viewhistory(capfd, monkeypatch):
    '''Testing View History Command'''
    command = 'view history'
    answers = iter(['delete history', 'add','2','2',command, 'exit'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "2 + 2 = 4" in captured.out

def test_getlatest(capfd, monkeypatch):
    '''Testing Get Latest Command'''
    command = 'get latest'
    answers = iter(['delete history', 'multiply','3','4',command, 'exit'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "3 * 4 = 12" in captured.out

def test_deletehistory(capfd, monkeypatch):
    '''Testing Delete History Command'''
    command = 'delete history'
    answers = iter(['add','2','2',command, 'view history','exit'])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "" in captured.out
