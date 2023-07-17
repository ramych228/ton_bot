from mongodb import bot_col
from models.bot import Bot


async def bot_col_init():
    await bot_col.delete_many({})
    bot_init_data = [
        Bot(id=0, template='UP', active=1, have_min_money=1),
        Bot(id=1, template='DOWN', active=1, have_min_money=0),
        Bot(id=2, template='NO_CHANGE', active=1, have_min_money=0)
    ]
    for x in bot_init_data:
        await bot_col.insert_one(x.model_dump())
    print('Данные успешно добавлены.')
