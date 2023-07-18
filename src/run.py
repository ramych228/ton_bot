import asyncio
import time
from config import BotConfigs, start_config
from database.bots import get_good_bot
from database.bets import put_new_bet, get_all_bets
from db_init import bot_col_init, bet_col_init, bot_wallets_init
from services.bookmaker_api import BookMakerAPI


async def polling():
    # start_config()
    await bot_col_init()
    await bet_col_init()
    bot_wallets = await bot_wallets_init()
    bookmaker = BookMakerAPI()
    min_end_time = 0

    while True:

        bot = await get_good_bot()

        if bot:

            try:
                #
                # bets = await get_all_bets()
                # for x in bets:
                #     print(x)

                wallet_manager = bot_wallets[bot["id"]]

                cur_game = bookmaker.get_active_games()[0]
                cur_game_id = cur_game.get("id")
                cur_game_recipient = cur_game.get("recipient")
                cur_game_end_time = cur_game.get("end_time")

                txs = await wallet_manager.wallet.get_balance()
                print(txs)

                comment = cur_game_id + "-" + bot['template']
                bet_value = 0.001

                # await wallet_manager.transfer_money(cur_game_recipient, bet_value, comment)
                # await put_new_bet(bet_value=bet_value, bot_id=bot["id"], game_id=cur_game_id,
                #                   end_time=cur_game_end_time)


                min_end_time = min(min_end_time, cur_game_end_time)  # надо пофиксить, когда поллинг доделывать буду

            except IndexError:
                print("No available games")
            except:
                print("Unknown error")

        await asyncio.sleep(min_end_time - time.time() + 10)  # ждем конца ближайшей игры -> бот освободится


async def main():
    await polling()


if __name__ == '__main__':
    asyncio.run(main())
