from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
import uvicorn
from typing import Annotated
from datetime import timedelta
from model import User,UserInDB,Token,TokenData
from data import fake_users_db as db
from passlib.context import CryptContext


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pass_context = CryptContext(schemes=['bcrypt'],deprecated="auto")


def create_password_hash(password:str):
    return pass_context.hash(password)

def verify_password(plain_password:str,hashed_password:str):
    return pass_context.verify(plain_password,hashed_password)


def get_user(username:str):
    if username in db:
        user_record = db[username]
        return UserInDB(**user_record)


def authentic_user(username:str,password:str):
    user = db[username]
    if not user:
        return False
    if not verify_password(password,user.hashed_password):
        return False
    return user


def create_access_token(data:dict,expires_time:timedelta|None=None):
    ...

async def get_current_user(token:Annotated[str,Depends(oauth2_scheme)]):
    ...


async def get_current_active_user(current_user:Annotated[User,Depends(get_current_user)]):
    ...


if __name__ == "__main__":
    uvicorn.run('code:app',reload=True)