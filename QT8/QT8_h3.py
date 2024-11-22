import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM genres WHERE title = 'фантастика'")
    fantasy_genre_id = cursor.fetchone()

    if fantasy_genre_id:
        fantasy_genre_id = fantasy_genre_id[0]
        cursor.execute("UPDATE films SET duration = duration * 2 WHERE genre = ?", (fantasy_genre_id,))
        conn.commit()

    conn.close()
