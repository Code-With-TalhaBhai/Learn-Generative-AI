from pydantic import BaseModel


class User(BaseModel):
    username: str | None = None
    full_name: str | None = None
    email: str | None = None
    disabled: bool | None = None

class Token(BaseModel):
    access_token:str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserInDb(User):
    hashed_password: str | None

