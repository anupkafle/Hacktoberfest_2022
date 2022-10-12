#include <stdio.h>
#include <stdlib.h>

void interpolation_search(int A[],int lb, int ub, int a)
{
    if(ub>=lb)
    {
        int mid = lb + (((a-A[lb])*(ub-lb))/(A[ub]-A[lb]));
        if(a == A[mid])
            printf("Data is found at index: %d",mid);
        else if(a>A[mid])
        {
            interpolation_search(A,mid+1,ub,a);
        }
        else if(a<A[mid])
        {
            interpolation_search(A,lb,mid-1,a);
        }
    }
    else
        printf("Data not found..");
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
    interpolation_search(A,0,n-1,a);
    return 0;
}
