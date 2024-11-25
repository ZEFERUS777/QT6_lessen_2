import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    curr = conn.cursor()

    curr.execute("SELECT id FROM genres WHERE title = 'боевик'")
    comedy_id = curr.fetchone()

    if comedy_id:
        comedy_id = comedy_id[0]
        curr.execute("""DELETE FROM films WHERE genre = ? and duration >= 90""", (comedy_id,))
        conn.commit()
