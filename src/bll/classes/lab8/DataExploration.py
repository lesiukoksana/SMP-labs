import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

from src.bll.classes.lab8.DataProcessor import DataProcessor

warnings.filterwarnings("ignore", category=UserWarning)

class DataExploration(DataProcessor):
    def process(self):
        print("\nData Exploration:")
        print("First 5 rows:\n", self.data.head())
        print("Last 5 rows:\n", self.data.tail())
        print("Columns:\n", self.data.columns)
        print("Shape:\n", self.data.shape)
        self.get_extreme_values()

    def get_extreme_values(self):
        print("\nExtreme values of data:")
        for col in self.data.select_dtypes(include=[np.number]).columns:
            print(f"{col} - min: {self.data[col].min()}, max: {self.data[col].max()}, median: {self.data[col].median()}")