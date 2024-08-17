from fastapi import APIRouter, Depends
from request_models.user_request import UserBase
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_user
from respons_models.user_respons import UserDisplay
from typing import List

router = APIRouter(
    prefix="/user",
    tags=['User']
)

#create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)
    

#read all user
@router.get('/', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_uesrs(db)

#read user by id
@router.get('/{id}', response_model=UserDisplay)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return db_user.get_user_by_id(db, id)


#update user
@router.post('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, id, request)


#delete user
@router.delete('/delete/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id)