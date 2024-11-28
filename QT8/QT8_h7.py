import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    curr = conn.cursor()

    curr.execute('SELECT id FROM genres WHERE title = "мюзикл"')

    genre_id = curr.fetchone()

    if genre_id:
        genre_id = genre_id[0]

        curr.execute("""
        UPDATE films SET duration = 100 WHERE duration > 100 AND genre = ?""", (genre_id,))
        conn.commit()
        conn.close()
