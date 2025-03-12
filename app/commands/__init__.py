from abc import ABC, abstractmethod
from decimal import Decimal
from calculations.calcHistory import CalcHistory
import logging
import os
import pandas as pd
from dotenv import load_dotenv
import csv

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
        filename = os.path.basename(command.__module__)
        filename_without_extension = os.path.splitext(filename)[-1]
        filename_clean = filename_without_extension.lstrip('.')
        logging.info(f"Command '{command_name}' from plugin '{filename_clean}' registered.")
    
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

    def __init__(self):
        load_dotenv()
        self.env_data = self.load_env_data()

    def load_env_data(self):
        return {
            'CSV_PATH': os.getenv('CSV_PATH'),
        }

    def write_data(self):
        with open(os.path.join(data_dir, 'calc_history.csv'), mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Calculation History'])
            writer.writerows([[item] for item in CalcHistory.history])
        logging.info("Data saved to calc_history.csv")

    def configure_data(self):
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            logging.info(f"The directory '{data_dir}' is created")
        elif not os.access(data_dir, os.W_OK):
            logging.error(f"The directory '{data_dir}' is not writable")
            return
        self.write_data()

    def load_data_into_list(self, csv2_path):
        if os.path.exists(csv2_path):
            with open(csv2_path, mode='r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
                data = [row[0] for row in csv_reader]
            env_values = [self.env_data['CSV_PATH']]
            CalcHistory.history = data + env_values
            logging.info(f"Loaded and updated data from {csv2_path} with .env values.")
        else:
            logging.error(f"{csv2_path} does not exist. Cannot load data.")
        return CalcHistory.history
    
    def save_data_to_gpt(dataframe, csv2_path):
        dataframe.to_csv(csv2_path, index=False)
        logging.info(f"Data saved to {csv2_path}")

    def load_gpt_path():
        load_dotenv() 
        return os.getenv("CSV_PATH")

    def load_data_from_gpt(csv2_path, csv1_path):
        if os.path.exists(csv2_path):
            df_csv2 = pd.read_csv(csv2_path)
            df_csv2.to_csv(csv1_path, index=False)
            logging.info(f"Data from {csv2_path} copied back to {csv1_path}")
        else:
            logging.error(f"No data in {csv2_path}, nothing copied back to {csv1_path}.")


    def load_data_from_csv1(csv1_path):
        if os.path.exists(csv1_path):
            try:
                df = pd.read_csv(csv1_path)
                if df.empty:
                    print(f"{csv1_path} is empty. Returning an empty list.")
                    return []
                return df.to_dict(orient='records')
            except pd.errors.EmptyDataError:
                print(f"{csv1_path} is empty. Returning an empty list.")
                return []
            else:
                print(f"No file found at {csv1_path}, returning an empty list.")
                return []
            
    def kill_it(self):
        csv1_file = './data/calc_history.csv'
        csv2_file = './data/gpt_calc_history.csv'
        df = pd.read_csv(csv1_file)
        df2 = pd.read_csv(csv2_file)
        df = df[~df['Calculation History'].fillna('').str.contains('/data/calc_history.csv')]
        df = df[~df['Calculation History'].fillna('').str.contains('./data/gpt_calc_history.csv')]
        df['Calculation History'] = df['Calculation History'].fillna('').astype(str)
        df = df[df['Calculation History'].str.strip() != '']
        df2['Calculation History'] = df2['Calculation History'].fillna('').astype(str)
        df2 = df2[df2['Calculation History'].str.strip() != '']
        df.to_csv(csv1_file, index=False)
        df2.to_csv(csv2_file, index=False)
        if "/data/calc_history.csv" in CalcHistory.history:
            CalcHistory.history.remove("/data/calc_history.csv")
        elif "./data/gpt_calc_history.csv" in CalcHistory.history:
            CalcHistory.history.remove("./data/gpt_calc_history.csv")
        for i in range(len(CalcHistory.history)):
            CalcHistory.history[i] = CalcHistory.history[i].strip()