from pydantic import BaseModel

class RecipeCreate(BaseModel):
    title:str
    author_name:str
    ingredients:str
    cook_time:str

class RecipeRead(BaseModel):
    id:int
    title:str
    author_name:str
    ingredients:str
    cook_time:str

class RecipeUpdate(BaseModel):
    title:str | None =  None
    author_name:str | None =  None
    ingredients:str | None =  None
    cook_time:str | None =  None
