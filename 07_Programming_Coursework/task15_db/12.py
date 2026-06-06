"""
Task:
Write a SQL query to list the titles of all movies in which both Bradley Cooper and Jennifer Lawrence starred.
Your query should output a table with a single column for the title of each movie.
You may assume that there is only one person in the database with the name Bradley Cooper.
You may assume that there is only one person in the database with the name Jennifer Lawrence.

Find the ID of Bradley Cooper
Find the ID of Jennifer Lawrence
Find the IDs of movies associated with Bradley Cooper’s ID
Find the IDs of movies associated with Jennifer Lawrence’s ID
Find movie titles from the movie IDs associated with both Bradley Cooper and Jennifer Lawrence
Then, try nesting those queries to arrive at a single query that returns the movies in which both Bradley Coop

results in a table with 1 column and 4 rows.
"""

import sqlite3
# pip install sqlite3
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# this is the only line that needs editing
query_code = "SELECT m.title FROM movies m JOIN stars s ON m.id = s.movie_id JOIN people p ON s.person_id = p.id WHERE p.name IN ('Bradley Cooper', 'Jennifer Lawrence') GROUP BY m.id HAVING COUNT(DISTINCT p.name) = 2;"

cursor.execute(query_code)
result = cursor.fetchall()
for row in result:
    for item in row:
        print(item, end="\t")
    print()
connection.close()