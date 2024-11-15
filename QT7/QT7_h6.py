import sqlite3

conn = sqlite3.connect(input())
curr = conn.cursor()

curr.execute("""
SELECT films.title FROM films 
JOIN genres ON films.genre = genres.id WHERE genres.title = 'детектив' AND year BETWEEN 1995 AND 2000 """)

result = curr.fetchall()

for i in result:
    print(i[0])
