#include <stdio.h>
#include <string.h>
#include <iostream>
// string.h provides strlen and length

using namespace std;
string replace(string input){
    for (int i = 0; i < input.length(); i++) {
        switch (input[i]) {
            case 'a':
            case 'A':
                input[i] = '6';
                break;
            case 'e':
            case 'E':
                input[i] = '3';
                break;
            case 'i':
            case 'I':
                input[i] = '1';
                break;
            case 'o':
            case 'O':
                input[i] = '0';
                break;
            case 'u':
            case 'U':
                break;
            default:
                break;

        }
    }
    return input;
}




int main(int argc, char* argv[])
{
    //    printf("%i", argc);
    // TODO: find out how many values should be in argc and change n to the appropriate number
    int n = 2; 
    if (argc != n) {
        printf("error\n");
        return 1;
    }
    string output = replace(argv[1]);
    printf("%s\n", output.c_str());
    return 0;
}
