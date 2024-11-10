//Aaron Wang - Fund Comp - Lab 7 - path driver file - path.c
//Driver file for the path program
#include "pathfunc.h"

int main(){
    FILE *fp;
    char infile[30];
    printf("Enter a file name: ");
    scanf("%s", infile);

    fp = fopen(infile, "r");
    if (!fp){
        printf("file %s not found\n", infile);
        return 1;
    }

    Point cords[30];
    int count = readFile(cords, fp);
    fclose(fp);
    
    float path = calcDistance(cords, count);

    displayInfo(cords, count, path);
}

