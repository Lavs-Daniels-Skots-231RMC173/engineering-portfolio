# This task is worth 3 points

"""
1********1
12******21
123****321
1234**4321
1234554321
Notice that there are no spaces after, it's just the numbers.
Use proper variable names, not one letter variable names
Do NOT use fixed values
Result must be a string that includes \n as line break. 
"""
def draw(height):
    result =""
    # TODO: Create a for loop that outputs a pyramid based on given height.
    for i in range(1, height + 1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)
        for j in range(2 * (height - i)):
            line += "*"
        for j in range(i, 0, -1):
            line += str(j)        
        result += line + "\n"
    # in loop use variable line to add new values
    # after creation/modification of each line, add it to variable result

    # return the variable result
    return result

if __name__ == "__main__":
    print(draw(5))