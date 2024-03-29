from fastapi import FastAPI,Depends
from fastapi.security import OAuth2PasswordBearer
import uvicorn
from typing import Annotated
from model import User


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_user(token):
    return User(username=token+" fake-user",email="talha@talha.com",full_name="Talha Bhai")


async def get_current_user(token:Annotated[str,Depends(oauth2_scheme)]):
    user = fake_user(token)
    return user


@app.get('/')
def index():
    return {'me':'thinking'}



@app.get('/user')
async def user(current_user:Annotated[str,Depends(get_current_user)]):
    return current_user


if __name__ == "__main__":
    uvicorn.run('code:app',reload=True)