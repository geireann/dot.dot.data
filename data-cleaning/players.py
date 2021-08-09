from bs4 import BeautifulSoup
import requests
import sqlite3

### IEX TRADING API METHODS ###
IEX_TRADING_URL = "https://en.wikipedia.org/wiki/List_of_chess_grandmasters"


### YAHOO FINANCE SCRAPING
CHESS_GAMES = "https://en.wikipedia.org/wiki/List_of_chess_grandmasters"

# PART 1: Use BeautifulSoup and requests to collect data required for the assignment.

# Use requests.get to access the html from the MOST_ACTIVE_STOCKS_URL stored above
most_active_stocks = requests.get(CHESS_GAMES)
# Use BeautifulSoup to parse through the requests
soup = BeautifulSoup(most_active_stocks.content, 'html.parser')
# Use BeautifulSoup to parse through the requests
table = soup.find(id='grandmasters').find("tbody").find_all("tr")

# print(soup)
# Save data below.
player_dict={}

for row in table:
    current = row.find_all("td")
    # print(current, len(current))
    if (len(current) == 9):
        name = current[0].a.text
        id = current[1].text
        born = current[2].text
        born = born.replace('-','.')
        birthplace = current[3].text
        died = current[4].text
        died = died.replace('-','.')
        year = current[5].text
        fed = current[6].text
        sex = current[7].text
        player_dict[id] = [name, id, born, birthplace, died, year, fed, sex]


# Create connection to database
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Delete tables if they exist
c.execute('DROP TABLE IF EXISTS "grandmasters";')


# PART 3: Create tables in the database and add data to it. REMEMBER TO COMMIT

grandmasters = []
for i in player_dict:
    name = player_dict.get(i)[0]
    id = player_dict.get(i)[1]
    born = player_dict.get(i)[2]
    birthplace = player_dict.get(i)[3]
    died = player_dict.get(i)[4]
    year = player_dict.get(i)[5]
    fed = player_dict.get(i)[6]
    sex = player_dict.get(i)[7]
    grandmasters.append([id, name, born, birthplace, died, year, fed, sex])

c.execute('CREATE TABLE grandmasters(id varchar NOT NULL primary key, \
    name str NOT NULL, \
    born str NOT NULL, \
    birthplace str NOT NULL, \
    died int, \
    year int NOT NULL, \
    fed str, \
    sex str NOT NULL)')


for i in range(len(grandmasters)):
    c.execute('INSERT INTO grandmasters VALUES (?,?,?,?,?,?,?,?)',grandmasters[i])

conn.commit()