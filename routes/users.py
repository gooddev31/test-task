from fastapi_jwt_auth import AuthJWT
from fastapi import APIRouter, Depends, HTTPException

from controllers.user_crud import create_user, get_user
from schemas.user import CreateUser
from database.connection import get_db
from sqlalchemy.orm import Session

router = APIRouter(tags=["users"])


@router.post("/login")
def login(
    user: CreateUser, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)
):
    try:
        user = get_user(db, user.email, user.password)
        access_token = Authorize.create_access_token(subject=user.email)
        return {"access_token": access_token}
    except:
        raise HTTPException(status_code=401, detail="Bad username or password")


@router.post("/signup")
def signup(
    user: CreateUser, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)
):
    try:
        user = create_user(db, user)
        access_token = Authorize.create_access_token(subject=user.email)
        return {"access_token": access_token}
    except:
        raise HTTPException(status_code=401, detail="Error while creating new user")


@router.get("/user")
def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}
