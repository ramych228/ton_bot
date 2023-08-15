from src.mongodb import bot_col
from models.bot import Bot


async def get_good_bots():  # смотрим, есть ли свободные боты c деньгами по db
    query = {'active': 1, 'have_min_money': 1}
    result = await bot_col.find(query).limit(1).to_list(1)

    if len(result) == 0:
        return [0]
    else:
        return result


async def update_have_min_money(min_money: int, bot_id: int):
    bot = await bot_col.find_one({'id': bot_id})
    bot["have_min_money"] = int(min_money)
    await bot_col.replace_one({'id': bot_id}, bot)


async def update_active(active: int, bot_id: int):
    bot = await bot_col.find_one({'id': bot_id})
    bot["active"] = active
    await bot_col.replace_one({'id': bot_id}, bot)
