from pydantic import BaseModel


class User(BaseModel):
    username: str = None
    full_name: str = None
    email: str = None
    disabled: bool | None

class Token(BaseModel):
    access_token:str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None


class UserInDb(User):
    hashed_password: str = None

