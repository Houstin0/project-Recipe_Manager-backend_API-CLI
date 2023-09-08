# Recipe_Manager_and_Meal_Planner_CLI
 
 **Recipe Manager and Meal Planner CLI** is a command-line application designed to help you organize your recipes and plan for meals. With this tool, you can store, categorize, search for recipes, plan meals, and even generate shopping lists based on your meal plans. Whether you're a culinary enthusiast or just trying to simplify your meal planning, this CLI app has you covered.

 ## Installation
1. Clone the repository to your local machine using git clone.
2. Navigate to the repository's directory.
3. Create pipenv environment and Install dependencies using pipenv install
4. Activate environment using pipenv shell
5. Navigate into the app directory using cd app/
6. Run the Application using python main.py

## Tables
- Recipes
- Meal_plans
- Ingredients

## Packages used
- sqlalchemy
- alembic
- click
- faker

## Usage and features
Getting Started:
- Launch the application using python main.py.
- Run commands with python main.py <command>
###Commands

1. Add ingredient:
- Adds an ingredient to the ingredients table.

2. Add meal plan:
- Adds a meal plan to the meal plans table.

3. Add recipe:
- Adds a recipe to the recipes table.

4. All ingredients:
- Displays a list of all ingredients in the ingredients table.

5. All meal plans:
- Displays a list of all meal plans in the meal plans table.

6. All recipes:
- Displays a list of all recipes in the recipes table.

7. Delete all meal plans:
- Delets all meal plans.

8. Delete ingredient:
- Deletes an ingrefient.

9. Delete recipe:
- Delets a recipe.

10. Ingredient by category and meal plan:
- Displays a list of ingredients that can be used as a shopping list.

11. Ingredient by meal plan:
- Displays a list of all ingredients for the specified meal plan.

12. Ingredients by recipe:
- Displays a list of all ingredients for the specified recipe.

13. meal plans by start date:
- Displays a list of meal plans for the specified start date.

14. Recipes by category:
- Displays a list of recipe belonging to a specified category(breakfast,lunch,dinner,dessert).

15. Recipes by ingrendients:
- Displays a list of recipe belonging to specified ingredients.

16. Recipes by meal plan:
- Displays a list of recipe belonging to a specified meal plan.

17. Recipes by meal plan and category:
-Displays a list of recipe belonging to specified category and meal plan.

18. Search ingredients:
- Displays a list of ingredients belonging to a specified name of an ingredient.

19. search meal plan:
- Displays a list of meal plans belonging to a specified name of meal plan.

20. Search recipe:
- Displays a list of recipe belonging to a specified  name of recipe.

21. Update ingredient column:
- Updates and ingredient.

22. Update meal plan column:
- updates a meal plan column.

23. Update recipe column:
- Updates a recipe column.
## Contributors
- Houstin Angwenyi

## License
This project is licensed under the [MIT License](LICENSE).