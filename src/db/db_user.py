from sqlalchemy.orm.session import Session
from request_models.user_request import UserBase
from db.models import DbUser
from db.hash import Hash
from fastapi import HTTPException, status

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username, 
        email=request.email, 
        password=Hash.bcrypt(request.password)
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_uesrs(db: Session):
    return db.query(DbUser).all()

def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with username {username} not found")
    return user

def update_user(db:Session, id:int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with id {id} not found")
    user.update({

        DbUser.username : request.username,
        DbUser.email : request.email,
        DbUser.password : Hash.bcrypt(request.password)
    })
    db.commit()
    return "Ok"


def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with id {id} not found")
    db.delete(user)
    db.commit()
    return "Ok"