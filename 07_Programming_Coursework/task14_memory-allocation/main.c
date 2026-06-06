#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check for command line args,
    // if argc is not 2, output usage suggestion "Usage: ./read infile\n" and return 1
    if (argc != 2)
    {
        printf("Usage: ./read infile\n");
        return 1;
    }

    // Create char buffer with size 7 chars to read into,
    // variable name - buffer
    char buffer[7];
    // Create array to store plate numbers
    char *plates[8];
    // connection to file
    FILE *infile = fopen(argv[1], "r");
    if (!infile)
    {
        perror("Error opening file");
        return 1;
    }

    int idx = 0;
    // using while loop, read data from file using fread
    // fread takes 4 parameters - where to write, size of each, count, file pointer
    // fread returns number of items read
    while (idx < 8 && fread(buffer, sizeof(char), 7, infile) == 7)
    {
        // replace any '\n' in the 7-byte chunk with '\0'
        for (int i = 0; i < 7; i++)
        {
            if (buffer[i] == '\n')
                buffer[i] = '\0';
        }

        // allocate exactly strlen(buffer)+1 bytes, copy in, bump idx
        plates[idx] = malloc(strlen(buffer) + 1);
        if (!plates[idx])
        {
            fprintf(stderr, "Memory allocation failed at plate %d\n", idx);
            // cleanup any earlier allocations
            for (int j = 0; j < idx; j++)
                free(plates[j]);
            fclose(infile);
            return 1;
        }
        strcpy(plates[idx], buffer);
        idx++;
    }
    fclose(infile);

    // output only the plates we actually read
    for (int i = 0; i < idx; i++)
    {
        printf("%s\n", plates[i]);
    }

    // free all allocations so valgrind reports zero leaks
    for (int i = 0; i < idx; i++)
    {
        free(plates[i]);
    }

    return 0;
}

