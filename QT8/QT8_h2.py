import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    curr = conn.cursor()

    curr.execute("UPDATE films SET duration = '42' WHERE duration = ''")
    conn.commit()
    conn.close()
