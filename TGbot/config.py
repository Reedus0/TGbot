import os

dir = os.path.abspath(os.curdir) + "\database.json"

config = {
    "name": "YourBotName",
    "token": "yourToken",
    "json_file": dir,
}

class States():
    S_LOGIN = 0
    S_LOGINED_A = 1
    S_END = 2
