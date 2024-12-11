//Aaron Wang - Fund Comp - Lab 6 - functions file - lifefunc.h
//Contains all functions necessary for game of life.

#include "lifefunc.h"

void clearBoard(char board [][SIZE]){
    for (int i = 0; i < SIZE; i++){
        for (int j = 0; j < SIZE; j++){
            board[i][j]=' ';
        }
    }
}

void displayBoard(char board [][SIZE]){

    //print top border
    printf("+");
    for(int i = 0; i < SIZE;i++){
        printf("-");
    }
    printf("+\n");

    //print body
    for (int i = 0; i < SIZE; i++){
        printf("|");
        for (int j = 0; j < SIZE; j++){
            printf("%c",board[i][j]);
        }
        printf("|\n");
    }

    //print bottom border
    printf("+");
    for(int i = 0; i < SIZE;i++){
        printf("-");
    }
    printf("+\n");
}

int move(FILE *fp, char board [][SIZE]){
    char input;
    int x,y;
    printf("Command: ");
    fscanf(fp, "%c", &input);
    if(input=='a'||input=='r'){
        fscanf(fp, "%d %d", &x, &y);
        printf("%c: %d %d\n", input, x, y);
        changeCell(input, x, y, board);
    } else if (input=='n'){
        advanceSimulation(board);
    } else if (input=='q'){
        return 1;
    } else if (input=='p'){
        animate(board);
        return 2;
    }
    system("clear");
    displayBoard(board);
    fscanf(fp, "%c", &input); //trash '\n' character
    return 0;
}

void changeCell(char input, int x, int y, char board [][SIZE]){
    if (input=='a'){
        board[y][x]='X';
    } else if (input=='r'){
        board[y][x]=' ';
    }
}

void animate(char board [][SIZE]){
    while(1){
        system("clear");
        displayBoard(board);    
        usleep(100000);
        advanceSimulation(board);
    }
}

void advanceSimulation(char board [][SIZE]){
    char temp[SIZE][SIZE]={};
    for (int i = 0; i < SIZE; i++){
        for (int j = 0; j < SIZE; j++){
            int livingNeighbors = 0;
            for(int r = -1; r <= 1; r++){
                for(int c = -1; c <= 1; c++){
                    if(!(i+r<0||i+r>=SIZE||j+c<0||j+c>=SIZE)&&!(r==0&&c==0)&&board[i+r][j+c]=='X'){
                        livingNeighbors++;
                    }
                }
            }

            //rule a
            if (board[i][j]==' '){
                if(livingNeighbors==3){
                    temp[i][j]='X';
                } else {
                    temp[i][j]=' ';
                }
            }

            //rule b
            if (board[i][j]=='X'){
                if(livingNeighbors==3||livingNeighbors==2){
                    temp[i][j]='X';
                } else {
                    temp[i][j]=' ';
                }
            }
        }
    }

    //copy temp into original array
    for (int i = 0; i < SIZE; i++){
        for (int j = 0; j < SIZE; j++){
            board[i][j]=temp[i][j];
        }
    }
}