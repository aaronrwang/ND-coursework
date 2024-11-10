// polar.c - Aaron Wang - Fund Comp - Lab 3 - Part 2
// Cartesian to polar Calculator and Quadrant finder
#include <math.h>
#include <stdio.h>

int get_quadrant(double x, double y);
double get_radius(double x, double y);
double get_angle(double x, double y);
void show_info(int quadrant, double radius, double angle);

int main (){
	double x, y;
//gathers user input
	printf("Enter coordinates (x, y): ");
	scanf("%lf %lf", &x, &y);
	show_info(get_quadrant(x, y), get_radius(x, y), get_angle(x, y));
	
	return 0;
}
//returns quadrant number (returns 0 if on axis)
int get_quadrant(double x, double y){
	if (x > 0 && y > 0){
		return 1;
	} else if (x < 0 && y > 0){
		return 2;
	} else if (x < 0 && y < 0){
		return 3;
	} else if (x > 0 && y < 0){
		return 4;
	} else {
		return 0;
	}
}
double get_radius(double x, double y){
	return sqrt(x*x+y*y);
}
double get_angle(double x, double y){
	return atan2(y, x)*180/M_PI;
}
void show_info(int quadrant, double radius, double angle){
	printf("Your point is in quadrant %d and its polar coordinates (r, theta) are (%lf, %lf)", quadrant, radius, angle);
}
