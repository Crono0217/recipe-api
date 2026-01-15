#business logic 

from sqlalchemy.orm import Session
from app.models import Recipe

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

def update_recipe(db:Session, recipe_id: int, title:str | None = None, author_name: str | None = None, ingredients: str | None = None, cook_time: str | None = None):
    """ Updates a recipe """
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()

    if not recipe:
        return None
    
    if title is not None:
        recipe.title = title
    if author_name is not None:
        recipe.author_name = author_name
    if ingredients is not None:
        recipe.ingredients = ingredients
    if cook_time is not None:
        recipe.cook_time = cook_time

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