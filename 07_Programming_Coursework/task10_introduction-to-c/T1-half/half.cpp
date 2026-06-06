#include <math.h>
// math is for math functions, like rounding

// This is a template/prototype for a function - if this is at the beginning of the file - you can write your function after main function. 
//Technically not needed here as main function is in a different file.
/*
functions in C consist of 
returnDataType functionName (list of arguments with data type)
void is used when there is no return or arguments 
*/
float half(float bill, float tax, float tip);

    
// TODO: complete the function
float half(float bill, float tax, float tip){
    //printf("%f", bill);
    //printf("%f", tax);
    //printf("%f", tip);
    // this is just a placeholder calculation to ensure running template before function completion
    float total = (bill * (tax/100+1) + tip);
    float result = total/2;
    return result;
}
