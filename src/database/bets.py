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


async def get_all_bets():
    all_docs = []
    cursor = bet_col.find({})
    for doc in cursor:
        all_docs.append(doc)
    return all_docs
