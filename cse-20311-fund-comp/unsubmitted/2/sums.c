#include <math.h>
#include <stdio.h>
int main(){
	int n;
	printf("Enter an integer: ");
	scanf("%d", &n);
	int sumOne = 0;
	double sumTwo = 0;
	for (int i = 0; i < n + 1; i++){
		sumOne+=(i*i);
		sumTwo+=sqrt(i);
	}
	printf("Sum one: %d\n", sumOne);
	printf("Sum two: %f\n", sumTwo);
		
	return 0;	
}
