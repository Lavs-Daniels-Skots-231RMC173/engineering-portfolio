#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    string word1, word2;
    printf("Player 1: ");
    getline(cin, word1);
    printf("Player 2: ");
    getline(cin, word2);

    int score1 = compute_score(word1);
    int score2 = compute_score(word2);
    // TODO: print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    int total = 0;

    for (int i = 0; i < word.length(); i++)
    {
        if (isalpha(word[i]))
        {
            
            char upper = toupper(word[i]);

            int index = upper - 'A';
            total += POINTS[index];
        }
        
    }

    return total;
}
