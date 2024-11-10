#include "func.h"

int main(int argc, char *argv[]){
    char input[20][16] = {};
    char board[15][15] = {};
    int count;
    if(argc==1){
        printf("Enter a list of words:\n");
        count = readFile(stdin, input);
    } else if (argc==2){
        FILE *fp = fopen(argv[1],"r");
        if (!fp) {
            printf("file %s not found\n", argv[1]);
            return 2;
        }
        count = readFile(fp, input);
    } else {
        printf("Too many arugments.\nProper usage: %s (file.txt)", argv[0]);
    }

    Word words[20]={};
    sort(words, input, count);
    upperCase(words, count);
    addFirstWord(board, words);
    
    printf("\n\n");
    
    for (int i = 0; i < count; i++){
        words[i]=scramble(words[i]);
    }
    int T = 2; //keeps track of how many times we try to insert words
    int n = 1; //keeps track of word to insert
    int currWordsAdded = 1; //if curr and last are the same that means none of the words can be inserted
    int lastWordsAdded = 1;
    printf("Iteration: 1\n");
    while(n<count){
        if(words[n].use==0){
            currWordsAdded+=addWord(board, words, n, count);
        } //insert word if not already inserted
        n++;
        if(n==count){
            n=1;
            if(currWordsAdded==count) break;
            if(currWordsAdded==lastWordsAdded) break;
            lastWordsAdded=currWordsAdded;
            printf("Iteration: %d\n", T);
            T++;
        } //checks to see if this is the final state the puzzle can be in
    }
    printf("\n");
    displaySolution(board);
    printf("\n");
    displayBoard(board);
    printClues(words, count);

    for (int i = 0; i < count; i++){
        displayWord(words[i]);
    }
}
