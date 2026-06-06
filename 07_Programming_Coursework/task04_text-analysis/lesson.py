"""
the main purpose of functions is to make code reusable either in the same project or another project

all functions consist of:

def function_name(<list of arguments>):
  code to execute
  <return>

there are multiple types of functions:
1. functions that don't have arguments and don't have a return
2. functions with no arguments, but have a return
3. functions with one or more arguments, but no return
4. functions with one or more arguments and a return
"""

def hello():
  print("hello")

def hi(name):
  print(name)

def sum(a,b):
  result = a + b
  print(result)

def multiply(a,b):
  result = a * b
  return result

"""
usually when function has a print in it - the function doesn't contain anything else, e.g. calculations
although it is possible to do calculations in return - it's not advised, especially with heavy calculations as it can lead to memory errors
there are functions that are so called getters and setters - this means that the functions purpose is to get or to set a value
"""
