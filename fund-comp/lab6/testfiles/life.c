#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#define SIZE 40

char board [SIZE][SIZE];

void displayBoard();
void clearBoard();
void animate();
void advanceSimulation();
int move(FILE*);
void changeCell(char, int, int);

int main(int argc, char *argv[]){

    if (argc==1){
        clearBoard();
        displayBoard();

        //iterate through actions
        int option = 0;
        while(!option){
            option=move(stdin);
        }
    } else if (argc==2){
        FILE *fp = fopen(argv[1],"r"); //open file return null if no file
        if (!fp) {
            printf("file %s not found\n", argv[1]);
            return 2;
        }

        clearBoard();

        //iterate through file commands
        int option = 0;
        while (!option){
            option = move(fp);
        } 
    } else{
        printf("Too many arguments\n");
        return 1;
    }
    return 0;
}

void clearBoard(){
    for (int i = 0; i < SIZE; i++){
        for (int j = 0; j < SIZE; j++){
            board[i][j]=' ';
        }
    }
}

void displayBoard(){

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

int move(FILE *fp){
    char input;
    int x,y;
    fscanf(fp, "%c", &input);
    if(input=='a'||input=='r'){
        fscanf(fp, "%d %d", &x, &y);
        printf("%c: %d %d\n", input, x, y);
        changeCell(input, x, y);
    } else if (input=='n'){
        advanceSimulation();
    } else if (input=='q'){
        return 1;
    } else if (input=='p'){
        animate();
        return 2;
    }
    system("clear");
    displayBoard();
    fscanf(fp, "%c", &input); //trash '\n' character
    return 0;
}

void changeCell(char input, int x, int y){
    if (input=='a'){
        board[y][x]='X';
    } else if (input=='r'){
        board[y][x]=' ';
    }
}

void animate(){
    while(1){
        system("clear");
        displayBoard();    
        usleep(100000);
        advanceSimulation();
    }
}

void advanceSimulation(){
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