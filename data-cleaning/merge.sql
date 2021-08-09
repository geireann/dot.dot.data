SELECT *
FROM grandmasters
LEFT JOIN games
ON games.white_player = grandmasters.name
UNION ALL
SELECT *
FROM grandmasters
LEFT JOIN games
ON games.black_player = grandmasters.name

SELECT
	grandmasters.id AS white_id,
	grandmasters.name AS white_player,
	grandmasters.born as white_born,
	grandmasters.birthplace as white_birthplace,
	grandmasters.year as white_year,
	grandmasters.fed as white_fed,
	grandmasters.sex as white_sex
FROM grandmasters
LEFT JOIN games
ON games.white_player = grandmasters.name
UNION ALL
SELECT
	grandmasters.id AS black_id,
	grandmasters.name AS black_player,
	grandmasters.born as black_born,
	grandmasters.birthplace as black_birthplace,
	grandmasters.year as black_year,
	grandmasters.fed as black_fed,
	grandmasters.sex as black_sex
FROM grandmasters
LEFT JOIN games
ON games.black_player = grandmasters.name