"""
Task:
Write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.
Your query should output a table with a single column for the name of each person.
There may be multiple people named Kevin Bacon in the database. Be sure to only select the Kevin Bacon born in 1958.
Kevin Bacon himself should not be included in the resulting list.

Find the ID of Kevin Bacon (the one born in 1958!)
Find the IDs of movies associated with Kevin Bacon’s ID
Find the IDs of people associated with those movie IDs
Find the names of people with those people IDs

results in a table with 1 column and 182 rows.

"""

import sqlite3
# pip install sqlite3
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# this is the only line that needs editing
query_code = "SELECT DISTINCT p2.name FROM people p1 JOIN stars s1 ON p1.id = s1.person_id JOIN stars s2 ON s1.movie_id = s2.movie_id JOIN people p2 ON s2.person_id = p2.id WHERE p1.name = 'Kevin Bacon' AND p1.birth = 1958 AND p2.name != 'Kevin Bacon'"

cursor.execute(query_code)
result = cursor.fetchall()
for row in result:
    for item in row:
        print(item, end="\t")
    print()
connection.close()