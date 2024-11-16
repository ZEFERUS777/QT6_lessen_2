import sqlite3

conn = sqlite3.connect(input())

cur = conn.cursor()
cur.execute("SELECT films.title FROM films WHERE films.duration <= 85")

reslt = cur.fetchall()
for i in reslt:
    print(i[0])
