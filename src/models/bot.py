from pydantic import BaseModel


class Bot(BaseModel):
    id: int
    template: str # мб поменять надо
    active: int
    min_money: int
