from abc import ABC, abstractmethod
from decimal import Decimal
import logging

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Commandlist:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        try:
            logging.info(f"{command_name} is operation chosen")
            self.commands[command_name].execute()
        except KeyError:
            logging.error(f"{command_name} is not a valid operation")
            print(f"{command_name} is not a valid operation")

class NumberInput:
    def __init__(self):
        self.numbers = {}
        
    def list_number(self, a: Decimal):
        try:
            return Decimal(a)
        except Exception as e:
            logging.error(f"{a} is not a valid number. Exiting operation")
            print(f"{a} is not a valid number")
            return 1
