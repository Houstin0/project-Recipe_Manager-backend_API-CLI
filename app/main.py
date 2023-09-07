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
     

     
if __name__=='__main__':
    cli()    
