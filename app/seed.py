from models import *
from faker import Faker
import random

fake=Faker()

if __name__=='__main__':
    session.query(Recipe).delete()
    session.query(Ingredient).delete()
    session.commit()
    print('seeding......')

    recipes=[]
    for i in range (10):
        recipe=Recipe(
            name=fake.name(),
            category=fake.name(),
            instructions=fake.sentence()
        )
        session.add(recipe)
        session.commit()
        recipes.append(recipe)

    ingredients=[]
    for recipe in recipes:
        for i in range(random.randint(1,10)):
            ingredient=Ingredient(
                name=fake.text(),
                recipe_id=recipe.id
            )   
            session.add(ingredient)
            session.commit()
            ingredients.append(ingredient)  
    session.bulk_save_objects(ingredients) 
    session.commit()
    session.close()       

    # meal_plans=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]    