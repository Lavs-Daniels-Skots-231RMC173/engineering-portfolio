#include <stdio.h>

int main(void)
{
    int start, end;

    
    do {
        printf("Start size: ");
        scanf("%d", &start);
    } while (start < 9);

    
    do {
        printf("End size: ");
        scanf("%d", &end);
    } while (end < start);

    int years = 0;
    while (start < end) {
        int born = start / 3;
        int died = start / 4;
        start = start + born - died;
        years++;
    }

    printf("Years: %d\n", years);

    return 0;
}