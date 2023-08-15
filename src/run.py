import asyncio
import time
from database.bots import get_good_bots, update_active
from database.bets import put_new_bet, add_bet_result
from db_init import bot_col_init, bet_col_init, bot_wallets_init
from services.bookmaker_api import BookMakerAPI


async def polling():
    await bot_col_init()
    await bet_col_init()
    bot_wallets = await bot_wallets_init()
    bookmaker = BookMakerAPI()
    min_end_time = time.time() + 1e9

    while True:

        bots = await get_good_bots()
        cur_game = ""
        bot = bots[0]

        if bot:

            try:
                wallet_manager = bot_wallets[bot["id"]]

                cur_game = bookmaker.get_active_games()[0]

                comment = cur_game.get("id") + "-" + bot['template']
                bet_value = 0.001

                await wallet_manager.transfer_money(cur_game.get("recipient"), bet_value, comment)
                await put_new_bet(bet_value=bet_value, bot_id=bot["id"], game_id=cur_game.get("id"),
                                  end_time=cur_game.get("end_time"))

                await update_active(0, bot_id=bot["id"])

                min_end_time = min(min_end_time, cur_game.get("end_time"))

            except IndexError:
                print("No available games")
            except Exception as e:
                print(e)

        if len(bots) == 1:
            await asyncio.sleep(min_end_time - time.time() + 10)  # ждем конца ближайшей игры -> бот освободится
            await end_game(bookmaker, bot, bot_wallets[bot["id"]], cur_game)

        else:
            await asyncio.sleep(1)


async def end_game(bookmaker, bot, wallet_manager, cur_game):
    await update_active(1, bot_id=bot["id"])
    cur_game_result = bookmaker.get_game_result(cur_game.get("id"))
    await add_bet_result(cur_game_result, cur_game.get("id"))
    await wallet_manager.have_min_money()


async def main():
    await polling()


if __name__ == '__main__':
    asyncio.run(main())
