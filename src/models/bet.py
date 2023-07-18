from pydantic import BaseModel


class Bet(BaseModel):
    id: int
    bet_value: float
    bot_id: int
    game_id: str
    end_time: int
