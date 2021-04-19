import sqlite3

def commit(text):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    j = 0
    i = 0

    while j != 1:
        i = i + 1
        try:
            cursor.execute("""INSERT INTO index_message
                                VALUES ("{0}", "{1}")""".format(i, text)
                            )
            j = 1
        except:
            pass

    conn.commit()