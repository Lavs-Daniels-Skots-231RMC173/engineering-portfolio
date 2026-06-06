"""
Task:
Write a SQL query to list the names of all people who starred in Toy Story.
Your query should output a table with a single column for the name of each person.
You may assume that there is only one movie in the database with the title Toy Story.

results in a table with 1 column and 4 rows.
"""

import sqlite3
# pip install sqlite3
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# this is the only line that needs editing
query_code = "SELECT name FROM people LEFT JOIN stars on people.id = stars.person_id LEFT JOIN movies on stars.movie_id = movies.id WHERE title = 'Toy Story'"

cursor.execute(query_code)
result = cursor.fetchall()
for row in result:
    for item in row:
        print(item, end="\t")
    print()
connection.close()