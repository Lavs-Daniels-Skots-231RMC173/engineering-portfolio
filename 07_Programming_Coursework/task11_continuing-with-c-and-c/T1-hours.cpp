#include <ctype.h>
#include <stdio.h>

float calc_hours(int hours[], int weeks, char output);
int main(void)
{
    // TODO: create input for weeks and control that it should be no less than 0
    int weeks = 0;
    // This in an empty array, try changing weeks count and outputting what is in the array after inicialization
    int hours[weeks];
    // TODO: loop trough week count
    //          and input hours for each week
    char output;
    // TODO: create do while loop until output is T or A 
    //          at input moment - change input to capital letters
    
    // this is the function call
    // printf("%.1f hours\n", calc_hours(hours, weeks, output));
}

// TODO: Define the function to calculate total or average hours
float calc_hours(int hours[], int weeks, char output){
    int totalTime = 0;
    
    // TODO: Use a loop to sum the total hours
    for (int i = 0; i < weeks; i++) {
        totalTime += hours[i];
    }
    
    // TODO: Check the output type and return the corresponding value
    if (output == 'T') {
        return (float) totalTime;
    } else if (output == 'A') {
        return (float) totalTime / weeks;
    }
    
    return 0; 
}