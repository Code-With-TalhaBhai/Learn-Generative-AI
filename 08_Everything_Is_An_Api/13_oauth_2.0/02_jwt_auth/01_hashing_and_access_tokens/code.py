from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
import uvicorn
from jose import jwt,JWTError
from typing import Annotated
from datetime import timedelta,datetime,timezone
from model import User,UserInDb,Token,TokenData
from data import fake_users_db as db
from passlib.context import CryptContext


app = FastAPI()
TOKEN_EXPIRES_MINUTES = timedelta(minutes=30)
ALGORITHM = "HS256"
# create secret-key from terminal by "openssl rand -hex 32"
SECRET_KEY = "f0eb2febcaf3cfd0d190a62504380acbc556dad3c2d6889ca60f4e97bf5b0bed"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pass_context = CryptContext(schemes=['bcrypt'],deprecated="auto") # We are using bcrypt password hash generator


def create_password_hash(password:str):
    return pass_context.hash(password)

def verify_password(plain_password:str,hashed_password:str):
    return pass_context.verify(plain_password,hashed_password)


def get_user(username:str):
    if username in db:
        user_record = db[username]
        return UserInDb(**user_record)


def authentic_user(username:str,password:str):
    user = db[username]

    if not user:
        return False
    if not verify_password(password,user['hashed_password']):
        return False
    return user


def create_access_token(data:dict,expires_time:timedelta | None=None):
    payload = data.copy()
    if expires_time:
        expire = datetime.now(timezone.utc) + expires_time
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    payload.update({"exp":expire})
    encoded_jwt = jwt.encode(claims=payload,key=SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt



async def get_current_user(token:Annotated[str,Depends(oauth2_scheme)]):
    payload = jwt.decode(token=token,key=SECRET_KEY,algorithms=ALGORITHM)
    print('payload is: ',payload)
    credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Some Authentication issues"
        )
    
    username = payload.get('sub')
    try:
        if username is None:
            print('Username not found in payload')
            credentials_exception()
    except JWTError:
        print("Wrong bearer token")
        credentials_exception()
    
    user = get_user(username)
    if user is None:
        print("User not found in DB")
        credentials_exception()
    return user
    



async def get_current_active_user(current_user:Annotated[User,Depends(get_current_user)]):
    if current_user.disabled == True:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is not currently active"
        )
    return current_user


@app.post('/login')
def login_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()]):
    user = authentic_user(form_data.username,form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User has not signed up",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = TOKEN_EXPIRES_MINUTES
# Pre-defined payloads(https://datatracker.ietf.org/doc/html/rfc7519#section-4.1)
    access_token = create_access_token(data={"sub":user['username']},expires_time=access_token_expires)
    return Token(access_token=access_token,token_type='bearer')


@app.get('/my-items')
def items(my:Annotated[User,Depends(get_current_active_user)]):
    return {"model":"GTR","Year":2025,"owner":my.username}


if __name__ == "__main__":
    uvicorn.run('code:app',reload=True)