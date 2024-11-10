//Aaron Wang - Fund Comp - Lab 7 - path header file - pathfunc.h
//Gives a header to all files for path program

#include <stdio.h>
#include <math.h>

typedef struct coordinate_struct{
    float x;
    float y;
} Point;

int readFile(Point[], FILE*);
float calcDistance(Point[], int);
void displayInfo(Point[], int, float);