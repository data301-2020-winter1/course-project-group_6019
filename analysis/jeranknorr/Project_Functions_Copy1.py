import numpy as np
import pandas as pd


def load_and_process():
    df= (
        pd.read_csv('../../data/raw/madden21_ratings.csv')
        .dropna()
    )
   
    df2= (    
            df.filter(['Team', 'Full Name', 'Overall Rating', 'Position']))
    return df2
    

def basics(data):
    print(data.head())
    print(data.shape)
    print(data.columns)
    
def load_data():
    
    data = pd.read_csv("../../data/raw/madden21_ratings.csv")
    return data
    