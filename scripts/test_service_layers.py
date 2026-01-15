from app.db import Session_Local
from app.services import create_recipe, get_recipe, get_recipes, update_recipe, delete_recipe

db = Session_Local()

recipe = create_recipe(db, title="Chicken Pasta", author_name= "Robert Pattison", ingredients="chicken, pasta, cheese", cook_time="3 hours")
print("success:", recipe)

one = get_recipe(db, recipe.id)
print("single recipe:", one)

all_recipes = get_recipes(db)
print("all recipes:", all_recipes)

updated = update_recipe(db, recipe.id, title="John Scott")
print("updated:", updated)

deleted = delete_recipe(db, recipe.id)
print("deleted:", deleted)

db.close()