from fastapi import FastAPI,Body
import uvicorn


app = FastAPI()

# GET request
@app.get('/')
def index():
    return {"msg":"hello world"}


# POST request -> Body 
@app.post('/bye')
def body_index(person=Body(embed=True)): # Body(embed=True) is used in POST request for json body
    return {'greet':f'{person}, says bye'}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="hello:app",reload=True)