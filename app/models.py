from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine('sqlite:///meals.db')
Session=sessionmaker(bind=engine)
session=Session()

Base=declarative_base() 

class Recipe(Base):
    __tablename__='recipes'

    id=Column(Integer(),primary_key=True)
    name=Column(String())
    category=Column(String())
    instructions=Column(String())

    def __repr__(self):
        return f"Recipe: {self.name} , Category: {self.category} , Instructions: {self.instructions}"

class Ingredient(Base):
    __tablename__='ingredients'

    id=Column(Integer(),primary_key=True)
    name=Column(String())

    def __repr__(self):
        return   f"Ingredient: {self.name} "  
    
class Meal_plan(Base):
    __tablename__='meal_plans'

    id=Column(Integer,primary_key=True)
    day=Column(String())

    def __repr__(self):
        return f"Day : {self.day}"

