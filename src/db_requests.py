from pymongo import MongoClient

client = MongoClient('mongodb://root:example@localhost:27017/')

ton_bot_db = client["ton_bot"]

bot_col = ton_bot_db["bots"]
bet_col = ton_bot_db["bets"]


def find_good_bots():  # смотрим, есть ли свободные боты c деньгами по db
    query = {'active': 1, 'min_money': 1}
    result = bot_col.find(query).limit(1)

    try:
        return result[0]
    except IndexError:
        return 0


def put_new_bet(bet_value, end_time, bot_id, game_id):
    id_ = bet_col.count_documents({}) # O(n), надо глобальную переменную заиметь для этого как будто
    bet = {"id": id_, "bet_value": bet_value, "bot_id": bot_id, "game_id": game_id, "end_time": end_time}
    bet_col.insert_one(bet)


if __name__ == '__main__':
    find_good_bots()
