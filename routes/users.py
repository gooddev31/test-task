from fastapi_jwt_auth import AuthJWT
from fastapi import APIRouter, Depends, HTTPException

from schemas.user import User, CreateUser

router = APIRouter(tags=["users"])

@router.post('/login')
def login(user: CreateUser, Authorize: AuthJWT = Depends()):
    if user.username != "test" or user.password != "test":
        raise HTTPException(status_code=401,detail="Bad username or password")

    access_token = Authorize.create_access_token(subject=user.username)
    return {"access_token": access_token}

@router.get('/user')
def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}
