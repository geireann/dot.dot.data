import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute(
    'SELECT games.id, games.black_player, games.white_player, games.black_elo, games.white_elo \
    FROM games WHERE games.black_elo > 2500 \
    AND games.white_elo > 2500 \
    ORDER BY games.white_elo, games.black_elo ASC'
)

conn.commit()

c.execute('DROP TABLE IF EXISTS "merge";')

c.execute(
    'INSERT INTO merge SELECT * FROM (\
        SELECT * \
        FROM grandmasters \
        LEFT JOIN games \
        ON games.white_player = grandmasters.name \
        UNION ALL \
        SELECT * \
        FROM grandmasters \
        LEFT JOIN games \
        ON games.black_player = grandmasters.name \
    )'
)

conn.commit()


