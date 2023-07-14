from pymongo import MongoClient

client = MongoClient('mongodb://root:example@localhost:27017/')

ton_bot_db = client["ton_bot"]

bot_col = ton_bot_db["bots"]
bet_col = ton_bot_db["bets"]