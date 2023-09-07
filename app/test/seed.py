#!/usr/bin/env python3

from models.models import *
from database.database import session
from faker import Faker
import random

if __name__=='__main__':
    session.query(Recipe).delete()
    session.query(Ingredient).delete()
    session.query(Meal_plan).delete()
    session.commit()
    print('seeding......')

    fake=Faker()

    recipe_names["Amish Breakfast Casserole","Creamy White Chili",
                 "Banana Bread","Cheeseburger Soup","Chicken Potpie",
                 "Chicken Fajitas","Apple Pie","Basic Homemade Bread"]
    category

    recipes=[]
    for i in range (10):
        recipe=Recipe(
            name=fake.name(),
            category=fake.name(),
            instructions=fake.sentence(),
            time_taken=fake.pyint()
        )
        session.add(recipe)
        session.commit()
        recipes.append(recipe)
   

    meal_plans=[] 
    for i in range(7):
        meal_plan=Meal_plan(
            name=fake.name(),
            start_date=fake.date_of_birth(),
            end=fake.date_of_birth()
        )
        session.add(meal_plan)
        session.commit()
        meal_plans.append(meal_plan)
    
    

    ingredients=[]
    for recipe in recipes:
        for i in range(random.randint(1,10)):
            meal_plan=random.choice(meal_plans)
            ingredient=Ingredient(
                name=fake.company(),
                recipe_id=recipe.id,
                meal_plan_id=meal_plan.id
            )   
            session.add(ingredient)
            session.commit()
            ingredients.append(ingredient)  
    session.bulk_save_objects(ingredients) 
    session.commit()
    session.close()       

  
