import json
import config
import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

def get_current_state(user_id):
    with open(config.config['json_file'], "r") as db:
        try:
            js = json.load(db)
            if js['user_id'] == user_id:
                return js['state']
        except:
            return 0

def set_state(user_id, value):
    with open(config.config['json_file'], "w") as db:
        try:
            data = {
                "user_id" : user_id,
                "state" : value
            }
            json.dump(data, db)
            return True
        except:
            return False

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
