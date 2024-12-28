import pandas as pd
import numpy as np
import os
import sys

def cleaning_data(data):
    #Performing data cleaning
    data.dropna()
    return data
