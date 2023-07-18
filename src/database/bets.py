from src.mongodb import bet_col
from models.bet import Bet


async def put_new_bet(bet_value: float, end_time: int, bot_id: int, game_id: str):
    bet = Bet(
        id=await bet_col.count_documents({}),
        bet_value=bet_value,
        bot_id=bot_id,
        game_id=game_id,
        end_time=end_time,
    )
    await bet_col.insert_one(bet.model_dump())


async def add_bet_result(result: int, game_id: str):
    bet = await bet_col.find_one({'game_id': game_id})
    bet["result"] = result
    await bet_col.replace_one({'id': game_id}, bet)  # replace_many?
