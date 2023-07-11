from pymongo import MongoClient

client = MongoClient('mongodb://root:example@localhost:27017/')

ton_bot_db = client["ton_bot"]

bot_col = ton_bot_db["bots"]


def find_good_bots():  # смотрим, есть ли свободные боты c деньгами по db
    query = {'active': 1, 'min_money': 1}
    result = bot_col.find(query).limit(1)

    try:
        return result[0]
    except IndexError:
        return 0


if __name__ == '__main__':
    find_good_bots()
