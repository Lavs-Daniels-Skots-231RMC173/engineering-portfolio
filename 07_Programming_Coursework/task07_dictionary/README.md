[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/YBl2BWqz)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18437859)

# DIP750_24P_ENG_T11


In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the given information lower.
Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit and return "try again".

Task needs to be done in a function named find_fruit(), that receives one variable/argument - the input text, returns one variable - numeric value of calories.
String formatting for input and output is outside of this function and is not graded.

This task requires the use of Dictionary. It's a similar structure to a list, with unique names instead of indexes. Technically it's not forbidden to use capital/lower letter mix in names, depending on context written in names it is "good style" to use lower letters.

Sample for dictionary:
```
my_dictionary: {"name 1": 200, "name 2": "my string", "name x": [5,7,9,10]}
```
Values can be all types of data types.
To access values you write:
```
my_dictionary["name 1"]
my_dictionary["name x"][0]
```

Sample for terminal after the program wa successfully run:
```
Item: apple
Calories: 130
```

Information for dicitonary:
```
apple 130
avocado 50
banana 110
cantaloupe 50
grapefruit 60
grapes 90
honeydew melon 50
kiwi 90
lemon 15
lime 20
nectarine 60
orange 80
peach 60
pear 100
pineapple 50
plums 70
strawberries 50
sweet cherries 100
tangerine 50
watermelon 80
```

Additional information:

https://docs.python.org/3/tutorial/datastructures.html#dictionaries

https://realpython.com/python-dicts/#dgetkey-default
