from models import *
import click

@click.group()
def cli():
    pass

@click.command() 
@click.option('--name',prompt="Recipe Name",help="number of greetings")   
@click.option('--category',prompt="Recipe category",help="number of greetings")   
@click.option('--time_taken',prompt="Time Taken",help="number of greetings")   
@click.option('--instructions',prompt="Recipe Instructions",help="number of greetings")   
def add_recipe(name,category,time_taken,instructions):
        """Function to add an Recipe by name"""
        recipe=Recipe(
        name=name,
        category=category,
        time_taken=time_taken,
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
     """Function to add a Meal plan by name"""
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
     """Function to add an ingredient"""
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
     """Function to delete a Recipe by name"""
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
    """Function to delete a Meal Plan by name"""
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
    """Function to delete an ingredient by name"""

    ingredient = session.query(Ingredient).filter(Ingredient.name == ingredient_name).first()

    if not ingredient:
        click.echo(f"Ingredient '{ingredient_name}' not found.")
        return
    
    session.delete(ingredient)
    session.commit()
    click.echo(f"Deleted {ingredient_name} from Ingredients") 
cli.add_command(delete_ingredient)  

@click.command()
@click.option('--recipe_name', prompt="Recipe Name to Search", help="Recipe name to search for")
def search_recipe(recipe_name):
    """Function to search for recipes by name"""

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
    """Function to search for meal plans by name"""
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
    """Function to search for ingredients by name"""
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
        click.echo(f"  Time Taken: {recipe.time_taken}")
        click.echo(f"  Instructions: {recipe.instructions}")
        click.echo()
cli.add_command(all_recipes)

@click.command()
def all_meal_plans():
    """Function display all meal plans"""

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
    """Function to display all ingredients"""

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
@click.option('--recipe_name', prompt="Recipe Name to Update", help="Recipe name to update")
@click.option('--column', prompt="Column to Update (name, category, time_taken, instructions)", help="Column to update")
@click.option('--new_value', prompt="New Value", help="New value for the column")
def update_recipe_column(recipe_name, column, new_value):
    """Function to update a specific column of a recipe by name"""

    recipe = session.query(Recipe).filter(Recipe.name == recipe_name).first()

    if not recipe:
        click.echo(f"Recipe '{recipe_name}' not found.")
        return

    # Update the specified column with the new value
    if column == 'name':
        recipe.name = new_value
    elif column == 'category':
        recipe.category = new_value
    elif column == 'time_taken':
        recipe.time_taken = new_value
    elif column == 'instructions':
        recipe.instructions = new_value
    else:
        click.echo("Invalid column name. Available columns: name, category, time_taken, instructions.")
        return

    session.commit()
    click.echo(f"Updated {column} of recipe '{recipe_name}'")
cli.add_command(update_recipe_column)    

@click.command()
@click.option('--meal_plan_name', prompt="Meal Plan Name to Update", help="Meal plan name to update")
@click.option('--column', prompt="Column to Update (name, start_date, end)", help="Column to update")
@click.option('--new_value', prompt="New Value", help="New value for the column")
def update_meal_plan_column(meal_plan_name, column, new_value):
    """Function to update a specific column of a meal plan by name"""

    meal_plan = session.query(Meal_plan).filter(Meal_plan.name == meal_plan_name).first()

    if not meal_plan:
        click.echo(f"Meal plan '{meal_plan_name}' not found.")
        return

    # Update the specified column with the new value
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
    """Function to update a specific column of an ingredient by name"""
    ingredient = session.query(Ingredient).filter(Ingredient.name == ingredient_name).first()

    if not ingredient:
        click.echo(f"Ingredient '{ingredient_name}' not found.")
        return

    # Update the specified column with the new value
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

     
if __name__=='__main__':
    cli()    
