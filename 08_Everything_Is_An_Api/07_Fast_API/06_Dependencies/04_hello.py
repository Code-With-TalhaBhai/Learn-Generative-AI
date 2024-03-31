from fastapi import FastAPI,Depends,Query,HTTPException,status
from typing import Annotated, Any


blogs = {
    "1": "Generative AI Blog",
    "2": "Deep Learning Blog",
    "3": "AI Vision Blog"
}

users = {
    "64": "Talha",
    "54": "Bhai"
}


class GetObjectOr404():
    def __init__(self,model)->None:
        self.model = model

    def __call__(self,id:str) -> Any:
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Object ID: {id} not found"
                )
        return obj


app = FastAPI(title="Learn Dependency Injection")


blog_dependency = GetObjectOr404(blogs)
@app.get('/find-blog/{id}')
def find_blog(blog:Annotated[str,Depends(blog_dependency)]):
    return blog


user_dependency = GetObjectOr404(users)
@app.get('/find-user/{id}')
def find_user(user:Annotated[str,Depends(user_dependency)]):
    return user



if __name__ == "__main__":
    import uvicorn
    uvicorn.run('04_hello:app',reload=True)