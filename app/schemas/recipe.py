from pydantic import BaseModel, Field, field_validator

class RecipeCreate(BaseModel):
    title:str = Field(min_length=2, max_length=100)
    author_name:str = Field(min_length=2, max_length=100)
    ingredients:str = Field(min_length=1)
    cook_time:str

    @field_validator("cook_time")
    @classmethod

    def validate_cook_time(cls, v:str):
        if not v.strip():
            raise ValueError("cook_time can not be empty")
        return v

class RecipeRead(BaseModel):
    id:int
    title:str
    author_name:str
    ingredients:str
    cook_time:str

class RecipeUpdate(BaseModel):
    title:str | None = Field(default= None, min_length=2, max_length=100)
    author_name:str | None =  Field(default= None, min_length=2, max_length=100)
    ingredients:str | None =  Field(default= None, min_length=1)
    cook_time:str | None =  None

    @field_validator("cook_time")
    @classmethod

    def validate_cook_time(cls, v:str | None):
        if not v.strip():
            raise ValueError("cook_time can not be empty")
        return v