from typing import List

from fastapi_jwt_auth import AuthJWT
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.connection import get_db
from schemas.posts import DeletePostResponse, Post, UpdatePost
from controllers.post_crud import (
    post_create,
    post_delete,
    post_update,
    get_user_posts
)
from fastapi_cache.decorator import cache

router = APIRouter(tags=["posts"])

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=Post)
def create_post(post: Post, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return post_create(db=db, post=post)


@router.get("/list/all", status_code=status.HTTP_200_OK, response_model=List[Post])
@cache(expire=300)
def get_all_posts(db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    return get_user_posts(db, current_user)


@router.delete(
    "/delete/{id}", status_code=status.HTTP_200_OK, response_model=DeletePostResponse
)

def delete_post(id, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    delete_status = post_delete(db=db, id=id)
    if delete_status.detail == "Doesnt Exist":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post Not Found"
        )
    else:
        return delete_status


@router.patch("/update", status_code=status.HTTP_200_OK, response_model=Post)
def update_post(post: UpdatePost, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return post_update(db=db, post=post)
