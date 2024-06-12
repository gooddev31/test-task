from pydantic import BaseModel

class Post(BaseModel):
    id: int
    text: str
    user_id: int

    class Config:
        orm_mode = True


class DeletePostResponse(BaseModel):
    detail: str


class UpdatePost(BaseModel):
    id: int
    text: str

    class Config:
        orm_mode = True
