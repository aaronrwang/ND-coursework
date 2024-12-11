// quadratics.c - Aaron Wang - Fund Comp - Lab 3 - Part 1
// computes the roots of a quadratic equation until terminated
#include <stdio.h>
#include <math.h>
float discriminant(float a, float b, float c);

int main()
{
  double a, b, c, disc;
  double x1, x2;
//ask for values
  printf("Enter the coefficients (a,b,c) of a quadratic equation (a=0 terminates program): ");
  scanf("%lf %lf %lf", &a, &b, &c);
	while (a != 0){
//solve for roots
		disc = discriminant(a, b, c);
		if (disc > 0){
			x1 = (sqrt(disc)-b)/(2 * a);
			x2 = (0-sqrt(disc)-b)/(2 * a);
			printf("roots: %f, %f\n", x1, x2);
		} else if (disc == 0){
			x1 = (0-b)/(2 * a);
			printf("root: %f\n", x1);
		} else {
			printf("There are no real solutions\n");
		}
//ask for new values
  printf("Enter the coefficients (a,b,c) of a quadratic equation (a=0 terminates program): ");
  scanf("%lf %lf %lf", &a, &b, &c);
	}
	return 0;
}

float discriminant(float a, float b, float c){
	return (b*b)-(4*a*c);
}

