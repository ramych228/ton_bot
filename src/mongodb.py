import os
from pymongo import MongoClient

USER = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
PASS = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")

uri = 'mongodb://{}:{}@localhost:27017/'.format(USER, PASS)

# client = MongoClient(uri) надо это нормально сделать, но не могу подключить нормально HELP

client = MongoClient('mongodb://root:example@localhost:27017/')

ton_bot_db = client["ton_bot"]

bot_col = ton_bot_db["bots"]
bet_col = ton_bot_db["bets"]