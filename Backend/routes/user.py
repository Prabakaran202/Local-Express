from fastapi import APIRouter,HTTPException
from schemas.user import FoodItem, FoodIemCreate
router =APIRouter(prefix="/users",tags=["users"])



mdb=[{"id":3,"name":"dhosa","price":2445,"category":"teabenitems"}]


@router.get("/")
async def get_all_user():
    return mdb
@router.get("/add")
async def add_user(user:FoodIemCreate):
    new_user = {"id": len(mdb) + 1, **user.model_dump(), "is_active": True}
    mdb.append(new_user)
    return new_user