[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Jd58FfGk)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19155233)
# DE0807_24R_ENG_T12

## Task 1 - Scrabble

```
Player 1: COMPUTER
Player 2: science
Player 1 wins!
```

In the game of Scrabble, players create words to score points, and the number of points is the sum of the point values of each letter in the word.

A B C D E F G H I J K L M N O P Q   R S T U V W X Y Z

1	3	3	2	1	4	2	4	1	8	5	1	3	1	1	3	10	1	1	1	1	4	4	8	4	10

For example, if we wanted to score the word Code, we would note that in general Scrabble rules, the C is worth 3 points, the o is worth 1 point, the d is worth 2 points, and the e is worth 1 point. Summing these, we get that Code is worth 3 + 1 + 2 + 1 = 7 points.

## Implementation Details
Complete the implementation of scrabble.py, such that it determines the winner of a short scrabble-like game, where two players each enter their word, and the higher scoring player wins.

Notice that we’ve stored the point values of each letter of the alphabet in an integer list named POINTS.

For example, A or a is worth 1 point (represented by POINTS[0]), B or b is worth 3 points (represented by POINTS[1]), etc.

Notice that we’ve created a prototype for a function called compute_score() that takes a string as input and returns an int.

Whenever we would like to assign point values to a particular word, we can call this function. 

In main(), the program prompts the two players for their words using the get_string() function. These values are stored inside variables named word1 and word2. The function get_string() also converts all letters to capital letters.

In compute_score(), your program should compute, using the POINTS list, and return the score for the string argument. 

Characters that are not letters should be given zero points, and uppercase and lowercase letters should be given the same point values.

For example, ! is worth 0 points while A and a are both worth 1 point.

Though Scrabble rules normally require that a word be in the dictionary, no need to check for that in this problem!

In main(), your program should print, depending on the players’ scores, Player 1 wins!, Player 2 wins!, or Tie!.


cin - https://en.cppreference.com/w/cpp/io/cin


This task will be graded manually, coefficient 0.5
ONLY GitHub Copilot is allowed.
You are NOT allowed to create another array!
