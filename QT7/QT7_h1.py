import sqlite3

conn = sqlite3.connect(input())
curr = conn.cursor()

obj = curr.execute("""
SELECT films.title FROM films JOIN genres ON films.genre = genres.id WHERE genres.title IN ('музыка', 'анимация') 
AND films.year >= 1997""")
for word in obj:
    print(word[0])
