from sqlmodel import SQLModel,Field



class Todo(SQLModel,table=True):
    id: int | None = Field(default=None,primary_key=True)
    title: str = Field(index=True)
    description: str
    author: str | None = Field(default=None)