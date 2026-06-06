#include <stdio.h>
// these are libraries to include, they are required to be at the top of the file
// stdio.h is for input output control
#include "half.cpp"

int main(void){
    // variables need actual data types as C is not an elastic language - it doesn't guess what you are using
    // variable can be predefined with data type but w/o a value
    float bill_amount;
    printf("Bill before tax and tip: ");
    scanf("%f/n", &bill_amount);
    float sales_tax;
    printf("Sales Tax: ");
    scanf("%f/n", &sales_tax);
    float tip;
    printf("Tip: ");
    scanf("%f/n", &tip);
    //printf("Input was = %f\n", bill_amount);
   // printf("Input was = %f\n", sales_tax);
    //printf("Input was = %f\n", tip);
    // TODO: create input for all three values given in task
    
    // TODO: fix values given to the function
    float result = half(bill_amount,sales_tax,tip);
    printf("You will owe %.2f eur each!\n", result);
    /*
    returns that are used in main function have their own meaning, all other functions can use them with this meaning or ar just value
    return 0 is used as EXIT_SUCCESS 
    return 1 is used as EXIT_FAILURE
    */
    return 0;
}
