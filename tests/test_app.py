'''Calculator App Test'''

import pytest
from app import App

def test_app_exit(capfd, monkeypatch):
    '''Testing exiting of the app'''
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_wrong_command(capfd, monkeypatch):
    '''Testing wrong command operation of the app'''
    inputs = iter(['operationNo', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "operationNo is not a valid operation" in captured.out
