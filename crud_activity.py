
cookbook = []



def create(recipe):
    cookbook.append(recipe)
    print(f"{recipe} has been added to the cookbook")


def read(index):
    if index in range(len(cookbook)):
        print(cookbook[index])
    else:
        print("Aw shucks, the list ain't long enough, sorry T-T")

def update(index,recipe):
    if index in range (len(cookbook)):
        cookbook[index] = recipe
        print(f"Recipe at index {index} has been updated to '{recipe}'")
    else:
        print("Out of range!")

def destroy(index):
    if index in range (len(cookbook)):
        removed_recipe = cookbook.pop(index)
        print(f"{removed_recipe} has been removed from the cookbook")
    else:
        print("Out of range!")

def list_all_recipes():
    for recipe in cookbook:
        print(recipe)


def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

main()
