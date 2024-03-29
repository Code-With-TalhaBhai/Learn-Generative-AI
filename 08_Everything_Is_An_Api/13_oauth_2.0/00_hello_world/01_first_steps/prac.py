import uvicorn
from fastapi import FastAPI,Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated


app = FastAPI()

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")


@app.get('/')
def index():
    return {'Msg':"Hello, Sorld"}

# @app.get('/next')
# def ind():
#     return {'Msg':"Hello, Sorld"}



@app.get('/profile')
async def profile(token:Annotated[str,Depends(oauth2_schema)]):
    return {"token":token}

if __name__ == "__main__":
    uvicorn.run('prac:app',reload=True)