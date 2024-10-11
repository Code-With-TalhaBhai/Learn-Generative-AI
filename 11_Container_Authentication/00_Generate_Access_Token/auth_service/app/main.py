from fastapi import FastAPI
from jose import jwt,JWTError
from datetime import timedelta,datetime


ALGORITHM = "HS256"
SECRET_KEY = "This is really secret"
app = FastAPI()


def create_access_token(subject:str,expires_delta: timedelta):
    expire_time = datetime.now() + expires_delta
    encoded_jwt = jwt.encode({"exp":expire_time,"sub":subject,"email":"talhakhalid411@gmail.com"},key=SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token:str):
    decoded_jwt = jwt.decode(token,key=SECRET_KEY,algorithms=ALGORITHM)
    return decoded_jwt

@app.get('/')
def home():
    return {"res":"This is home page"}


@app.get('/new-route')
def get_new_route(username:str):
    
    token_expiry_time = timedelta(minutes=1)
    access_token = create_access_token(username,token_expiry_time)
    return {"access_token":access_token}


@app.get('/decode-token')
def decode_token(access_token):

    try:
        decoded_token = decode_access_token(access_token)
        print(decoded_token)
        return {"decoded_token":decoded_token}
    except JWTError as e:
        return {"error":str(e)}


