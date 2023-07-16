import asyncio
import time
from database.bots import get_good_bots, update_min_money
from db_init import bot_col_init
from services.bookmaker_api import BookMakerAPI
from services.ton_connector import TonConnector
from services.wallet_management import WalletManagement
from config import BotConfigs, start_config


async def polling():
    start_config()
    bot_col_init()
    bot_config = BotConfigs()
    # TODO: url неизменяемый параметр для класса BookMakerAPI, поэтому не передаем в инициализацию
    # В инициализацию классов передаем изменяемые переменные типа логина, пароля и тд
    bookmaker = BookMakerAPI('https://bookmakerapi.startech.live')
    connector = TonConnector()

    while True:
        # TODO: следим за неймингом, good - непонятно, множественное или единтвенное число?
        bot = get_good_bots()

        if bot:

            seed = bot_config.BOT_SEEDS["SEED_BOT" + str(bot["id"])]
            print(bot, seed)

            try:
                wallet_manager = WalletManagement(connector)
                await wallet_manager.async_init(seed)
                wallet = wallet_manager.wallet
                x = await wallet_manager.get_min_money()
                print(x)
                game_address = bookmaker.get_active_games()[0]

                template = bot["template"]
                # TODO: хорошо было бы потом не забыть добавить проверку последних транзакций у бота, чтобы если приложение сломается и будут бесконечные рестарты, у тебя деньги с ботов утекут в одну игру
                print(game_address + "-" + template)

            except IndexError:
                print("No available games")
        await asyncio.sleep(1)


async def main():
    await polling()


if __name__ == '__main__':
    asyncio.run(main())
