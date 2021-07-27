import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute(
    'SELECT games_id.id, games_id.black_player, games_id.white_player, games_id.black_elo, games_id.white_elo \
    FROM games_id WHERE games_id.black_elo > 2500 \
    AND games_id.white_elo > 2500 \
	AND games_id.black_fide_id > 0 \
	AND games_id.white_fide_id > 0 \
    ORDER BY games_id.white_elo, games_id.black_elo ASC'
)

conn.commit()

c.execute('DROP TABLE IF EXISTS "merge";')

c.execute('CREATE TABLE merge( id, result, moves, date, round, eco, black_id, black_player, black_born, black_birthplace, black_year, black_fed, black_sex, id1, white_id, white_player, white_born, white_birthplace, white_year, white_fed, white_sex)')

c.execute('WITH white_sub AS (SELECT \
			games_id.id AS id, \
			games_id.result, \
			games_id.moves AS moves, \
			games_id.date AS date, \
			games_id.round AS round, \
			games_id.eco AS eco, \
			grandmasters.id AS black_id, \
			grandmasters.name AS black_player, \
			grandmasters.born as black_born, \
			grandmasters.birthplace as black_birthplace, \
			grandmasters.year as black_year, \
			grandmasters.fed as black_fed, \
			grandmasters.sex as black_sex \
		FROM grandmasters \
		LEFT JOIN games_id \
		ON games_id.white_fide_id = grandmasters.id \
), black_sub AS ( \
	SELECT \
			games_id.id AS id1, \
			grandmasters.id AS white_id, \
			grandmasters.name AS white_player, \
			grandmasters.born as white_born, \
			grandmasters.birthplace as white_birthplace, \
			grandmasters.year as white_year, \
			grandmasters.fed as white_fed, \
			grandmasters.sex as white_sex \
		FROM grandmasters \
		LEFT JOIN games_id \
		ON games_id.black_fide_id = grandmasters.id \
) \
INSERT INTO merge (id, result, moves, date, round, eco, black_id, black_player, black_born, black_birthplace, black_year, black_fed, black_sex, id1, white_id, white_player, white_born, white_birthplace, white_year, white_fed, white_sex) \
SELECT white_sub.*, black_sub.* \
FROM (white_sub) \
JOIN (black_sub) \
ON id = id1')

conn.commit()


