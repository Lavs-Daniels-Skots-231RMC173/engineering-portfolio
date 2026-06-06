"""
Task:
Write a SQL query to determine the birth year of Emma Stone.
Your query should output a table with a single column and a single row (not counting the header) containing Emma Stone’s birth year.
You may assume that there is only one person in the database with the name Emma Stone.

results in a table with 1 column and 1 row.
"""

import sqlite3
# pip install sqlite3
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# this is the only line that needs editing
query_code = "SELECT birth FROM people where name='Emma Stone'"

cursor.execute(query_code)
result = cursor.fetchall()
for row in result:
    for item in row:
        print(item, end="\t")
    print()
connection.close()