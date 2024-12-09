//Aaron Wang - Fund Comp - Lab 4 - Part 1 grades.c
//Find the average and STDEV of a set of grades

#include <stdio.h>
#include <math.h>

// function prototypes ...
float average(int[], int);
float stdev(int[], int);

int main()
{
  	int grades[] =
    { 96,73,62,87,80,63,93,79,71,99,
      82,83,80,97,89,82,93,92,95,89,
      71,97,91,95,63,81,76,98,64,86,
      74,79,98,82,77,68,87,70,75,97,
      71,94,68,87,79 };

	// rest of program goes here ...
 	int size = sizeof(grades)/sizeof(grades[0]);
	printf("array of grades size: %d\n", size);
	printf("Average grade: %f\n", average(grades, size));
	printf("Standard Deviation: %f\n", stdev(grades, size));
  
  	return 0;
}

// function definitions ...
float average(int a[], int size){
	int total = 0;
	for (int i = 0; i < size; i++){
		total+=a[i];
	}
	float average = ((float) total)/size;
	return average;
}

//formula sqrt(sigma((x-ave)^2)/size)
float stdev(int a[], int size){
	float ave = average(a, size);
	float total = 0;
	for (int i = 0; i < size; i++){
		total+=pow(a[i]-ave,2);
	}
	float stdev=sqrt(total/size);
	return stdev;
}
