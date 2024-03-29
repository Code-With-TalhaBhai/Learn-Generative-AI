from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
import uvicorn
from typing import Annotated
from model import User,UserInDB
from user_db import fake_users_db as db


app = FastAPI()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def fake_hashed(password:str):
    return 'fakehashed' + password


def check_user_in_db(username:str):
    if username in db:
        user_detail = db[username]
        return UserInDB(**user_detail)


async def get_current_user(token:Annotated[str,Depends(oauth2_scheme)]):
    user = check_user_in_db(token)
    # if user == None
    if not user: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found in Db",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return user


async def get_current_active_user(current_user:Annotated[str,Depends(get_current_user)]):
    if current_user.disabled == True:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user. Please activate first"
            )
    return current_user


@app.get('/')
def index():
    return {'me':'thinking'}

# @app.post('/token')
@app.post('/login')
async def login(form_data:Annotated[OAuth2PasswordRequestForm,Depends()]):
    user_dict = db.get(form_data.username)
    user_dict["disabled"] = False
    if not user_dict:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    user = UserInDB(**user_dict)
    hashed_password = fake_hashed(form_data.password)

    if not hashed_password and hashed_password != user.hashed_password:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect password"
        )

    return {"access_token":user.username,"token_type": "bearer"}



@app.get('/users/me')
def user_me(current_user:Annotated[UserInDB,Depends(get_current_active_user)]):
    return current_user









# Dummy route
@app.get('/error')
def error(q:int):
    if(q<18):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are under age"
    )  
    return {'perm':'Allowed'}


if __name__ == "__main__":
    uvicorn.run('code:app',reload=True)