import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    curr = conn.cursor()

    curr.execute("""
    DELETE FROM films WHERE title LIKE 'Я%' AND title LIKE '%а';""")

    conn.commit()
    conn.close()
