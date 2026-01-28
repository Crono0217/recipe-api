#business logic 

from sqlalchemy.orm import Session
from app.models import Recipe
from app.schemas import RecipeUpdate

def create_recipe(db:Session, title:str, author_name:str, ingredients:str, cook_time:str):
    recipe = Recipe(title=title, author_name = author_name, ingredients = ingredients, cook_time = cook_time)
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe

def get_recipe(db:Session, recipe_id: int):
    """ shows a specific recipe by id """
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()

def get_recipes(db:Session):
    """ shows all the recipes """
    return db.query(Recipe).all()

def update_recipe(db:Session, recipe_id: int, updates: RecipeUpdate):
    """ Updates a recipe """
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()

    if not recipe:
        return None
    
    update_data = updates.model_dump(exclude_none=True)

    for field, value in update_data.items():
        setattr(recipe, field, value)

    db.commit()
    db.refresh(recipe)
    return recipe

def delete_recipe(db:Session, recipe_id: int):
    """ Deletes a recipe """

    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()

    if not recipe:
        return None
    
    db.delete(recipe)
    db.commit()
    return recipe