// rectangle.c - Aaron Wang - Fund Comp - Lab 3 - Ex 1
#include <stdio.h>

// function prototypes go here ...
float find_perim(float l, float w);
float find_area(float l, float w);
void display(float perim, float area);

int main()
{
  float len, wid;
  float perim, area;

  printf("enter the rectangle's length and width: ");
  scanf("%f %f", &len, &wid);

  perim = find_perim(len, wid);  // call the find_perim function
  area = find_area(len, wid);    // call the find_area function

  display(perim, area);          // call the display function

  return 0;
}

// function definitions go here ...
float find_perim(float l, float w){
	return 2 * (l+ w);
}

float find_area(float l, float w){
	return l * w;
}

void display(float perim, float area){
	printf("the perimeter is: %.2f\n", perim);
	printf("the area is: %.2f\n", area);
}
