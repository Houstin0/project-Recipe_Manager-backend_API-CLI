from models import *
from faker import Faker

fake=Faker()

if __name__=='__main__':
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
    for i in range(10):
        ingredient=Ingredient(
            name=fake.name()
        )  
        session.add(ingredient)
        session.commit()
        ingredients.append(ingredient)  

    meal_plans=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]    