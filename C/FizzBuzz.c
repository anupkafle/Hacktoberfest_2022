#include <stdio.h>

int main()
{
    int num,n;
    printf("enter the number till you want FizzBuzz to be printed:\n");
    scanf("%d", &n);
    for (num = 1; num <= n; num++)
    {
        if ((num % 3 == 0) && (num % 5 == 0))
        {
            printf("FizzBuzz\n");
        }

        else if (num % 5 == 0)
        {
            printf("Buzz\n");
        }
        else if (num % 3 == 0)
        {
            printf("Fizz\n");
        }
        else
        {
            printf("%d\n", num);
        }
    }
    return 0;
}

//Alternate way with less lines
/*
int main(void)
{
    int i;
    for(i=1; i<=100; ++i)
    {
        if (i % 3 == 0)
            printf("Fizz");
        if (i % 5 == 0)
            printf("Buzz");
        if ((i % 3 != 0) && (i % 5 != 0))
            printf("number=%d", i);
        printf("\n");
    }

    return 0;
} 
*/
