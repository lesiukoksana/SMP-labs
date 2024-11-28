import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

from src.bll.classes.lab8.DataProcessor import DataProcessor

warnings.filterwarnings("ignore", category=UserWarning)

class DataVisualization(DataProcessor):
    def process(self):
        print("\nData Visualization:")
        self.plot_pairplot()
        self.plot_heatmap()

    def plot_pairplot(self):
        sns.pairplot(self.data)
        self.save_plot(plt, f"{self.csv_file_name}_pairplot")

    def plot_heatmap(self):
        numeric_df = self.data.select_dtypes(include=[np.number])
        if not numeric_df.empty:
            plt.figure(figsize=(10, 8))
            sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
            plt.title("Correlation Heatmap")
            self.save_plot(plt, f"{self.csv_file_name}_heatmap")