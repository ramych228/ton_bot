from database.bots import get_good_bots, update_min_money
from db_init import bot_col_init
from services.bookmaker_api import BookMakerAPI
from services.ton_connector import TonConnector
from config import BotConfigs, start_config

if __name__ == '__main__':
    start_config()
    bot_config = BotConfigs()

    bookmaker = BookMakerAPI('https://bookmakerapi.startech.live')

    connector = TonConnector()
    wallet_client = connector.client
    seed = bot_config.BOT_SEEDS["SEED_BOT0"]
    wallet = connector.client.import_wallet(seed)

    bot_col_init()
    bot = get_good_bots()

    if bot:
        try:
            game_address = bookmaker.get_active_games()[0]

            template = bot["template"]

            print(game_address + "-" + template)

        except IndexError:
            print("No available games")
