//Aaron Wang - Fund Comp - Lab 5 - Part 1 letterfreq.c
//Analyzes the letters of each file of text

#include <stdio.h>
#include <ctype.h>
#define numLetters  26
void displayCount(int letterCount[], int size);
void displayPercent(int letterCount[], int size, int letters);

int main()
{
    //read in file
    
    FILE *fp;
    char infile[30];

    printf("enter a file name: ");
    scanf("%s", infile);

    fp = fopen(infile, "r");    // connect to the file
    if (!fp) {                  // OR:  if (fp == NULL);
        printf("file %s not found\n", infile);
        return 1;
    }

    //Find out the # of letters and how many times each letter appears
    int count = 0;
    int letterCount[numLetters]={};
    char letter;
    int letters = 0;
    while (1){
        fscanf(fp, "%c", &letter);   
        if(feof(fp)) break;
              
        letter=tolower(letter);
        letterCount[letter-97]++;      
        count++;
        if(isalpha(letter)){
            letters++;
        }                  
    }
    fclose(fp);

    //print out general summary
    printf("General summary for %s:\n", infile);
    printf("   count: %d\n", count);
    printf("   count: %d\n", letters);


    displayCount(letterCount, numLetters);
    
    displayPercent(letterCount, numLetters, letters);
    
    return 0;
}

void displayCount(int letterCount[], int size){
    printf("Letter count:\n");
    for (int i = 0; i < size; i++){
        printf("   %c: %6d", 97+i,letterCount[i]);
        if (i%6==5){
            printf("\n");
        }
    }
    printf("\n");
}

void displayPercent(int letterCount[], int size, int letters){
    printf("Letter percentages:\n");
    for (int i = 0; i < size; i++){
        printf("   %c: %5.1f%%", 97+i,((float)letterCount[i])/letters*100);
        if (i%6==5){
            printf("\n");
        }
    }
    printf("\n");
}