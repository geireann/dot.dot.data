import sqlite3
import random
from difflib import SequenceMatcher
import unicodedata
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from  sklearn import tree

conn = sqlite3.connect('../data-cleaning/data.db')
c = conn.cursor()

df_games = pd.read_sql_query("select * from games_final_cat;", conn)

df_elo = pd.concat([df_games['black_elo'], df_games['white_elo']])

elo_count = df_elo.count()
elo_mean = df_elo.mean()
elo_median = df_elo.median()
elo_q1, elo_q3 = np.percentile(df_elo, 25), np.percentile(df_elo, 75)    
elo_min = df_elo.min()
elo_max = df_elo.max()
elo_std = df_elo.std()
elo_var = df_elo.var()

print("Elo Distribution Stats")
print("Count:", elo_count)
print("Mean:", elo_mean)
print("Min:", elo_min)
print("Max:", elo_max)
print("Q1:", elo_q1, "Median:", elo_median, "Q3:",  elo_q3)
print("Standard deviation:", elo_std)
print("Variance:", elo_var)

def elo_to_category(elo):
    if elo <= elo_q1:
        return "q1"
    elif elo > elo_q1 and elo <= elo_median:
        return "q2"
    elif elo > elo_median and elo <= elo_q3:
        return "q3"
    elif elo > elo_q3:
        return "q4"

df_games['black_elo_cat'] = df_games['black_elo'].apply(elo_to_category)
df_games['white_elo_cat'] = df_games['white_elo'].apply(elo_to_category)