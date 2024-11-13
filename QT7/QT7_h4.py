import sqlite3

conn = sqlite3.connect(input())

cur = conn.cursor()

cur.execute(
    """
SELECT films.title FROM films JOIN genres ON films.genre = genres.id WHERE genres.title = 'комедия' 
AND films.duration >= 60;""")
result = cur.fetchall()
for row in result:
    print(row[0])
