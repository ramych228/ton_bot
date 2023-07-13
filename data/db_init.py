from pymongo import MongoClient

my_client = MongoClient("mongodb://root:example@localhost:27017/")

ton_bot_db = my_client["ton_bot"]

bot_col = ton_bot_db["bots"]
bet_col = ton_bot_db["bets"]


def bot_col_init():
    if bot_col.count_documents({}) == 0:
        bot_init_data = [
            {'id': 0, 'template': 'UP', 'active': 1, 'min_money': 1,
             'address': 'EQDyegU155LTDQrQYSAp-cDYG41YTK-crIkxdEx1DV4A3-CK',
             'seed': ['crush', 'brand', 'kid', 'night', 'foster', 'fuel', 'divide', 'curtain', 'wish', 'evoke',
                      'father', 'decline', 'album', 'cable', 'oblige', 'mercy', 'sphere', 'chest', 'ghost', 'almost',
                      'shell', 'escape', 'aim', 'limb']
             # это надо убрать отсюда очевидно, но я не очень понимаю куда и как
             },
            {'id': 1, 'template': 'DOWN', 'active': 1, 'min_money': 1,
             'address': 'EQAJdaddEC1EUMEFbLcJw6Kn6pkSuWOFWQu5mTEMcmQZwffL',
             'seed': ['laptop', 'dragon', 'income', 'decade', 'coral', 'genius', 'conduct', 'song', 'citizen',
                      'diagram', 'exist', 'garage', 'today', 'amused', 'page', 'talent', 'salt', 'play', 'pair',
                      'eyebrow', 'witness', 'attitude', 'come', 'profit']
             },
            {'id': 2, 'template': 'NO_CHANGE', 'active': 1, 'min_money': 0,
             'address': 'EQCBwpZwgGEzzX58qITrPWf0-Kvhy9fTuqJLKK1yISt4RVqm',
             'seed': ['pause', 'kidney', 'april', 'disagree', 'dust', 'nut', 'sunny', 'earth', 'fee', 'fiscal',
                      'carbon', 'champion', 'conduct', 'leisure', 'tuna', 'kid', 'frame', 'skull', 'pulse', 'calm',
                      'denial', 'emerge', 'pottery', 'nut']
             }
        ]
        bot_col.insert_many(bot_init_data)
        print('Данные успешно добавлены.')
    else:
        print('Данные уже присутствуют в коллекции.')


if __name__ == '__main__':
    bot_col_init()
    for x in bot_col.find():
        print(x)

    my_client.close()
