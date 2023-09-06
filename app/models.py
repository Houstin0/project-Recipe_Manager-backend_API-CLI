from sqlalchemy import Column,Integer,String,ForeignKey,desc
from base import Base,session

class Recipe(Base):
    __tablename__='recipes'

    id=Column(Integer(),primary_key=True)
    name=Column(String())
    category=Column(String())
    instructions=Column(String())

    def __repr__(self):
        return f"Recipe: {self.name} , Category: {self.category} , Instructions: {self.instructions}"
    