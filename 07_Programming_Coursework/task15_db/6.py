"""
Task:
Write a SQL query to determine the average rating of all movies released in 2012.
Your query should output a table with a single column and a single row (not counting the header) containing the average rating.

results in a table with 1 column and 1 row.
"""

import sqlite3
# pip install sqlite3
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# this is the only line that needs editing
query_code = "SELECT avg(rating) FROM ratings left join movies on ratings.movie_id=movies.id where movies.year=2012"

cursor.execute(query_code)
result = cursor.fetchall()
for row in result:
    for item in row:
        print(item, end="\t")
    print()
connection.close()