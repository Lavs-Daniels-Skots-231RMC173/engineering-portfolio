# This task is worth 1 point
"""
Example:
1
12
123
1234
12345

Notice that there are no spaces after, it's just the numbers.
Use proper variable names, not one letter variable names
Do NOT use fixed values
Result must be a string that includes \n as line break. 
This makes the resulting string "1\n12\n123\n1234\n12345\n"
"""


def draw(height):
    result =""
    # TODO: Create a for loop that outputs a pyramid based on given height.
    for line_no in range(1, height+1):
    # in loop use variable line to add new values
        line = ""
        for value in range(1, line_no+1):
            line += str(value)
    # after creation/modification of each line, add it to variable result
        result += line + "\n"
    # return the variable result
    return result

if __name__ == "__main__":
    print(draw(3))
    print()
    print(draw(5))