from db_requests import find_good_bots
from api_requests import get_active_games

if __name__ == '__main__':
    bot = find_good_bots()

    if bot:  # надо придумать поизящней решение
        try:
            game_address = get_active_games()[0]

            template = bot["template"]


            print(game_address + "-" + template)

        except IndexError:
            print("No available games")
