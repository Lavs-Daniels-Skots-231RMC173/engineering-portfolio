[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Wfueh0bx)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18656402)
# DE0807_24_25P_ENG_T08

This task is graded manually. Assume that input will be as correct as described in task. 
As this task is manually graded we will be skipping one step - it is possible to creata a requirements file, that allows to list all needed libraries sso that when someone else tries to run code on their device - can install the missing libraries with no guesswork.



FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:
```
 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/
```
Among the fonts supported by FIGlet are those at http://www.figlet.org/examples.html.

FIGlet has since been ported to Python as a module called *pyfiglet*.

In a file called figlet_sample.py, implement a program that:

- Expects zero or two command-line arguments:

  - Zero if the user would like to output text in a random font.

  - Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
    - If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.
 - Prompts the user for a string of text.
 - Outputs that text in the desired font.




Run command samples:
```
python figlet_sample.py
Input: Moo

        :::   :::   ::::::::  :::::::: 
      :+:+: :+:+: :+:    :+::+:    :+: 
    +:+ +:+:+ +:++:+    +:++:+    +:+  
   +#+  +:+  +#++#+    +:++#+    +:+   
  +#+       +#++#+    +#++#+    +#+    
 #+#       #+##+#    #+##+#    #+#     
###       ### ########  ########       


python figlet_sample.py test
Invalid usage

python figlet_sample.py -a slant
Invalid usage

python figlet_sample.py -f invalid_font
Invalid usage

python figlet_sample.py -f rectangles
Input: Hello world
 _____     _ _                        _   _ 
|  |  |___| | |___      _ _ _ ___ ___| |_| |
|     | -_| | | . |_   | | | | . |  _| | . |
|__|__|___|_|_|___| |  |_____|___|_| |_|___|
                  |_|


python figlet_sample.py -f alphabet
Input: Moo
M   M         
MM MM         
M M M ooo ooo 
M   M o o o o 
M   M ooo ooo  
```


Additional material:

https://pip.pypa.io/en/stable/installation/ - about installing libraries

https://requirements-txt.readthedocs.io/en/latest/ - about requirements txt file

https://docs.python.org/3/library/random.html - about random

https://docs.python.org/3/library/sys.html - about sys argv and sys exit



