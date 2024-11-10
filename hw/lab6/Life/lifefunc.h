//Aaron Wang - Fund Comp - Lab 6 - header file - lifefunc.h
//Gives a header to all files in game of life

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#define SIZE 40

void displayBoard(char[][SIZE]);
void clearBoard(char[][SIZE]);
void animate(char[][SIZE]);
void advanceSimulation(char[][SIZE]);
int move(FILE*, char[][SIZE]);
void changeCell(char, int, int, char[][SIZE]);