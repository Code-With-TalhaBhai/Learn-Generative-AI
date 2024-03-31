from fastapi import FastAPI,Depends,Query
from typing import Annotated

def dep_func1(num1:str=Query(None)):
    num1 = int(num1)
    num1 += 1
    print('func1 working')
    return num1


def dep_func2(num2:str=Query(None)):
    num2 = int(num2)
    num2 += 1
    print('func2 working')
    return num2


# Run dependency before every request work
app : FastAPI = FastAPI(dependencies=[Depends(dep_func1),Depends(dep_func2)])
# app : FastAPI = FastAPI()

# Run Dependency function only before this request
@app.get('/main/{num}') # localhost:8000/main/1?num1={some_number}&num2={some_number}
def main(num:int,number1:Annotated[int,Depends(dep_func1)],number2:Annotated[int,Depends(dep_func2)]):
    total = num + number1 + number2
    return f'The total is {total}'


@app.get('/sub/{num}') # localhost:8000/sub/1?num1={some_number}&num2={some_number}
def main(num:int):
    total = num
    return f'The total is {total}'


# Should give `num` parameter into query as it is the dependency added in `app` object
@app.get('/check') # localhost:8000/check?num1=324&num2=43
def check():
    return "check working"



if __name__ == "__main__":
    import uvicorn
    uvicorn.run('03_hello:app',reload=True)