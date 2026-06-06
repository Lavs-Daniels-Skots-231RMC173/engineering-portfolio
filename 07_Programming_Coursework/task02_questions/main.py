"""
This is a function. A function is a piece of code that can be used repeatedly. The main purpose is that you jsut write the name and don't copy the code.
This also allows to avoid additional bugs(mistakes) when having new changes to code as there is only one copy of the code.
def - define
choice - name of function
() - contain arguments
v1, v2 - arguments

Functions receive data trough function calls. As it's good practice to not deal with data in same place where we input and output it, sometimes functions need to send something back. 
return provides functions with the ability to send some data back.
In some languages return can give not only data, but also statuses. Although Python is not one of them, they sometimes are seen or used as placeholders.
0 - success, 1 - fail.
"""
def choice(v1, v2):
    # TODO: compare v1 and v2, after comparison assign to variable result values "Value 1 is bigger than Value 2" / "Value 1 is smaller than Value 2" / "Both values are the same"
    if v1 > v2:
        result = "Value 1 is bigger than Value 2"
    elif v1 < v2:
        result = "Value 1 is smaller than Value 2"
    else:
        result = "Both values are the same"
    # TODO: return the variable result
    return result


if __name__ == "__main__":
    # all the things that start with an indent, work in this if context
    # TODO: ask user to input "Value 1: " and "Value 2: "
    value_1 = input("Value 1: ")
    value_2 = input("Value 2: ")
    # TODO: cast these values to integer
    value_1 = int(value_1)
    value_2 = int(value_2)
    # While it is possible to use the same name in function call and inside function, let's avoid that for the first couple of tasks while you learn what works in which context.
    result = choice(value_1, value_2)
    print(result)
# this is outside of the if
print("program ended")