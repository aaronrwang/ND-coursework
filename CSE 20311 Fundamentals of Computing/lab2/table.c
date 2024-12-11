#include <stdio.h>

int digits(int n);
//program only esigned for x<100 & y<100;
int main(){
	printf("Enter the dimensions for a multiplication table: ");
	int x, y;
	scanf("%d %d", &x, &y);
	printf("*  ");
	//Prints header
	for (int i = 1; i <= x; i++){
		printf("%5d", i);
	}  
	printf("\n");
	//prints horizontal line
	printf("   ");
	int width = 5 * x;
	for (int i = 0; i < width; i++){
		printf("-");
	}
	printf("\n");
	//printing table
	for (int i = 1; i <= y; i++){
		printf("%2d", i);
		printf("|");
		for (int j = 1; j <= x; j++){
			printf("%5d", i * j);
		}
		printf("\n");
	}
	return 0;
}

int digits(int n){
	int count = 0;
	while (n > 0){
		count++;
		n/=10;
	}
	return count;
}
