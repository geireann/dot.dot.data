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

df_age = pd.concat([df_games['black_age'], df_games['white_age']])

age_count = df_age.count()
age_mean = df_age.mean()
age_median = df_age.median()
age_q1, age_q3 = np.percentile(df_age, 25), np.percentile(df_age, 75)    
age_min = df_age.min()
age_max = df_age.max()
age_std = df_age.std()
age_var = df_age.var()

print("Age Distribution Stats")
print("Count:", age_count)
print("Mean:", age_mean)
print("Min:", age_min)
print("Max:", age_max)
print("Q1:", age_q1, "Median:", age_median, "Q3:",  age_q3)
print("Standard deviation:", age_std)
print("Variance:", age_var)