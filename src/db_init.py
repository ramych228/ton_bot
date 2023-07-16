from mongodb import bot_col


def bot_col_init():
    bot_col.delete_many({})
    bot_init_data = [
        {'id': 0, 'template': 'UP', 'active': 1, 'min_money': 1},
        {'id': 1, 'template': 'DOWN', 'active': 1, 'min_money': 1},
        {'id': 2, 'template': 'NO_CHANGE', 'active': 1, 'min_money': 1}
    ]
    bot_col.insert_many(bot_init_data)
    print('Данные успешно добавлены.')


# TODO: так не делаем, не видно, что этот код выполняется
if __name__ == '__main__':
    bot_col_init()
    for x in bot_col.find():
        print(x)
