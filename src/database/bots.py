from src.mongodb import bot_col


def get_good_bots():  # смотрим, есть ли свободные боты c деньгами по db
    query = {'active': 1, 'min_money': 1}
    result = bot_col.find(query).limit(1)

    try:
        return result[0]
    except IndexError:
        return 0


def update_min_money(min_money: int, bot_id: int):
    filter_query = {'id': bot_id}
    update_query = {'$set': {'min_money': min_money}}
    bot_col.update_one(filter_query, update_query)
