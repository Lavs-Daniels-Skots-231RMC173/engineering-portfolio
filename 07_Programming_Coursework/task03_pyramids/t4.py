# This task is worth 3 points
"""
****5
***45
**345
*2345
12345

Notice that there are no spaces after, it's just the numbers.
Use proper variable names, not one letter variable names
Do NOT use fixed values
Result must be formatted a that includes \n as line break. 
"""
def draw(height):
    result =""
    # TODO: Create a for loop that outputs a pyramid based on given height.
    for i in range(0, height):
        line = ""
        for j in range(1, height-i):
            line += "*"
        for j in range(height-i, height+1):
            line += str(j)
        result += line + "\n"
    # in loop use variable line to add new values
    # after creation/modification of each line, add it to variable result

    # return the variable result
    return result

if __name__ == "__main__":
    print(draw(3))
    print()
    print(draw(5))
