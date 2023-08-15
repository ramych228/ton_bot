from config import BotConfigs, start_config
from mongodb import bot_col, bet_col
from models.bot import Bot
from models.bet import Bet
from services.wallet_management import WalletManagement
from services.ton_connector import TonConnector
from database.bots import update_have_min_money


async def bot_wallets_init():
    start_config()
    tc = TonConnector()
    await tc.async_init()

    bot_config = BotConfigs()
    wm0 = WalletManagement(tc, bot_config.BOT_SEEDS["SEED_BOT0"])
    wm1 = WalletManagement(tc, bot_config.BOT_SEEDS["SEED_BOT1"])
    wm2 = WalletManagement(tc, bot_config.BOT_SEEDS["SEED_BOT2"])
    await wm0.async_init()
    await wm1.async_init()
    await wm2.async_init()

    bot_wallets = [wm0, wm1, wm2]

    for i in range(len(bot_wallets)):
        new_have_min_money = await bot_wallets[i].have_min_money()
        await update_have_min_money(new_have_min_money, i)

    return bot_wallets


async def bot_col_init():
    await bot_col.delete_many({})

    bot_init_data = [
        Bot(id=0, template='UP', active=1, have_min_money=0),
        Bot(id=1, template='DOWN', active=1, have_min_money=0),
        Bot(id=2, template='NO_CHANGE', active=1, have_min_money=0)
    ]
    for x in bot_init_data:
        await bot_col.insert_one(x.model_dump())

    print('Данные ботов успешно добавлены.')


async def bet_col_init():
    await bet_col.delete_many({})

    await bet_col.insert_one(Bet(id=-1, bet_value=-1, bot_id=-1, game_id="-1", end_time=0).model_dump())

    print('Коллекция ставок создана')
