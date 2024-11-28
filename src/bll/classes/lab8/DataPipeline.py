import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

from src.bll.classes.lab8.DataProcessorFactory import DataProcessorFactory

warnings.filterwarnings("ignore", category=UserWarning)

class DataPipeline:
    def __init__(self, csv_file, plot_dir, data_dir):
        self.csv_file = csv_file
        self.plot_dir = plot_dir
        self.data_dir = data_dir

    def run_pipeline(self):
        for processor_type in ["exploration", "cleaning", "visualization"]:
            processor = DataProcessorFactory.create_processor(processor_type, self.csv_file, self.plot_dir, self.data_dir)
            processor.process()