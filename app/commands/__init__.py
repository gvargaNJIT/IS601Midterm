from abc import ABC, abstractmethod
from decimal import Decimal
import logging
import os
import pandas as pd

calculator_history = { }
data_dir = './data'

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

class Data:
    
    def write_data(self):
        df_states = pd.DataFrame(list(calculator_history.items()), columns=['Function', 'Result'])
        csv_file_path = os.path.join(data_dir, 'calc_history.csv')
        df_states.to_csv(csv_file_path, index=False)


    def configure_data(self):
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            logging.info(f"The directory '{data_dir}' is created")
        elif not os.access(data_dir, os.W_OK):
            logging.error(f"The directory '{data_dir}' is not writeable")
            return
        df_states = pd.DataFrame(list(calculator_history.items()), columns=['Function', 'Result'])
        csv_file_path = os.path.join(data_dir, 'calc_history.csv')
        df_states.to_csv(csv_file_path, index=False)