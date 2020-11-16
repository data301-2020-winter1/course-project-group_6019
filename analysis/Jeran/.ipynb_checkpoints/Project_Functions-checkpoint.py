import numpy as np
import pandas as pd


def load_data():
    
    data = pd.read_csv("../../data/raw/madden21_ratings.csv")
    return data
    
    
def basics(data):
    print(data.head())
    print(data.shape)
    print(data.columns)
    
    
    