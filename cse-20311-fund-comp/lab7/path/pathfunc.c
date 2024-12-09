//Aaron Wang - Fund Comp - Lab 7 - path function file - pathfunc.c
//Contains functions for path program
#include "pathfunc.h"

int readFile(Point cords[], FILE* fp){
    int count = -1;
    while(1){
        if (feof(fp)) break;
        count++;
        fscanf(fp, "%f %f", &cords[count].x, &cords[count].y);
    }
    return count;
}

float calcDistance(Point cords[], int count){
    float path = 0;
    for (int i = 1; i < count; i++){
        path+= (float) sqrt(pow(cords[i].x-cords[i-1].x, 2)+pow(cords[i].y-cords[i-1].y, 2));
    }
    return path;
}

void displayInfo(Point cords[], int count, float path){
    printf("\nThere are %d points:\n\n", count);
    printf("   x   |   y   \n");
    printf("-------+-------\n");
    for (int i = 0; i < count; i++){
        printf("%6g | %6g\n", cords[i].x, cords[i].y);
    }
    printf("\nThe length of the path through them is %.2f\n", path);
}