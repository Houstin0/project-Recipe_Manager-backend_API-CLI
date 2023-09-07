from models import *

reci=session.query(Recipe.ingredients).first()
print(reci)