[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/NDO56oIM)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18437698)
f DE0807_24-25P_PT05
Assume that all user inputs will be correct. This task is not about efficiency, but about splitting process in similar processes and to cause thoughts about more efficient ways this could be done.
Theoretical material can be found in file **lesson.py**

## Cash

Implement a program in given file, that gives out change with least amount of coins possible.

Allowed coins: 25, 10, 5, 1 cents.

Create a file called **cash.py**. In this file implement further mentioned functions with the given names. User will input "Change owed: " amount and you have to output total coin count.

Function list:
* get_cents() - prompts user for input, transforms the input to integer
* calculate_quarters(change) - calculates how many quarters (25c coins) can be given, returns number of coins
* calculate_dimes(change) - calculate how many dimes (10c coins) can be given, returns number of coins
* calculate_nickels(change) - calculate how many nickels (5c coins) can be given, return number of coins
* calculate_pennies(change) - calculate how many pennies (1c coins) can be given, return number of coins
* coin_count(change) - get's the amount of money given in cents, furthers it to calculations, returns total number of coins
* main() - calls for get_cents and coin_count, also outputs the resulting coin count (don't forget to add name==main check for main() to be launched)

Output example:
```
Change owed: 41
Coins: 4
```

Test values: 99, 26, 25, 24, 5, 4, 1, 0

Tests check for the 8 cases and for individual functions.
