"""
Task:
Write a SQL query to list the titles of all movies released in 2008.
Your query should output a table with a single column for the title of each movie.

results in a table with 1 column and 10,276 rows.
"""

import sqlite3
# pip install sqlite3
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# this is the only line that needs editing
query_code = "SELECT Title FROM movies where Year=2008"

cursor.execute(query_code)
result = cursor.fetchall()
for row in result:
    for item in row:
        print(item, end="\t")
    print()
connection.close()