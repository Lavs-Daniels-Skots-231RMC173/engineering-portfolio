
# define the function that will search for the fruit and return the calories
def find_fruit(fruit):
    # information for dicitonary
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwi": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    # convert the input to lowercase
    fruit = fruit.lower()

    # check if the input fruit is in the dictionary and return the corresponding calories
    if fruit in fruit_calories:
        return fruit_calories[fruit]
    else:
        return "try again"
    
# define the calculate_quarters function
def calculate_quarters(fruit):
    return "try again"

# main program to prompt the user and display the result
def main():
    user_input = input("Item: ")  
    calories = find_fruit(user_input)  
    print("Calories:", calories)  

# main program runs when executed

if __name__ == "__main__":
    main()
