import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

from src.bll.classes.lab8.DataCleaning import DataCleaning
from src.bll.classes.lab8.DataExploration import DataExploration
from src.bll.classes.lab8.DataVisualization import DataVisualization

warnings.filterwarnings("ignore", category=UserWarning)

class DataProcessorFactory:
    @staticmethod
    def create_processor(processor_type, *args):
        if processor_type == "exploration":
            return DataExploration(*args)
        elif processor_type == "cleaning":
            return DataCleaning(*args)
        elif processor_type == "visualization":
            return DataVisualization(*args)
        else:
            raise ValueError("Unknown processor type")