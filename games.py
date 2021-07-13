import sqlite3
names = ['Modern.pgn', 'FourKnights.pgn', 'QG-Chigorin.pgn', 'SicilianNajdorf6Bc4.pgn', 'GiuocoPiano.pgn',\
         'London2g6.pgn', 'RuyLopezOther3.pgn', 'KIDClassical.pgn', 'QG-Albin.pgn',\
         'ThreeKnights.pgn']


lists = []
for name in names:
    print(name)
    f = open("pgn/"+name, "r")
    data = f.read()
    list = data.split("\n\n")
    lists.append(list)

games = []
for list in lists:
    for ind,item in enumerate(list):
        if(ind % 2 == 0) and (ind+1 < len(list)):
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
        id = white_player+","+black_player+","+date
        # print(id, white_player, black_player, white_elo, black_elo, moves, result, event, date, site, round, eco)
        games_dict[id] = [id, white_player, black_player, white_elo, black_elo, moves, result, event, date, site, round, eco]

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
    if not white_elo or not black_elo:
        continue
    white_elo = int(white_elo)
    black_elo = int(black_elo)
    if white_elo < 2500 or black_elo < 2500:
        continue
    moves = games_dict.get(i)[5]
    result = games_dict.get(i)[6]

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
    games_list.append([id, white_player, black_player, white_elo, black_elo, moves, result, event, date, site, round, eco])

print(len(games_list))
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
    c.execute('INSERT INTO games VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',games_list[i])

conn.commit()
print("done!")