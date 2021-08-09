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

df_games = pd.read_sql_query("select * from games_new;", conn)

df_gm_age = pd.concat([df_games['black_gm_age'], df_games['white_gm_age']])

gm_age_count = df_gm_age.count()
gm_age_mean = df_gm_age.mean()
gm_age_median = df_gm_age.median()
gm_age_q1, age_q3 = np.percentile(df_gm_age, 25), np.percentile(df_gm_age, 75)    
gm_age_min = df_gm_age.min()
gm_age_max = df_gm_age.max()
gm_age_std = df_gm_age.std()
gm_age_var = df_gm_age.var()

print("Grandmaster Age Distribution Stats")
print("Count:", gm_age_count)
print("Mean:", gm_age_mean)
print("Min:", gm_age_min)
print("Max:", gm_age_max)
print("Q1:", gm_age_q1, "Median:", gm_age_median, "Q3:",  age_q3)
print("Standard deviation:", gm_age_std)
print("Variance:", gm_age_var)