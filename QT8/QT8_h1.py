import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id FROM genres WHERE title = 'комедия'")
        comedy_genre_id = cursor.fetchone()

        if comedy_genre_id:
            comedy_genre_id = comedy_genre_id[0]
            cursor.execute("DELETE FROM films WHERE genre = ?", (comedy_genre_id,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Произошла ошибка: {e}")
    finally:
        conn.close()
