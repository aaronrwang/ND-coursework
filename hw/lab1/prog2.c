#include <stdio.h>
#include <math.h>

int main()
{
	int x1,x2,x3,y1,y2,y3;
	printf("This is a cross product calculator.\n");
	printf("Enter vector v = [a,b,c] as prompted  \n");

	printf("v1[a]: ");
	scanf("%d", &x1);
	printf("v1[b]: ");
	scanf("%d", &x2);
	printf("v1[c]: ");
	scanf("%d", &x3);

	printf("v2[a]: ");
	scanf("%d", &y1);
	printf("v2[b]: ");
	scanf("%d", &y2);
	printf("v2[c]: ");
	scanf("%d", &y3);

	int z1 = x2*y3-x3*y2;
	int z2 = y1*x3-x1*y3;
	int z3 = x1*y2-x2*y1;

	printf("[%d,%d,%d]\n", z1, z2, z3);
}
