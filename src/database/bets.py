from src.mongodb import bet_col


def put_new_bet(bet_value, end_time, bot_id, game_id):
    id_ = bet_col.count_documents({}) # O(n), надо глобальную переменную заиметь для этого как будто
    bet = {"id": id_, "bet_value": bet_value, "bot_id": bot_id, "game_id": game_id, "end_time": end_time}
    bet_col.insert_one(bet)