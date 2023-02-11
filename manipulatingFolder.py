import os
from os import system
from pathlib import Path

base = Path.home()
# cria o path do diretorio
my_path = Path(base, "OneDrive", "Desktop", "Recipes")


def counter(path):
    count = 0
    for txt in Path(path).glob("**/*.txt"):  # isso percorre todos os arquivos
        count += 1
    return count

def hello():
    system("cls")
    print("Hello!\n")
    print(f"the recipes are in {my_path} and are {counter(my_path)} recipes\n")
    command = "x"
    while not command.isnumeric() or int(command) not in range(1, 7):
        print("choose an option: ")
        command = input()
    return int(command)
 
def show_categories(path):
    print("categories:")
    list_categories = []
    for folder in Path(path).iterdir():
        folder_name=str(folder.name)
        print(f"{folder_name}")
        list_categories.append(folder)
    return list_categories

def choose_category(list_categories):
    size = len(list_categories)
    choice=""
    while not choice.isnumeric() or int(choice) not in range(1, size+1):
        choice = input("choose a category: ")
    return list_categories[int(choice)-1]

def show_recipes(path):
    list_of_recipes = []
    for recipe in Path(path).glob("*.txt"):
        list_of_recipes.append(recipe)
    return list_of_recipes

def choose_recipe(list_of_recipes):
    size = len(list_of_recipes)
    choice = ''
    while not choice.isnumeric() or int(choice) not in range(1, size+1):
        choice = input("choose a recipe: ")
    return list_of_recipes[int(choice)-1]

def read(recipe):
    file = open(recipe, "r")
    print(file.read())
    file.close()

def create_recipe(path):
    recipe_exist = False
    while not recipe_exist:
        print("write the name of the new recipe: ")
        recipe_name = input()+".txt"
        print("write the content of your new recipe: ")
        recipe_content = input()
        new_path = Path(path, recipe_name)  # create a new path
        if not os.path.exists(new_path):
            Path.write_text(new_path, recipe_content)  # write on the new path
            print("done!")
            recipe_exist = True
        else:
            print("this recipe already exists!!!")

def create_category(path):
    category_exist = False
    while not category_exist:
        print("write the name of the new category: ")
        category_name = input()
        new_path = Path(path, category_name)  # create a new category path
        if not os.path.exists(new_path):
            Path.mkdir(new_path)  # create new category
            print("done!")
            category_exist = True
        else:
            print("this category already exists!!!")

def delete_recipe(recipe):
    Path(recipe).unlink()
    print("the recipe has been deleted")

def delete_category(category):
    Path(category).rmdir()
    print("the category has been deleted")

def return_menu():
    menu=''
    while menu.lower()!="x":
        menu=input("press x to return: ")
        

finish = False
while not finish:
    option = hello()
    if option == 1:
        categories = show_categories(my_path)
        choose = choose_category(categories)
        recipes = show_recipes(choose)
        recipe = choose_recipe(recipes)
        read(recipe)
        return_menu()
    elif option == 2:
        categories = show_categories(my_path)
        choose = choose_category(categories)
        create_recipe(choose)
        return_menu()
    elif option == 3:
        create_category(my_path)
        return_menu()
    elif option == 4:
        categories = show_categories(my_path)
        choose = choose_category(categories)
        recipes = show_recipes(choose)
        recipe = choose_recipe(recipes)
        delete_recipe(recipe)
        return_menu()
    elif option == 5:
        categories = show_categories(my_path)
        choose = choose_category(categories)
        delete_category(choose)
        return_menu()
    elif option == 6:
        finish = True
        
