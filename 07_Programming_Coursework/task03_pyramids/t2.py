# This task is worth 1 point

"""
Example:
2
24
246
2468
246810

Notice that there are no spaces after, it's just the numbers.
Use proper variable names, not one letter variable names
Do NOT use fixed values
Result must be a string that includes \n as line break. 
This makes the resulting string "2\n24\n246\n2468\n246810\n"
"""


def draw(height):
    result =""
    # TODO: Create a for loop that outputs a pyramid based on given height.
    for line_no in range(2, height+1,2):
    # The loop always uses the same increment and always the same start value of 2
    # in loop use variable line to add new values
        line = ""
        for value in range(2, line_no+1,2):
            line += str(value)        
    # after creation/modification of each line, add it to variable result
        result += line + "\n"
    # return the variable result
    return result

if __name__ == "__main__":
    print(draw(5))
    print()
    print(draw(10))