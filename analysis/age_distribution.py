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

# AGE
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

def age_to_category(age):
    if age <= age_q1:
        return "q1"
    elif age > age_q1 and age <= age_median:
        return "q2"
    elif age > age_median and age <= age_q3:
        return "q3"
    elif age > age_q3:
        return "q4"

df_games['black_age_cat'] = df_games['black_age'].apply(age_to_category)
df_games['white_age_cat'] = df_games['white_age'].apply(age_to_category)

print(df_games['black_age_cat'])
print(df_games['white_age_cat'])


# ELO
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

# AGE SINCE GM
df_gm_age = pd.concat([df_games['black_gm_age'], df_games['white_gm_age']])

gm_age_count = df_gm_age.count()
gm_age_mean = df_gm_age.mean()
gm_age_median = df_gm_age.median()
gm_age_q1, gm_age_q3 = np.percentile(df_gm_age, 25), np.percentile(df_gm_age, 75)    
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

def gm_age_to_category(gm_age):
    if gm_age <= gm_age_q1:
        return "q1"
    elif gm_age > gm_age_q1 and gm_age <= gm_age_median:
        return "q2"
    elif gm_age > gm_age_median and gm_age <= gm_age_q3:
        return "q3"
    elif gm_age > gm_age_q3:
        return "q4"

df_games['black_gm_age_cat'] = df_games['black_gm_age'].apply(gm_age_to_category)
df_games['white_gm_age_cat'] = df_games['white_gm_age'].apply(gm_age_to_category)


c.execute('DROP TABLE IF EXISTS "games_final_cat";')
df_games.to_sql('games_final_cat', con=conn)