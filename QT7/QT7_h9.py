import sqlite3

conn = sqlite3.connect(input())

curr = conn.cursor()

curr.execute("""
SELECT DISTINCT genres.title FROM films 
JOIN genres ON films.genre = genres.id WHERE films.year = 2010 OR films.year = 2011;""")

result = curr.fetchall()

for i in result:
    print(i[0])
