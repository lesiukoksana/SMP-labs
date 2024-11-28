import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

class DataProcessor:
    def __init__(self, csv_file, plot_dir, data_dir):
        if not os.path.isfile(csv_file):
            raise FileNotFoundError(f"CSV file '{csv_file}' does not exist.")
        self.data = pd.read_csv(csv_file)
        self.csv_file_name = os.path.splitext(os.path.basename(csv_file))[0]
        self.plot_dir = plot_dir
        self.data_dir = data_dir

    def process(self):
        raise NotImplementedError("Subclasses should implement this!")

    def save_plot(self, plt, filename):
        path = os.path.join(self.plot_dir, f"{filename}.png")
        plt.savefig(path, bbox_inches='tight')
        plt.close()
        print(f"Saved plot to {path}")