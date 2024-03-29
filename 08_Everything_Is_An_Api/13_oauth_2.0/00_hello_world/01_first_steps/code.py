
import uvicorn
from fastapi import FastAPI,Depends
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from typing import Annotated


app = FastAPI()

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")


@app.get('/')
def index(token:Annotated[str, Depends(oauth2_schema)]):
    return {"token":token} # Here, token is undefined as fastapi doesn't handle itself, rather you can use library as (JWT) or (OAUTH) to handle it(Not completely true)


@app.post('/token')
async def token(form_data: OAuth2PasswordRequestForm=Depends()):
    return {'acc_token': f'my token name is {form_data.username}'}


if __name__ == "__main__":
    uvicorn.run('code:app',reload=True)