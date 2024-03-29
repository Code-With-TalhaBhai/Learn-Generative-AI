#filename main.py

from fastapi import FastAPI, HTTPException, status, Depends
from typing import Annotated

development_db = ["DB for Development"]

def get_db_session():
    return development_db 

def func1():
    return 'func1'

def func2():
    return 'func2'

app = FastAPI(dependencies=[Depends(func1),Depends(func2)])

@app.get("/check")
def check():
    return {'fun':func1}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('multiple:app',reload=True)