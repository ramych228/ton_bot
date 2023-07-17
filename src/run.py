import asyncio
import time
from config import BotConfigs, start_config
from database.bots import get_good_bot, update_min_money
from db_init import bot_col_init
from services.bookmaker_api import BookMakerAPI
from services.ton_connector import TonConnector
from services.wallet_management import WalletManagement


async def polling():
    start_config()
    await bot_col_init()
    bot_config = BotConfigs()
    bookmaker = BookMakerAPI()
    connector = TonConnector()

    while True:

        bot = await get_good_bot()

        if bot:

            seed = bot_config.BOT_SEEDS["SEED_BOT" + str(bot["id"])]
            print(bot, seed)

            try:
                wallet_manager = WalletManagement(connector)
                await wallet_manager.async_init(seed)

                x = await wallet_manager.get_min_money()
                print(x)
                cur_game = bookmaker.get_active_games()[0]
                cur_game_id = cur_game.get("id")
                cur_game_end_time = cur_game.get("end_time")

                template = bot["template"]
                # TODO: хорошо было бы потом не забыть добавить проверку последних транзакций у бота, чтобы если
                #  приложение сломается и будут бесконечные рестарты, у тебя деньги с ботов утекут в одну игру
                print(cur_game_id + "-" + template)

            except IndexError:
                print("No available games")
        await asyncio.sleep(1)


async def main():
    await polling()


if __name__ == '__main__':
    asyncio.run(main())
