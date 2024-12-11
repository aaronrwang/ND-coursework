// testgcd.c - Aaron Wang - Fund Comp - lab 3 - Ex 2
#include <stdio.h>

int get_gcd(int n, int m);

int main(){
	int n, m;
	printf("Enter two positive integers: ");
	scanf("%d %d", &n, &m);
	int gcd  = get_gcd(n, m);
	printf("The greatest common divisor between these two numbers is: %d\n", gcd);
	return 0;
}

int get_gcd(int n, int m){
	int min = n;
	if (m < n){
		min = m;
	}	
	for (int i = min; i > 0; i--){
		if (n % i == 0 && m % i == 0){
			return i;
		}
	}
	return -1;
}
