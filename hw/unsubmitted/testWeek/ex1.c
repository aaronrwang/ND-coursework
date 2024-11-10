// testing the array shift function
#include <stdio.h>

void display(int [], int);
void leftshift(int [], int);

int main()
{
    int arr[] = {4, 9, 2, 8, 4, 3, 8, 7, 6};
    int size = sizeof(arr)/sizeof(int);

    printf("original array order: ");
    display(arr, size);

    leftshift(arr, size);
    printf("after 1st left shift: ");
    display(arr, size);

    leftshift(arr, size);
    printf("after 2nd left shift: ");
    display(arr, size);

    return 0;
}

void display(int a[], int sz)
{
    for (int i = 0; i < sz; i++)
    printf("%d ", a[i]);
    printf("\n");
}

// a circular left shift
void leftshift(int a[], int sz)
{
    int temp = a[0];
    for (int i = 0; i < sz-1; i++){
        a[i]=a[i+1];
    }
    a[sz-1]=temp;
}