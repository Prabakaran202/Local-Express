from pydantic import BaseModel,Field
from typing import Optional


class FoodItem(BaseModel):
    id:int
    name:str=Field(...,min_length =3)
    price :float =Field(...,gt=0)
    category:str
    is_available:bool=True

#neew items add 

class FoodIemCreate(BaseModel):
    name:str
    price:float
    category:str