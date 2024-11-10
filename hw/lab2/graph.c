#include <stdio.h>
#include <math.h>


//calculates y value for function y=3(sin(x)+4sqrt(x)+cos^2(x)-x+2)
float function(float x){
	float y = 3*(sin(x)+4*sqrt(x)+pow(cos(x), 2)-x+2);
	return y;
}

int main(){
//header
	printf("Plot for y=3(sin(x)+4sqrt(x)+cos^2(x)-x+2) for x from 0.0 to 20.0 with a 0.2 interval\n");
	printf("  X\t  Y\n");
//max and min
	float max = function(0);
	float min = function(0);
	float xMax=0;
	float xMin=0;
//finding and printing values
	for (float x = 0; x<20.1; x+=0.2){
		float y = function(x);
		printf("%.2f\t", x);
		printf("%.2f\t", y);
//find min and max
		if (y > max){
			max=y;
			xMax=x;
		}
		if (y < min){
			min=y;
			xMin=x;
		}
//print graph
		int Y = round(y);
		for (int i=0; i < y; i++){
			printf("#");
		}
		printf("\n");
	}
	printf("Max: %.2f at %.2f\n", max, xMax);
	printf("Min: %.2f at %.2f\n", min, xMin);
	return 0;
}
