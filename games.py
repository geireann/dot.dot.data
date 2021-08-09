import sqlite3
import random
from difflib import SequenceMatcher
import unicodedata
import pandas as pd
import numpy as np
import operator

RANDOM_SEED = 0
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

names = ['Modern.pgn', 'FourKnights.pgn', 'QG-Chigorin.pgn', 'SicilianNajdorf6Bc4.pgn', 'GiuocoPiano.pgn', \
         'London2g6.pgn', 'RuyLopezOther3.pgn', 'KIDClassical.pgn', 'QG-Albin.pgn', \
         'ThreeKnights.pgn', 'TrompowskyOther.pgn', 'CatalanClosed.pgn', 'BenkoGambit.pgn', \
         'DutchOther.pgn']

lists = []
for name in names:
    print(name)
    f = open("pgn/" + name, "r")
    data = f.read()
    list = data.split("\n\n")
    lists.append(list)

games = []
for list in lists:
    for ind, item in enumerate(list):
        if (ind % 2 == 0) and (ind + 1 < len(list)):
            games.append([item, list[ind + 1]])

games_dict = {}
for ind, game in enumerate(games):
    info = game[0].split("\n")
    if (len(info) == 10):
        moves = game[1]
        event = info[0].split('"')[1]
        site = info[1].split('"')[1]
        date = info[2].split('"')[1]
        round = info[3].split('"')[1]
        white_player = info[4].split('"')[1]
        black_player = info[5].split('"')[1]
        result = info[6].split('"')[1]
        white_elo = info[7].split('"')[1]
        black_elo = info[8].split('"')[1]
        eco = info[9].split('"')[1]
        id = white_player + "," + black_player + "," + date
        # print(id, white_player, black_player, white_elo, black_elo, moves, result, event, date, site, round, eco)
        games_dict[id] = [id, white_player, black_player, white_elo, black_elo, moves, result, event, date, site, round,
                          eco]

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS "games";')

games_list = []
for i in games_dict:
    id = games_dict.get(i)[0]
    white_player = games_dict.get(i)[1]
    black_player = games_dict.get(i)[2]
    white_elo = games_dict.get(i)[3]
    black_elo = games_dict.get(i)[4]
    # dont include game with elo less than 2500
    if not white_elo or not black_elo:
        continue
    white_elo = int(white_elo)
    black_elo = int(black_elo)
    if white_elo < 2500 or black_elo < 2500:
        continue
    moves = games_dict.get(i)[5]
    result = games_dict.get(i)[6]

    # 1 --> White won, -1 --> Black won, 0 --> Draw
    if not result:
        continue
    if result == '1-0':
        result = 1
    elif result == '0-1':
        result = -1
    elif result == '1/2-1/2':
        result = 0

    event = games_dict.get(i)[7]
    date = games_dict.get(i)[8]
    if "??" in date:
        continue
    site = games_dict.get(i)[9]
    round = games_dict.get(i)[10]
    eco = games_dict.get(i)[11]
    games_list.append(
        [id, white_player, black_player, white_elo, black_elo, moves, result, event, date, site, round, eco])

c.execute('CREATE TABLE games( \
    id varchar NOT NULL primary key, \
    white_player str NOT NULL, \
    black_player str NOT NULL, \
    white_elo int NOT NULL, \
    black_elo int NOT NULL, \
    moves str NOT NULL, \
    result int NOT NULL, \
    event str, \
    date str NOT NULL, \
    site str NOT NULL, \
    round str, \
    eco str)')

for i in range(len(games_list)):
    c.execute('INSERT INTO games VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', games_list[i])

conn.commit()


def test_train_split(data, train_pct):
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)
    msk = np.random.rand(len(data)) < train_pct
    return data[msk], data[~msk]

def clean(text):
    #strip away the accent
    '''
    text = ''.join(char for char in \
                   unicodedata.normalize('NFKD', text) if unicodedata.category(char) != 'Mn')
    '''
    text = text.replace(', ', ' ')
    text = text.replace(',', ' ')
    text = text.replace('.', '')
    text = text.split(' ')
    if len(text) >= 2:
        text = text[0] + '.' + (text[-1])[0]
    else:
        text = text[0] + '.'
    return text

dfgames = pd.read_sql_query("select * from games;", conn)
dfplayers = pd.read_sql_query("select * from grandmasters;", conn)
#dfplayers['name'] = dfplayers['name'].apply(clean)
#dfgames['black_player'] = dfgames['black_player'].apply(clean)
#dfgames['white_player'] = dfgames['white_player'].apply(clean)

# test, train = test_train_split(df, 0.8)

dic = {}
dplayers = dfplayers['name'].to_numpy()
for players in dplayers:
    if players not in dic:
        id = dfplayers.loc[dfplayers['name'] == players, 'id'].to_numpy()
        if len(id) == 1:
            dic[players] = id
        else:
            dic[players] = 0

#print(len(dic))

correct = {}
total = {}
incorrect = []
count = 0
wh = dfgames['white_player'].to_numpy()
for w in wh:
    total[w] = '#'
    # print(w)
    if w in dic:
        total[w] = dic[w]
        correct[w] = dic[w]

bl = dfgames['black_player'].to_numpy()
for b in bl:
    total[b] = '#'
    # print(b)
    if b in dic:
        total[b] = dic[b]
        correct[b] = dic[b]

maxes = []
print(len(correct))
print(len(total))

for names in total:
    similarity = {}
    if names not in dic:
        for n in dic:
            num = SequenceMatcher(None, n, names).ratio()
            if num >= 0.8:
                similarity[names + '##' + n] = num
        try:
            m = max(similarity.items(), key=operator.itemgetter(1))[0]
            namea, nameb = m.split('##')
            total[namea] = dic[nameb]
            maxes.append(m)
        except:
            total[names] = 0
            continue

def set_FIDE_ID(names):
    if names in total:
        return int(total[names])
    else:
        return 0

dfgames['black_fide_id'] = dfgames['black_player'].apply(set_FIDE_ID)
dfgames['white_fide_id'] = dfgames['white_player'].apply(set_FIDE_ID)

c.execute('DROP TABLE IF EXISTS "games_id";')

dfgames.to_sql('games_id', con=conn)

# dfgames.to_excel('id.xlsx')

print(f'total ={len(total)}')
print(f'dic ={len(dic)}')
print(f'count = {count}')

#ML positional analysis






'''
for names in total:
    similarity = {}
    if total[names] == '#':
        for n in dic:
            num = SequenceMatcher(None, n, names).ratio()
            if num >= 0.8:
                similarity[names + "#" + n] = num
    try:
        m = max(similarity.items(), key=operator.itemgetter(1))[0]
        namea, nameb = m.split('#')
        total[nameb] = dic[namea]
        maxes.append(m)
    except:
        continue



for ele in maxes:
    namea, nameb = ele.split('#')
    print(f'{namea} -- {nameb}\n')
'''
'''
for v in total:
    if v not in correct:
        incorrect.append(v)

maxes = []

for names in total:
    similarity = {}
    for n in dic:
        if n != names:
            num = SequenceMatcher(None, n, names).ratio()
            if num >= 0.7:
                similarity[names + "#" + n + "->index " + str(num)] = num
    try:
        m = max(similarity.items(), key=operator.itemgetter(1))[0]
        maxes.append(m)
    except:
        continue

names = []
for ele in maxes:
    namea, nameb = ele.split('#')
    print(f'{namea} -- {nameb}\n')
'''