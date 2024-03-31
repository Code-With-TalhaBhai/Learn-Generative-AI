from fastapi import FastAPI,Depends,Query
from typing import Annotated


app : FastAPI = FastAPI()


# Custom login function
def custom_login(username:str,password:str):
    if username == "admin" and password == "admin":
        return {"message": "Login Successfully"}
    else:
        return {"message": "Login Failed"}
    


@app.get('/custom-login')
def cust_login(username,password):
    result  = custom_login(username,password)
    return result


# Creating Dependeny function
def dep_login(username:str = Query(None),password:str=Query(None)):
# def dep_login(username:str,password:str):
    if username == "admin" and password == "admin":
        return {"message": "Login Successfully"}
    else:
        return {"message": "Login Failed"}


@app.get('/dep-login')
def login(user:Annotated[str,Depends(dep_login)]):
    return user


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('01_hello:app',reload=True)