import sqlite3
import pandas as pd

conn = sqlite3.connect('data.db')
c = conn.cursor()

dfgames = pd.read_sql_query("select * from merge;", conn)




