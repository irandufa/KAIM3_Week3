import pandas as pd
import numpy as np
import os
import sys

def load_dataset(file_path):
    """
    Function to load a dataset from a given file path.
    """
    try:
        df = pd.read_csv(file_path, sep="|", low_memory=False)
        print("Dataset loaded successfully!")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        