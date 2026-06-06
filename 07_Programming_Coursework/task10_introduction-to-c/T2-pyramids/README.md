# DIP750_24P_ENG_T14

# Hashtag pyramid

## Youy will need

Your Practical Task 5 Part 4 work

for loop - https://en.cppreference.com/w/cpp/language/for
while loop - https://en.cppreference.com/w/cpp/language/while
do while loop - https://en.cppreference.com/w/cpp/language/do
if statement - https://en.cppreference.com/w/cpp/language/if

## Task

Let's create pyramid like steps with # symbols and spaces. This task is aimed at understanding how values change and controlling output, as same skills that are required to display a character pyramid are used to control complex data structures and tables.

In input you should check if it's less than 1 or more than 8 - if so - require user to input value again.

**After successful run your terminal should look like this:**
```
Height: 4
   #  #   
  ##  ##  
 ###  ### 
####  ####
```
Take note that right and left sides are symetrical, so empty spaces should be on both sides, no matter that we can't see them on right side. Between both sides there are 2 spaces.
```
Height: 1
#  #
```
```
Height: 2
 #  #
##  ## 
```
```
Height: -1
Height: 2
 #  #
##  ## 
```

```
Height: 8
       #  #       
      ##  ##      
     ###  ###     
    ####  ####    
   #####  #####   
  ######  ######  
 #######  ####### 
########  ########
```
```
Height: 9
Height: 2
 #  #
##  ## 
```


## Notes

Although we use *.cpp files which indicate C++ language, in reality we are writing in C language which would require *.c files. This is done to ensure flexibility with future testing and addition of libraries as some of the libraries are easier and more accessable in C++.

Grading will be done manually.

Keep in mind that when working with string in C/C++, for long text we use " marks, for one character ' marks. 

At the end of the string there is a hidden symbol to notify of end of string which causes strings to be longer than in interpreted languages.

Try to incorporate if statement in this task. Take note that in C/C++ we use if/else if/ else if not elif.

All code should be located in main function.