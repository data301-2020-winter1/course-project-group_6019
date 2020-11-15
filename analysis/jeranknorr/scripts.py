import numpy as np
import pandas as pd

def load_and_process():
    df= (
        pd.read_csv('../../data/raw/madden21_ratings.csv')
        .dropna()
    )
   
    df2= (    
            df.filter(['Team', 'Full Name', 'Overall Rating', 'Position'])
)
    return df2


def QuarterBack_Score(df):
    
    return df.loc[lambda x: x['Position'].str.contains('QB')].groupby('Team')['Overall Rating'].max().reset_index().sort_values('Overall Rating', ascending=False).reset_index(drop=True).rename(columns={'Overall Rating': 'Top Quaterback'})


def TightEnd_Score(df):
    return df.loc[lambda x: x['Position'].str.contains('TE')].groupby('Team')['Overall Rating'].max().reset_index().sort_values('Overall Rating', ascending=False).reset_index(drop=True).rename(columns={'Overall Rating': 'Top Tight End'})

def WideReceiver_Score(df):
    return df.loc[lambda x: x['Position'].str.contains('WR')].groupby('Team')['Overall Rating'].max().reset_index().sort_values('Overall Rating', ascending=False).reset_index(drop=True).rename(columns={'Overall Rating': 'Top Wide Receiver'})

def FullBack_Score(df):
    return df.loc[lambda x: x['Position'].str.contains('FB')].groupby('Team')['Overall Rating'].max().reset_index().sort_values('Overall Rating', ascending=False).reset_index(drop=True)

def HalfBack_Score(df):
    return  df.loc[lambda x: x['Position'].str.contains('WR')].groupby('Team')['Overall Rating'].max().reset_index().sort_values('Overall Rating', ascending=False).reset_index(drop=True).rename(columns={'Overall Rating': 'Top Half Back'})

def CornerBack_Score(df):
    return df.loc[lambda x: x['Position'].str.contains('CB')].groupby('Team')['Overall Rating'].max().reset_index().sort_values('Overall Rating', ascending=False).reset_index(drop=True).rename(columns={'Overall Rating': 'Top Corner Back'})

def RightOutsideLinebacker_Score(df):
    return df.loc[lambda x: x['Position'].str.contains('ROLB')].groupby('Team')['Overall Rating'].max().reset_index().sort_values('Overall Rating', ascending=False).reset_index(drop=True).rename(columns={'Overall Rating': 'Top Right Outside Linebacker'})

def LeftOutsideLinebacker_Score(df):
    return df.loc[lambda x: x['Position'].str.contains('LOLB')].groupby('Team')['Overall Rating'].max().reset_index().sort_values('Overall Rating', ascending=False).reset_index(drop=True).rename(columns={'Overall Rating': 'Top Left Outside Linebacker'})

def MiddleLinebacker_Score(df):
    return df.loc[lambda x: x['Position'].str.contains('MLB')].groupby('Team')['Overall Rating'].max().reset_index().sort_values('Overall Rating', ascending=False).reset_index(drop=True).rename(columns={'Overall Rating': 'Top Middle Linebacker'})

def FreeSafety_Score(df):
    return df.loc[lambda x: x['Position'].str.contains('FS')].groupby('Team')['Overall Rating'].max().reset_index().sort_values('Overall Rating', ascending=False).reset_index(drop=True).rename(columns={'Overall Rating': 'Top Free Safety'})

def StrongSafety_Score(df):
    return df.loc[lambda x: x['Position'].str.contains('SS')].groupby('Team')['Overall Rating'].max().reset_index().sort_values('Overall Rating', ascending=False).reset_index(drop=True).rename(columns={'Overall Rating': 'Top Strong Saftey'})

def DefensiveTackle_Score(df):
    return df.loc[lambda x: x['Position'].str.contains('DT')].groupby('Team')['Overall Rating'].max().reset_index().sort_values('Overall Rating', ascending=False).reset_index(drop=True).rename(columns={'Overall Rating': 'Top Defensive Tackle'})

def LeftEnd_Score(df):
    return  df.loc[lambda x: x['Position'].str.contains('LE')].groupby('Team')['Overall Rating'].max().reset_index().sort_values('Overall Rating', ascending=False).reset_index(drop=True).rename(columns={'Overall Rating': 'Top Defensive Left End'})

def RightEnd_Score(df):
    return df.loc[lambda x: x['Position'].str.contains('RE')].groupby('Team')['Overall Rating'].max().reset_index().sort_values('Overall Rating', ascending=False).reset_index(drop=True).rename(columns={'Overall Rating': 'Top Defensive Right End'})

def Kicker_Score(df):
    return df.loc[lambda x: x['Position'].str.contains('K')].groupby('Team')['Overall Rating'].max().reset_index().sort_values('Overall Rating', ascending=False).reset_index(drop=True).rename(columns={'Overall Rating': 'Top Kicker'})

def Punter_Score(df):
    return  df.loc[lambda x: x['Position'].str.contains('P')].groupby('Team')['Overall Rating'].max().reset_index().sort_values('Overall Rating', ascending=False).reset_index(drop=True).rename(columns={'Overall Rating': 'Top Punter'})

