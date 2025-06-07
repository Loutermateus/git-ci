from pydantic import BaseModel




class CreateUserResponseModel(BaseModel):
    email: str
    name: str
    nickname: str
    avatar_url: str
    uuid: str