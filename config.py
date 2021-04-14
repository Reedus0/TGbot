import os

dir = os.path.abspath(os.curdir) + "\database.json"

config = {
    "name": "@TGtestbot",
    "token": "1622866884:AAHVFMLXDhxKVk2RvDIIUmqZyaC1PPpLAIo",
    "json_file": dir,
}

class States():
    S_LOGIN = 0
    S_LOGINED_A = 1
    S_END = 2