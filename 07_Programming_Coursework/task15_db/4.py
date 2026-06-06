"""
Task:
Write a SQL query to determine the number of movies with an IMDb rating of 10.0.
Your query should output a table with a single column and a single row (not counting the header) containing the number of movies with a 10.0 rating.

results in a table with 1 column and 1 row.
"""

import sqlite3
# pip install sqlite3
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# this is the only line that needs editing
query_code = "SELECT count(rating) FROM ratings where rating=10.0"

cursor.execute(query_code)
result = cursor.fetchall()
for row in result:
    for item in row:
        print(item, end="\t")
    print()
connection.close()