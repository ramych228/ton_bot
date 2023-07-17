from src.mongodb import bet_col
from models.bet import Bet


async def put_new_bet(bet_value: int, end_time: int, bot_id: int, game_id: str):
    bet = Bet(
        id=await bet_col.count_documents({}),
        bet_value=bet_value,
        bot_id=bot_id,
        game_id=game_id,
        end_time=end_time,
    )
    await bet_col.insert_one(bet.model_dump())
