from src.mongodb import bot_col
from models.bot import Bot


async def get_good_bot():  # смотрим, есть ли свободные боты c деньгами по db
    query = {'active': 1, 'min_money': 1}
    result = await bot_col.find(query).limit(1).to_list(1)

    try:
        return result[0]
    except IndexError:
        return 0


async def update_min_money(min_money: int, bot_id: int):
    bot = Bot.get_by_id(bot_id)
    bot.min_money = min_money
    await bot_col.replace_one({'id': bot_id}, bot.dict())
