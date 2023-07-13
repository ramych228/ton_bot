from db_requests import find_good_bots
from data.db_init import bot_col_init
from api_requests import get_active_games
from wallet_init import client

if __name__ == '__main__':
    bot_col_init()
    bot = find_good_bots()

    if bot:  # надо придумать поизящней решение
        try:
            game_address = get_active_games()[0]

            template = bot["template"]
            seed = bot["seed"]

            wallet = await client.import_wallet(seed)

            print(game_address + "-" + template)

        except IndexError:
            print("No available games")
