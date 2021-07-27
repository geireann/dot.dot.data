import sqlite3
import random
from difflib import SequenceMatcher
import unicodedata
import numpy as np
import pandas as pd
import operator
from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from  sklearn import tree

conn = sqlite3.connect('data.db')
c = conn.cursor()

dfgames = pd.read_sql_query("select * from merge;", conn)

def getWhiteAge(id):
	game = dfgames.loc[id == dfgames['id'],'date'].item()
	birth = dfgames.loc[id == dfgames['id'],'white_born'].item()
	if type(game) is int:
		g_year = game
	else:
		g_year = game.split('.')[0]

	if type(birth) is int:
		b_year = birth
	else:
		b_year = birth.split('.')[0]
	age = (int(g_year) - int(b_year))
	return age

def getBlackAge(id):
	game = dfgames.loc[id == dfgames['id'],'date'].item()
	birth = dfgames.loc[id == dfgames['id'],'black_born'].item()
	if type(game) is int:
		g_year = game
	else:
		g_year = game.split('.')[0]

	if type(birth) is int:
		b_year = birth
	else:
		b_year = birth.split('.')[0]
	age = (int(g_year) - int(b_year))
	return age

def getWhiteGM(id):
	gm_year = int(dfgames.loc[id == dfgames['id'],'white_year'].item())
	birth = dfgames.loc[id == dfgames['id'],'white_born'].item()
	if type(gm_year) is int:
		gm_year = gm_year
	else:
		gm_year = gm_year.split('.')[0]

	if type(birth) is int:
		b_year = birth
	else:
		b_year = birth.split('.')[0]
	age = (int(gm_year) - int(b_year))
	return age

def getBlackGM(id):
	gm_year = int(dfgames.loc[id == dfgames['id'],'black_year'].item())
	birth = dfgames.loc[id == dfgames['id'],'black_born'].item()
	if type(gm_year) is int:
		gm_year = gm_year
	else:
		gm_year = gm_year.split('.')[0]

	if type(birth) is int:
		b_year = birth
	else:
		b_year = birth.split('.')[0]
	age = (int(gm_year) - int(b_year))
	return age

def getBlackTime(id):
	game = dfgames.loc[id == dfgames['id'],'date'].item()
	gm_year = int(dfgames.loc[id == dfgames['id'],'black_year'].item())
	if type(gm_year) is int:
		gm_year = gm_year
	else:
		gm_year = gm_year.split('.')[0]

	if type(game) is int:
		g_year = game
	else:
		g_year = game.split('.')[0]
	time = (int(g_year) - int(gm_year))
	if (time < 0):
		time = 0
	return time

def getWhiteTime(id):
	game = dfgames.loc[id == dfgames['id'],'date'].item()
	gm_year = int(dfgames.loc[id == dfgames['id'],'white_year'].item())
	if type(gm_year) is int:
		gm_year = gm_year
	else:
		gm_year = gm_year.split('.')[0]

	if type(game) is int:
		g_year = game
	else:
		g_year = game.split('.')[0]
	time = (int(g_year) - int(gm_year))
	if (time < 0):
		time = 0
	return time


dfgames['black_age'] = dfgames['id'].apply(getBlackAge)
dfgames['white_age'] = dfgames['id'].apply(getWhiteAge)

dfgames['black_gm_age'] = dfgames['id'].apply(getBlackGM)
dfgames['white_gm_age'] = dfgames['id'].apply(getWhiteGM)

dfgames['black_time_since_gm'] = dfgames['id'].apply(getWhiteTime)
dfgames['white_time_since_gm'] = dfgames['id'].apply(getBlackTime)

c.execute('DROP TABLE IF EXISTS "games_new";')

dfgames.to_sql('games_new', con=conn)

# dfgames.to_excel('id.xlsx')

print("complete")

# # drop general
# dfgames.drop['round', 'eco', 'id1' ]
# # drop black
# dfgames.drop['black_id', 'black_birthplace', 'black_born', 'black_year']
# # drop white
# dfgames.drop['white_id', 'white_birthplace', 'white_born', 'white_year']
