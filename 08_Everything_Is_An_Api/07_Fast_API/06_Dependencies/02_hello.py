from fastapi import FastAPI,Depends,Query
from typing import Annotated


app : FastAPI = FastAPI()


def dep_check(name:str=Query(None),password:str=Query(None)):
    if not name:
        raise


@app.get('/login',dependencies=[Depends(dep_check)])
def login():
    return True


# @app.get('/login')
# def login(user:Annotated[str,Depends(dep_check)]):
#     return True


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('02_hello:app',reload=True)