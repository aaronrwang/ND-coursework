// quad.c
// computes the roots of a quadratic equation
#include <stdio.h>
#include <math.h>

int main()
{
  double a, b, c, disc;
  double x1, x2;

  printf("Enter the coefficients (a,b,c) of a quadratic equation: ");
  scanf("%lf %lf %lf", &a, &b, &c);

  // ... rest of program goes here
	disc = (b*b)-(4*a*c);
	if (disc > 0){
		x1 = (sqrt(disc)-b)/(2 * a);
		x2 = (0-sqrt(disc)-b)/(2 * a);
		printf("roots: %f, %f\n", x1, x2);
	} else if (disc == 0){
		x1 = (0-b)/(2 * a);
		printf("root: %f\n", x1);
	} else {
		printf("There are no real solutions");
	}
	return 0;
	
}

