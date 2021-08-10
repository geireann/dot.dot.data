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

age_median = df_age.median()
age_q1, age_q3 = np.percentile(df_age, 25), np.percentile(df_age, 75)    

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


# ELO
df_elo = pd.concat([df_games['black_elo'], df_games['white_elo']])


elo_median = df_elo.median()
elo_q1, elo_q3 = np.percentile(df_elo, 25), np.percentile(df_elo, 75)    

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

gm_age_median = df_gm_age.median()
gm_age_q1, gm_age_q3 = np.percentile(df_gm_age, 25), np.percentile(df_gm_age, 75)    

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

# ELO DIFF
df_elo_diff =df_games['elo_diff']

elo_diff_median = df_elo_diff.median()
elo_diff_q1, elo_diff_q3 = np.percentile(df_elo_diff, 25), np.percentile(df_elo_diff, 75)    

print(elo_diff_q1, elo_diff_median, elo_diff_q3)

def gm_age_to_category(elo_diff):
    if elo_diff <= elo_diff_q1:
        return "q1"
    elif elo_diff > elo_diff_q1 and elo_diff <= elo_diff_median:
        return "q2"
    elif elo_diff > elo_diff_median and elo_diff <= elo_diff_q3:
        return "q3"
    elif elo_diff > elo_diff_q3:
        return "q4"

df_games['elo_diff_cat'] = df_games['elo_diff'].apply(gm_age_to_category)


# AGE DIFF
df_age_diff =df_games['age_diff']

age_diff_median = df_age_diff.median()
age_diff_q1, age_diff_q3 = np.percentile(df_age_diff, 25), np.percentile(df_age_diff, 75)    

print(age_diff_q1, age_diff_median, age_diff_q3)

def gm_age_to_category(age_diff):
    if age_diff <= age_diff_q1:
        return "q1"
    elif age_diff > age_diff_q1 and age_diff <= age_diff_median:
        return "q2"
    elif age_diff > age_diff_median and age_diff <= age_diff_q3:
        return "q3"
    elif age_diff > age_diff_q3:
        return "q4"

df_games['age_diff_cat'] = df_games['age_diff'].apply(gm_age_to_category)


# TIME SINCE GM DIFF
df_time_since_gm_dif =df_games['time_since_gm_diff']

time_since_gm_dif_median = df_time_since_gm_dif.median()
time_since_gm_dif_q1, time_since_gm_dif_q3 = np.percentile(df_time_since_gm_dif, 25), np.percentile(df_time_since_gm_dif, 75)    

print(time_since_gm_dif_q1, time_since_gm_dif_median, time_since_gm_dif_q3)

def gm_age_to_category(time_since_gm_dif):
    if time_since_gm_dif <= time_since_gm_dif_q1:
        return "q1"
    elif time_since_gm_dif > time_since_gm_dif_q1 and time_since_gm_dif <= time_since_gm_dif_median:
        return "q2"
    elif time_since_gm_dif > time_since_gm_dif_median and time_since_gm_dif <= time_since_gm_dif_q3:
        return "q3"
    elif time_since_gm_dif > time_since_gm_dif_q3:
        return "q4"

df_games['time_since_gm_diff_cat'] = df_games['time_since_gm_diff'].apply(gm_age_to_category)



c.execute('DROP TABLE IF EXISTS "games_final_cat";')
df_games.to_sql('games_final_cat', con=conn)

