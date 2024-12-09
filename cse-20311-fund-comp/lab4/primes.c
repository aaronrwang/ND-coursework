//Aaron wang - Fund Comp - Lab 4 - part 2 primes.c
//finds and prints every prime number between 1-1000 

#include <stdio.h>

int main(){
	int prime[1000];
	for (int i = 0; i < 1000; i++){
		prime[i]=1;
	}
	for (int i = 2; i < 1000; i++){
		if(prime[i]==1){
			for (int j = 2*i; j < 1000; j+=i){
				prime[j]=0;
			}
		}
	}
int count = 0;
	for (int i = 2; i < 1000; i++){
		if(prime[i]==1){
			printf("%4d", i);
			count++;
			if(count%10==0){
				printf("\n");
			}
		}
	}
	printf("\n");

	return 0;	
}
