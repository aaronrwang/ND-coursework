#include <stdio.h>

int main()
{
	int td, ep, fg, s;
	//Get user input
	printf("How many touchdowns: ");
	scanf("%d", &td);
	printf("How many extra points: ");
	scanf("%d", &ep);
	printf("How many field goals: ");
	scanf("%d", &fg);
	printf("How many safeties: ");
	scanf("%d", &s);
	//Print answer
	int score = td*7+ep+fg*3+s*2;
	printf("%d\n", score);
}
