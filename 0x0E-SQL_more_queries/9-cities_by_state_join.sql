-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id AS city_id, cities.name AS city_name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

