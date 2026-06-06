"""
Task:
Write a SQL query to list the names of all people who starred in a movie released in 2004, ordered by birth year.
Your query should output a table with a single column for the name of each person.
People with the same birth year may be listed in any order.
No need to worry about people who have no birth year listed, so long as those who do have a birth year are listed in order.
If a person appeared in more than one movie in 2004, they should only appear in your results once.

results in a table with 1 column and 19,325 rows.
"""

import sqlite3
# pip install sqlite3
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# this is the only line that needs editing
query_code = "SELECT name FROM people JOIN stars ON people.id = stars.person_id JOIN movies ON stars.movie_id = movies.id WHERE movies.year = 2004 GROUP BY people.id ORDER BY birth"



cursor.execute(query_code)
result = cursor.fetchall()
for row in result:
    for item in row:
        print(item, end="\t")
    print()
connection.close()