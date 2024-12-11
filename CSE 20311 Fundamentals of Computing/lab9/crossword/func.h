#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

typedef struct{
    char str[16];
    char scramble[16];
    int use;
    //0: unused; 1: horizontal; 2: vertical
    int x;
    int y;
} Word;

int readFile(FILE*, char[20][16]);
void sort(Word[20],char[20][16], int);
void upperCase(Word[20], int);
Word scramble(Word);
void addFirstWord(char[15][15],Word[20]);
int addWord(char[15][15], Word[20], int, int);
void displaySolution(char[15][15]);
void displayBoard(char[15][15]);
void printClues(Word[20], int);
void displayWord(Word);

