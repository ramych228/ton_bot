from pydantic import BaseModel


class Bot(BaseModel):
    id: int
    template: str # мб поменять надо
    active: int
    have_min_money: int
