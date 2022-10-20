#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

void linear_search(int A[],int n, int a)
{
    int i;
    for(i=0;i<n;i++)
    {
        if(A[i]==a)
        {
            printf("Element found at index: %d", i);
            break;
        }
    }
    if(i==n)
    {
        printf("Data not found..");
    }
}
int main()
{
    int n,a;
    printf("Enter no. of array:");
    scanf("%d",&n);
    int A[n],i;
    for(i=0;i<n;i++)
    {
        printf("A[%d]=",i);
        scanf("%d",&A[i]);
    }
    printf("\nEnter the data you want to search:");
    scanf("%d",&a);
    linear_search(A,n,a);
    return 0;
}
