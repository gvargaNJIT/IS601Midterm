#Exit Plug-In

import logging
import sys
from app.commands import Command, Data
import pandas as pd
import numpy as np

csv1_file = './data/calc_history.csv'
csv2_file = './data/gpt_calc_history.csv'

class ExitCommand(Command):
    def execute(self):
        Data.kill_it(self)
        df = pd.read_csv(csv1_file)
        df2 = pd.read_csv(csv2_file)
        if not df.empty:
            data_from_csv1 = Data.load_data_from_csv1(csv1_file)
            df_to_save = pd.DataFrame(data_from_csv1)  
            Data.save_data_to_gpt(df_to_save, csv2_file)
            data_from_csv1 = Data.load_data_from_csv1(csv1_file)
        else:
            df2['Calculation History'] = None
            df2.to_csv(csv2_file, index=False)
        logging.info("Exiting Calculator")
        sys.exit("~Exiting Calculator~")