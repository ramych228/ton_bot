import asyncio
import time
from config import BotConfigs, start_config
from database.bots import get_good_bot, update_min_money
from database.bets import put_new_bet
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
    min_end_time = None

    while True:

        bot = await get_good_bot()

        if bot:

            seed = bot_config.BOT_SEEDS["SEED_BOT" + str(bot["id"])]
            print(bot, seed)

            try:
                wallet_manager = WalletManagement(connector, seed)
                await wallet_manager.async_init()

                cur_game = bookmaker.get_active_games()[0]
                cur_game_id = cur_game.get("id")
                cur_game_recipient = cur_game.get("recipient")
                cur_game_end_time = cur_game.get("end_time")

                txs = await wallet_manager.wallet.get_transactions()
                print(txs)

                comment = cur_game_id + "-" + bot['template']
                bet_value = 0.001

                await wallet_manager.transfer_money(cur_game_recipient, bet_value, comment)
                await put_new_bet(bet_value=bet_value, bot_id=bot["id"], game_id=cur_game_id,
                                  end_time=cur_game_end_time)

                min_end_time = min(min_end_time, cur_game_end_time) # надо пофиксить, когда поллинг доделывать буду

            except IndexError:
                print("No available games")
            except:
                print("Unknown error")

        await asyncio.sleep(min_end_time - time.time() + 10) # ждем конца ближайшей игры -> бот освободится


async def main():
    await polling()


if __name__ == '__main__':
    asyncio.run(main())
