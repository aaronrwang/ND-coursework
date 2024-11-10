//Aaron Wang - Fund Comp - Lab 6 - driver file - playlife.c
//Contains the main code for the game of life.
#include "lifefunc.h"

int main(int argc, char *argv[]){
    char board [SIZE][SIZE];
    if (argc==1){
        clearBoard(board);
        displayBoard(board);

        //iterate through actions
        int option = 0;
        while(!option){
            option=move(stdin, board);
        }
    } else if (argc==2){
        FILE *fp = fopen(argv[1],"r"); //open file return null if no file
        if (!fp) {
            printf("file %s not found\n", argv[1]);
            return 2;
        }

        clearBoard(board);

        //iterate through file commands
        int option = 0;
        while (!option){
            option = move(fp, board);
        } 
    } else{
        printf("Too many arguments\n");
        return 1;
    }
    return 0;
}