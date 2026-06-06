#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <iostream>
// ctype provides symbol check

using namespace std;

bool valid(string password);

int main(void)
{

    
    string password;
    printf("Enter your password: ");
    cin >> password;
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
        fflush(stdout);   
            }
    return 0;
}
bool valid(string password)
{
    bool hasUpper = false;
    bool hasLower = false;
    bool hasDigit = false;
    bool hasSymbol = false;

    for (char c : password)
    {
        if (isupper(c))
        {
            hasUpper = true;
        }
        else if (islower(c))
        {
            hasLower = true;
        }
        else if (isdigit(c))
        {
            hasDigit = true;
        }
        else if (ispunct(c))
        {
            hasSymbol = true;
        }  
    }
    return hasUpper && hasLower && hasDigit && hasSymbol;
}