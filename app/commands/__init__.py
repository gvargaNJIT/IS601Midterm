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
        # Load environment variables when the Data class is instantiated
        load_dotenv()
        self.env_data = self.load_env_data()

    def load_env_data(self):
        """Load the necessary data from the .env file."""
        return {
            'CSV_PATH': os.getenv('CSV_PATH'),
        }

    def write_data(self):
        """Write the data in CalcHistory.history to a CSV file with only one column."""
        # Write the history data to calc_history.csv (single column)
        with open(os.path.join(data_dir, 'calc_history.csv'), mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Calculation History'])  # Header
            writer.writerows([[item] for item in CalcHistory.history])  # Write each item as a row
        logging.info("Data saved to calc_history.csv")

    def configure_data(self):
        """Ensure the data directory exists and write initial data if necessary."""
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            logging.info(f"The directory '{data_dir}' is created")
        elif not os.access(data_dir, os.W_OK):
            logging.error(f"The directory '{data_dir}' is not writable")
            return
        
        # Initialize calc_history.csv if it's empty
        self.write_data()

    def load_data_into_list(self, csv2_path):
        """Load data from the second CSV file into CalcHistory.history and add .env values."""
        if os.path.exists(csv2_path):
            with open(csv2_path, mode='r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip the header row
                data = [row[0] for row in csv_reader]  # Extract only the calculation history column

            # Add the .env values to the data as a new row for each value
            env_values = [self.env_data['CSV_PATH']]
            CalcHistory.history = data + env_values  # Append the .env values to the history
            
            logging.info(f"Loaded and updated data from {csv2_path} with .env values.")
        else:
            logging.error(f"{csv2_path} does not exist. Cannot load data.")
        
        return CalcHistory.history
    
    def save_data_to_gpt(dataframe, csv2_path):
        dataframe.to_csv(csv2_path, index=False)
        logging.info(f"Data saved to {csv2_path}")

    # Function to load csv-2 path from the .env file
    def load_gpt_path():
        load_dotenv()  # Load environment variables from .env
        return os.getenv("CSV_PATH")

# Function to load data from csv-2 into csv-1 (when program restarts)
    def load_data_from_gpt(csv2_path, csv1_path):
        if os.path.exists(csv2_path):
            df_csv2 = pd.read_csv(csv2_path)
            # Copy the data back to csv-1 (This assumes you want to overwrite csv-1 with csv-2 data)
            df_csv2.to_csv(csv1_path, index=False)
            logging.info(f"Data from {csv2_path} copied back to {csv1_path}")
        else:
            logging.error(f"No data in {csv2_path}, nothing copied back to {csv1_path}.")


# Function to load data from csv-1 into a list (to be used by your program)
    def load_data_from_csv1(csv1_path):
        if os.path.exists(csv1_path):
            try:
                df = pd.read_csv(csv1_path)
                if df.empty:
                    print(f"{csv1_path} is empty. Returning an empty list.")
                    return []  # Return empty list if CSV is empty
                return df.to_dict(orient='records')  # Convert to list of dicts
            except pd.errors.EmptyDataError:
                print(f"{csv1_path} is empty. Returning an empty list.")
                return []  # Return an empty list if the file is empty
            else:
                print(f"No file found at {csv1_path}, returning an empty list.")
                return []  # Return an empty list if the file doesn't exist
            
    def kill_it(self):
        csv1_file = './data/calc_history.csv'
        df = pd.read_csv(csv1_file)
        df = df[~df['Calculation History'].str.contains('/data/calc_history.csv')]
        df = df[~df['Calculation History'].str.contains('./data/gpt_calc_history.csv')]
        df.to_csv(csv1_file, index=False)
        if "/data/calc_history.csv" in CalcHistory.history:
            CalcHistory.history.remove("/data/calc_history.csv")
        elif "./data/gpt_calc_history.csv" in CalcHistory.history:
            CalcHistory.history.remove("./data/gpt_calc_history.csv")