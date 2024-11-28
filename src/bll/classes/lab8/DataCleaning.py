import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

from src.bll.classes.lab8.DataProcessor import DataProcessor

warnings.filterwarnings("ignore", category=UserWarning)

class DataCleaning(DataProcessor):
    def process(self):
        print("\nData Cleaning:")
        if self.data.isnull().values.any():
            print("Missing values found. Cleaning data.")
            self.data.dropna(inplace=True)
            cleaned_path = os.path.join(self.data_dir, f"{self.csv_file_name}_cleaned.csv")
            self.data.to_csv(cleaned_path, index=False)
            print(f"Cleaned data saved to {cleaned_path}")
        else:
            print("No missing values found. Cleaning not required.")