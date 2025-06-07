from pydantic import BaseModel
from typing import List


class Meta(BaseModel):
    total: int


class User(BaseModel):
    email: str
    name: str
    nickname: str
    avatar_url: str
    uuid: str


class UsersListResponseModel(BaseModel):
    meta: Meta
    users: List[User]