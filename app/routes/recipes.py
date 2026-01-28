#URLs and HTTP status codes
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import Session_Local
from app.services import create_recipe, get_recipe,get_recipes, update_recipe, delete_recipe
from app.schemas import RecipeUpdate

router = APIRouter()

def get_db_session():
    db =  Session_Local()
    try:
        yield db
    finally:
        db.close()

#create route
@router.post("/recipes")
def route_create_recipe(title: str, 
                        author_name:str, 
                        ingredients:str, 
                        cook_time:str, 
                        db: Session = Depends(get_db_session)):
    return create_recipe(db, title, author_name, ingredients, cook_time)

#read route
@router.get("/recipe/{recipe_id}")
def route_get_recipe(recipe_id: int, 
                     db: Session =  Depends(get_db_session)):
    return get_recipe(db, recipe_id)
#read all route
@router.get("/recipes")
def route_get_recipes(db:Session = Depends(get_db_session)):
    return get_recipes(db)

#update route
@router.patch("/recipe/{recipe_id}")
def route_update_recipe(recipe_id: int, 
                        recipe: RecipeUpdate,
                        db: Session = Depends(get_db_session)):
    return update_recipe(db, recipe_id, recipe)
    
#delete route
@router.delete("/recipe/{recipe_id}")
def route_delete_recipe(recipe_id: int, 
                        db: Session = Depends(get_db_session)):
    return delete_recipe(db, recipe_id)