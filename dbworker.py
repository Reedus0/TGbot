import json
import config

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