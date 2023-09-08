from models.models import *
from database.database import session
from sqlalchemy import func
import click

@click.group()
def cli():
    pass

@click.command() 
@click.option('--name',prompt="Recipe Name")   
@click.option('--category',prompt="Recipe category")   
@click.option('--time_in_minutes',prompt="Time Taken in minutes")   
@click.option('--instructions',prompt="Recipe Instructions")   
def add_recipe(name,category,time_in_minutes,instructions):
        """Add an new Recipe"""

        recipe=Recipe(
        name=name,
        category=category,
        time_in_minutes=time_in_minutes,
        instructions=instructions  
        )
        session.add(recipe)
        session.commit()
        click.echo(f"Added {name} to Recipes")
cli.add_command(add_recipe)        

@click.command()
@click.option('--name',prompt="Meal Plan Name",help="number of greetings")   
@click.option('--start_date',prompt="Meal Plan start date",help="number of greetings")   
@click.option('--end',prompt="Meal Plan end date",help="number of greetings")   
def add_meal_plan(name,start_date,end):
     """Add a new Meal plan """

     meal_plan=Meal_plan(
          name=name,
          start_date=start_date,
          end=end
     )
     session.add(meal_plan)
     session.commit()
     click.echo(f"Added {name} to Meal plan")
cli.add_command(add_meal_plan)   

@click.command()
@click.option('--ingredient_name',prompt="Ingredient Name",help="number of greetings")  
@click.option('--recipe_name',prompt="Recipe Name",help="number of greetings")  
@click.option('--meal_plan_name',prompt="Meal Plan Name",help="number of greetings")  
def add_ingredient(ingredient_name,recipe_name,meal_plan_name):
     """Add an new ingredient"""
     
     recipe_obj=session.query(Recipe.id).filter(Recipe.name==recipe_name).first()
     meal_plan_obj=session.query(Meal_plan.id).filter(Meal_plan.name==meal_plan_name).first()
     
     if not recipe_obj:
          click.echo(f"Recipe '{recipe_name}' not found")
          return
     if not meal_plan_obj:
          click.echo(f"Meal Plan '{meal_plan_name}' not found")
          return
               
     ingredient=Ingredient(
          name=ingredient_name,
          recipe_id=recipe_obj.id,
          meal_plan_id=meal_plan_obj.id
     )
     session.add(ingredient)
     session.commit()
     click.echo(f"Added {ingredient_name} to Ingredients")
cli.add_command(add_ingredient)


@click.command()
@click.option('--recipe_name',prompt="Recipe Name to Delete")
def delete_recipe(recipe_name):
     """Delete a Recipe by name"""
     recipe_to_delete=session.query(Recipe).filter(Recipe.name==recipe_name).first()

     if not recipe_to_delete:
          click.echo(f"Recipe '{recipe_name}' not found.")
          return
     session.delete(recipe_to_delete)
     session.commit()
     click.echo(f"Deleted {recipe_name} from Recipes")
cli.add_command(delete_recipe)    

@click.command()
@click.option('--meal_plan_name', prompt="Meal Plan Name to Delete", help="Meal plan name to delete")
def delete_meal_plan(meal_plan_name):
    """Delete a Meal Plan by name"""
    meal_plan = session.query(Meal_plan).filter(Meal_plan.name == meal_plan_name).first()

    if not meal_plan:
        click.echo(f"Meal plan '{meal_plan_name}' not found.")
        return

    session.delete(meal_plan)
    session.commit()
    click.echo(f"Deleted {meal_plan_name} from Meal plans")
cli.add_command(delete_meal_plan)    
     
@click.command()
@click.option('--ingredient_name', prompt="Ingredient Name to Delete", help="Ingredient name to delete")
def delete_ingredient(ingredient_name):
    """Delete an ingredient by name"""

    ingredient = session.query(Ingredient).filter(Ingredient.name == ingredient_name).first()

    if not ingredient:
        click.echo(f"Ingredient '{ingredient_name}' not found.")
        return
    
    session.delete(ingredient)
    session.commit()
    click.echo(f"Deleted {ingredient_name} from Ingredients") 
cli.add_command(delete_ingredient) 

@click.command()
def delete_all_meal_plans():
    """deletes all from Meal Plans table"""
    session.query(Meal_plan).delete()
    session.commit()
    click.echo("Deleted all records from the Meal Plans table.")
cli.add_command(delete_all_meal_plans)


@click.command()
@click.option('--recipe_name', prompt="Recipe Name to Update", help="Recipe name to update")
@click.option('--column', prompt="Column to Update (name, category, time_in_minutes, instructions)", help="Column to update")
@click.option('--new_value', prompt="New Value", help="New value for the column")
def update_recipe_column(recipe_name, column, new_value):
    """Update a column of a recipe"""

    recipe = session.query(Recipe).filter(Recipe.name == recipe_name).first()

    if not recipe:
        click.echo(f"Recipe '{recipe_name}' not found.")
        return

    if column == 'name':
        recipe.name = new_value
    elif column == 'category':
        recipe.category = new_value
    elif column == 'time_in_minutes':
        recipe.time_in_minutes = new_value
    elif column == 'instructions':
        recipe.instructions = new_value
    else:
        click.echo("Invalid column name. Available columns: name, category, time_in_minutes, instructions.")
        return

    session.commit()
    click.echo(f"Updated {column} of recipe '{recipe_name}'")
cli.add_command(update_recipe_column)    

@click.command()
@click.option('--meal_plan_name', prompt="Name of Meal Plan to Update", help="Meal plan name to update")
@click.option('--column', prompt="Column to Update (name, start_date, end)", help="Column to update")
@click.option('--new_value', prompt="New Value", help="New value for the column")
def update_meal_plan_column(meal_plan_name, column, new_value):
    """Update a column of a meal plan"""

    meal_plan = session.query(Meal_plan).filter(Meal_plan.name == meal_plan_name).first()

    if not meal_plan:
        click.echo(f"Meal plan '{meal_plan_name}' not found.")
        return

    if column == 'name':
        meal_plan.name = new_value
    elif column == 'start_date':
        meal_plan.start_date = new_value
    elif column == 'end':
        meal_plan.end = new_value
    else:
        click.echo("Invalid column name. Available columns: name, start_date, end.")
        return

    session.commit()
    click.echo(f"Updated {column} of meal plan '{meal_plan_name}'")
cli.add_command(update_meal_plan_column)  

@click.command()
@click.option('--ingredient_name', prompt="Ingredient Name to Update", help="Ingredient name to update")
@click.option('--column', prompt="Column to Update (name, recipe, meal_plan)", help="Column to update")
@click.option('--new_value', prompt="New Value", help="New value for the column")
def update_ingredient_column(ingredient_name, column, new_value):
    """Update a column of an ingredient"""

    ingredient = session.query(Ingredient).filter(Ingredient.name == ingredient_name).first()

    if not ingredient:
        click.echo(f"Ingredient '{ingredient_name}' not found.")
        return

    if column == 'name':
        ingredient.name = new_value
    elif column == 'recipe':
        recipe = session.query(Recipe).filter(Recipe.name == new_value).first()
        if not recipe:
            click.echo(f"Recipe '{new_value}' not found.")
            return
        ingredient.recipe_id = recipe.id
    elif column == 'meal_plan':
        meal_plan = session.query(Meal_plan).filter(Meal_plan.name == new_value).first()
        if not meal_plan:
            click.echo(f"Meal plan '{new_value}' not found.")
            return
        ingredient.meal_plan_id = meal_plan.id
    else:
        click.echo("Invalid column name. Available columns: name, recipe, meal_plan.")
        return

    session.commit()
    click.echo(f"Updated {column} of ingredient '{ingredient_name}'")
cli.add_command(update_ingredient_column)



@click.command()
@click.option('--recipe_name', prompt="Recipe Name to Search", help="Recipe name to search for")
def search_recipe(recipe_name):
    """search for recipes by name"""

    recipes = session.query(Recipe).filter(Recipe.name.ilike(f"%{recipe_name}%")).all()

    if not recipes:
        click.echo(f"No recipes found matching '{recipe_name}'.")
        return

    click.echo("Matching Recipes:")
    for recipe in recipes:
        click.echo(f"- {recipe}")
cli.add_command(search_recipe)

@click.command()
@click.option('--meal_plan_name', prompt="Meal Plan Name to Search", help="Meal plan name to search for")
def search_meal_plan(meal_plan_name):
    """search for meal plans by name"""

    meal_plans = session.query(Meal_plan).filter(Meal_plan.name.ilike(f"%{meal_plan_name}%")).all()

    if not meal_plans:
        click.echo(f"No meal plans found matching '{meal_plan_name}'.")
        return

    click.echo("Matching Meal Plans:")
    for meal_plan in meal_plans:
        click.echo(f"- {meal_plan.name}")
cli.add_command(search_meal_plan)

@click.command()
@click.option('--ingredient_name', prompt="Ingredient Name to Search", help="Ingredient name to search for")
def search_ingredient(ingredient_name):
    """search for ingredients by name"""

    ingredients = session.query(Ingredient).filter(Ingredient.name.ilike(f"%{ingredient_name}%")).all()

    if not ingredients:
        click.echo(f"No ingredients found matching '{ingredient_name}'.")
        return

    click.echo("Matching Ingredients:")
    for ingredient in ingredients:
        click.echo(f"- {ingredient.name}")
cli.add_command(search_ingredient)  

@click.command()
def all_recipes():
    """Function display all recipes"""
    recipes = session.query(Recipe).all()

    if not recipes:
        click.echo("No recipes found.")
        return

    click.echo("Recipes:")
    for recipe in recipes:
        click.echo(f"- Name: {recipe.name}")
        click.echo(f"  Category: {recipe.category}")
        click.echo(f"  Time Taken: {recipe.time_in_minutes}")
        click.echo(f"  Instructions: {recipe.instructions}")
        click.echo()
cli.add_command(all_recipes)

@click.command()
def all_meal_plans():
    """display all meal plans"""

    meal_plans = session.query(Meal_plan).all()

    if not meal_plans:
        click.echo("No meal plans found.")
        return

    click.echo("Meal Plans:")
    for meal_plan in meal_plans:
        click.echo(f"- Name: {meal_plan.name}")
        click.echo(f"  Start Date: {meal_plan.start_date}")
        click.echo(f"  End Date: {meal_plan.end}")
        click.echo()   
cli.add_command(all_meal_plans)       

@click.command()
def all_ingredients():
    """display all ingredients"""

    ingredients = session.query(Ingredient).all()

    if not ingredients:
        click.echo("No ingredients found.")
        return

    click.echo("Ingredients:")
    for ingredient in ingredients:
        click.echo(f"- Name: {ingredient.name}")
        click.echo(f"  Recipe: {ingredient.recipe.name if ingredient.recipe else 'N/A'}")
        click.echo(f"  Meal Plan: {ingredient.meal_plan.name if ingredient.meal_plan else 'N/A'}")
        click.echo()
cli.add_command(all_ingredients)




@click.command()
@click.option('--category', prompt="Recipe Category to Retrieve", help="Recipe category to retrieve")
def recipes_by_category(category):
    """get recipes by category"""
    recipes = session.query(Recipe).filter(Recipe.category.ilike(f"%{category}%")).all()

    if not recipes:
        click.echo(f"No recipes found in the '{category}' category.")
        return

    click.echo(f"Recipes in the '{category}' category:")
    for recipe in recipes:
        click.echo(f"- Name: {recipe.name}")
        click.echo(f"  Category: {recipe.category}")
        click.echo(f"  Time Taken: {recipe.time_in_minutes}")
        click.echo(f"  Instructions: {recipe.instructions}")
        click.echo()

cli.add_command(recipes_by_category)


@click.command()
@click.option('--start_date', prompt="Meal Plan Start Date to Retrieve", help="Meal plan start date to retrieve")
def meal_plans_by_start_date(start_date):
    """get meal plans by start date"""
    meal_plans = session.query(Meal_plan).filter(Meal_plan.start_date == start_date).all()

    if not meal_plans:
        click.echo(f"No meal plans found with the start date '{start_date}'.")
        return

    click.echo(f"Meal plans with start date '{start_date}':")
    for meal_plan in meal_plans:
        click.echo(f"- Name: {meal_plan.name}")
        click.echo(f"  Start Date: {meal_plan.start_date}")
        click.echo(f"  End Date: {meal_plan.end}")
        click.echo()
cli.add_command(meal_plans_by_start_date)
 
@click.command()
@click.option('--recipe_name', prompt="Recipe Name to Retrieve Ingredients From", help="Recipe name to retrieve ingredients from")
def ingredients_by_recipe(recipe_name):
    """get ingredients by recipe name"""

    recipe = session.query(Recipe).filter(Recipe.name == recipe_name).first()

    if not recipe:
        click.echo(f"Recipe '{recipe_name}' not found.")
        return

    
    ingredients = session.query(Ingredient).filter(Ingredient.recipe_id == recipe.id).all()

    if not ingredients:
        click.echo(f"No ingredients found for recipe '{recipe_name}'.")
        return

    click.echo(f"Ingredients for recipe '{recipe_name}':")
    for ingredient in ingredients:
        click.echo(f"- Name: {ingredient.name}")
        click.echo(f"  Meal Plan: {ingredient.meal_plan.name if ingredient.meal_plan else 'N/A'}")
        click.echo()
cli.add_command(ingredients_by_recipe)
 
@click.command()
@click.option('--meal_plan_name', prompt="Meal Plan Name to Retrieve Ingredients From", help="Meal plan name to retrieve ingredients from")
def ingredients_by_meal_plan(meal_plan_name):
    """get ingredients by meal plan name"""

   
    meal_plan = session.query(Meal_plan).filter(Meal_plan.name == meal_plan_name).first()

    if not meal_plan:
        click.echo(f"Meal plan '{meal_plan_name}' not found.")
        return

  
    ingredients = session.query(Ingredient).filter(Ingredient.meal_plan_id == meal_plan.id).all()

    if not ingredients:
        click.echo(f"No ingredients found for meal plan '{meal_plan_name}'.")
        return

    click.echo(f"Ingredients for meal plan '{meal_plan_name}':")
    for ingredient in ingredients:
        click.echo(f"- Name: {ingredient.name}")
        click.echo(f"  Recipe: {ingredient.recipe.name if ingredient.recipe else 'N/A'}")
        click.echo()
cli.add_command(ingredients_by_meal_plan)

@click.command()
@click.option('--meal_plan_name', prompt="Meal Plan Name to Retrieve Recipes From", help="Meal plan name to retrieve recipes from")
def recipes_by_meal_plan(meal_plan_name):
    """get recipes by meal plan name"""
    meal_plan = session.query(Meal_plan).filter(Meal_plan.name == meal_plan_name).first()

    if not meal_plan:
        click.echo(f"Meal plan '{meal_plan_name}' not found.")
        return

    recipes = session.query(Recipe).join(Ingredient).filter(Ingredient.meal_plan_id == meal_plan.id).all()

    if not recipes:
        click.echo(f"No recipes found for meal plan '{meal_plan_name}'.")
        return

    click.echo(f"Recipes for meal plan '{meal_plan_name}':")
    for recipe in recipes:
        click.echo(f"- Name: {recipe.name}")
        click.echo(f"  Category: {recipe.category}")
        click.echo(f"  Time Taken: {recipe.time_in_minutes}")
        click.echo(f"  Instructions: {recipe.instructions}")
        click.echo()
cli.add_command(recipes_by_meal_plan)

@click.command()
@click.option('--meal_plan_name', prompt="Meal Plan Name", help="Meal plan name")
@click.option('--recipe_category', prompt="Recipe Category", help="Recipe category")
def recipes_by_meal_plan__category(meal_plan_name, recipe_category):
    """get recipes by meal plan and category"""
    meal_plan = session.query(Meal_plan).filter(Meal_plan.name == meal_plan_name).first()

    if not meal_plan:
        click.echo(f"Meal plan '{meal_plan_name}' not found.")
        return

    recipes = session.query(Recipe).join(Ingredient).filter(
        Ingredient.meal_plan_id == meal_plan.id,
        Recipe.category.ilike(f"%{recipe_category}%")
    ).all()

    if not recipes:
        click.echo(f"No recipes found for meal plan '{meal_plan_name}' and category '{recipe_category}'.")
        return

    click.echo(f"Recipes for meal plan '{meal_plan_name}' in category '{recipe_category}':")
    for recipe in recipes:
        click.echo(f"- Name: {recipe.name}")
        click.echo(f"  Category: {recipe.category}")
        click.echo(f"  Time Taken: {recipe.time_in_minutes}")
        click.echo(f"  Instructions: {recipe.instructions}")
        click.echo()
cli.add_command(recipes_by_meal_plan__category)

@click.command()
@click.option('--ingredients', prompt="List of Ingredients", help="Comma-separated list of ingredients")
def recipes_by_ingredients(ingredients):
    """get recipes by ingredients"""
    ingredient_list = [ingredient.strip() for ingredient in ingredients.split(',')]
    
    recipes = (
        session.query(Recipe)
        .join(Ingredient, Ingredient.recipe_id == Recipe.id)
        .filter(Ingredient.name.in_(ingredient_list))
        .group_by(Recipe.id)
        .having(func.count(Ingredient.id) == len(ingredient_list))
        .all()
    )

    if not recipes:
        click.echo(f"No recipes found with the provided ingredients: {', '.join(ingredient_list)}")
        return

    click.echo(f"Recipes with ingredients: {', '.join(ingredient_list)}")
    for recipe in recipes:
        click.echo(f"- Name: {recipe.name}")
        click.echo(f"  Category: {recipe.category}")
        click.echo(f"  Time Taken: {recipe.time_in_minutes}")
        click.echo(f"  Instructions: {recipe.instructions}")
        click.echo()
cli.add_command(recipes_by_ingredients)

@click.command()
@click.option('--recipe_category', prompt="Recipe Category", help="Recipe category")
@click.option('--meal_plan_name', prompt="Meal Plan Name", help="Meal plan name")
def ingredients_by_category__meal_plan(recipe_category, meal_plan_name):
    """get ingredients by recipe category and meal plan name"""
    meal_plan = session.query(Meal_plan).filter(Meal_plan.name == meal_plan_name).first()

    if not meal_plan:
        click.echo(f"Meal plan '{meal_plan_name}' not found.")
        return

    ingredients = (
        session.query(Ingredient)
        .join(Recipe, Recipe.id == Ingredient.recipe_id)
        .filter(Recipe.category.ilike(f"%{recipe_category}%"))
        .filter(Ingredient.meal_plan_id == meal_plan.id)
        .all()
    )

    if not ingredients:
        click.echo(f"No ingredients found for recipe category '{recipe_category}' and meal plan '{meal_plan_name}'.")
        return

    click.echo(f"Ingredients for recipe category '{recipe_category}' and meal plan '{meal_plan_name}':")
    for ingredient in ingredients:
        click.echo(f"- Name: {ingredient.name}")
        click.echo(f"  Recipe: {ingredient.recipe.name if ingredient.recipe else 'N/A'}")
        click.echo()
cli.add_command(ingredients_by_category__meal_plan)

if __name__=='__main__':
    cli()    