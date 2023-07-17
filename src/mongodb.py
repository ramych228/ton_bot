import os
import motor.motor_asyncio
from config import start_config

start_config()
USER = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
PASS = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")

uri = "mongodb://{}:{}@localhost:27017/".format(USER, PASS)

client = motor.motor_asyncio.AsyncIOMotorClient(uri)

ton_bot_db = client["ton_bot"]

bot_col = ton_bot_db["bots"]
bet_col = ton_bot_db["bets"]