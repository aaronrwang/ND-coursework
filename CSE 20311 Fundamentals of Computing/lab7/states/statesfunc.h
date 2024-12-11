//Aaron Wang - Fund Comp - Lab 7 - states header file - statesfunc.h
//Gives a header to all files for states program

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <ctype.h>



typedef struct state_struct{
    char abbreviation[3];
    char name[256];
    char capital[256];
    int year;
} state;

int readFile(state[], FILE*);
void displayMenu();
void displayData(state[], int);
void capitals(state[], int);
void abbreviations(state[], int);
void statesBefore(state[], int);
void statesAfter(state[], int);
void lowerString(char[]);
