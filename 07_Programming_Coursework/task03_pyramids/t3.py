# This task is worth 2 points

"""
   #  #   
  ##  ##  
 ###  ### 
####  ####
*this one is assesed to be in full symetry

Notice that there ARE spaces after, it's NOT just the numbers.
Use proper variable names, not one letter variable names
Do NOT use fixed values.
Result must be a string that includes \n as line break. 
"""

def draw(height):
    result =""
    # TODO: Create a for loop that outputs a pyramid based on given height.
    for line_no in range(1, height+1):
    # in loop use variable line to add new values
        line = ""
    # after creation/modification of each line, add it to variable result
        for space in range(1, height - line_no + 1):
            line += " "
        for hashtag in range(line_no):
            line += "#"
        line += "  "
        for  hashtag in range(line_no):
            line += "#"
        for space in range(1, height - line_no + 1):
            line += " "
        result += line + "\n"
    # return the variable result
    return result

if __name__ == "__main__":
    # TODO: user input control
    # ask user to input a value, check if the value is 2 or more and 8 or less, if not - request the user for another input
    value = 0
    while (value <2 or value >8):
        value = input()
        value = int(value)
    print(draw(value))