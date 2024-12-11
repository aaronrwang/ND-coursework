//Aaron Wang - Fund Comp - Lab 9 - crossword driver file - path.c
//Driver file for the crossword program
#include "func.h"

int main(int argc, char *argv[]){
    FILE *outputfile = stdout;
    char input[20][16] = {};
    char board[15][15] = {};
    int count;
    if(argc==3|| argc==2){
        if(argc==3){
            outputfile = fopen(argv[2], "w");
        }
        FILE *fp = fopen(argv[1],"r");
        if (!fp) {
            printf("file %s not found\n", argv[1]);
            return 2;
        }
        count = readFile(fp, input, outputfile);
    } else if (argc==1) {
        printf("Enter a list of words:\n");
        count = readFile(stdin, input, outputfile);
    } else {
        printf("Too many arugments.\nProper usage: %s (inputfile.txt) (outputfile.txt)", argv[0]);
    }
    
    
    Word words[20]={};
    sort(words, input, count);
    upperCase(words, count);
    addFirstWord(board, words);
    
    fprintf(outputfile, "\n\n");
    
    for (int i = 0; i < count; i++){
        words[i]=scramble(words[i]);
    }
    int T = 2; //counts iterations
    int n = 1; //# of word to try and add
    int currWordsAdded = 1; //used to compare if iterations had the same amount of words
    int lastWordsAdded = 1;
    while(n<count){
        if(words[n].use==0){
            currWordsAdded+=addWord(board, words, n, count, outputfile);
        }
        n++;
        if(n==count){
            n=1;
            if(currWordsAdded==count) break; //if every word is put in, none can be added
            if(currWordsAdded==lastWordsAdded) break; //if curr and last iteration had the same number of words, none can be added
            lastWordsAdded=currWordsAdded;
            T++;
        }
    }
    fprintf(outputfile, "\n");
    displaySolution(board, outputfile);
    fprintf(outputfile, "\n");
    displayBoard(board, outputfile);
    printClues(words, count, outputfile);
}