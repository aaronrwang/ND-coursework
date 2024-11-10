#include <stdio.h>

int main(){
	int n;
	printf("Enter a positive Integer: ");
	scanf("%d", &n);
	while (n > 0){
		printf("%d\n",n%10);
		n/=10; 
	}
	return 0;
}
