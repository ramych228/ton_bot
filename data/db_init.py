from pymongo import MongoClient

my_client = MongoClient("mongodb://root:example@localhost:27017/")

ton_bot_db = my_client["ton_bot"]

bot_col = ton_bot_db["bots"]
bet_col = ton_bot_db["bets"]


def bot_col_init():
    if bot_col.count_documents({}) == 0:
        data = [
            {'id': '0', 'template': 'UP', 'active': 'true', 'min_money': 'true'},
            {'id': '1', 'template': 'DOWN', 'active': 'true', 'min_money': 'true'},
            {'id': '1', 'template': 'NO_CHANGE', 'active': 'true', 'min_money': 'true'}
        ]
        bot_col.insert_many(data)
        print('Данные успешно добавлены.')
    else:
        print('Данные уже присутствуют в коллекции.')


if __name__ == '__main__':
    bot_col_init()
    for x in bot_col.find():
        print(x)

    my_client.close()
