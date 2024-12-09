#include <stdio.h>
#include <string.h>

// typedef struct{
//     char word[16];
    
//     char scramble[16];
//     int use;
//     int x;
//     int y;
// } word;

int readFile(FILE*, char[20][16]);
void sort(char[20][16],char[20][16], int);
void displayBoard(char[15][15]);
int addFirstWord(char[15][15],char[16]);
int main(int argc, char *argv[]){
    char input[20][16] = {};
    char board[15][15] = {};
    int count;
    if(argc==1){
        count = readFile(stdin, input);
    } else if (argc==2){
        FILE *fp = fopen(argv[1],"r");
        if (!fp) {
            printf("file %s not found\n", argv[1]);
            return 2;
        }
        count = readFile(fp, input);
    } else {
        printf("Too many arugments.\nProper usage: %s file.txt", argv[0]);
    }
    // printf("\n\n");
    // for (int i = 0; i < count; i++){
    //     printf("%d: %s\n",i, input[i]);
    // }
    
    char words[20][16]={};
    sort(words, input, count);
    int used[20] = {};
    used[0] = addFirstWord(board, words[0]);
    displayBoard(board);
    // printf("\n\n");
    // for (int i = 0; i < count; i++){
    //     printf("%d: %s\n", i, words[i]);
    // }
    
    //addFirstWord();
    // while(1){
    //     addWord();
    // }
}

int readFile(FILE *fp, char input[20][16]){
    char temp[16] = {};
    int count = 0;
    while(count < 20){
        fscanf(fp, "%s", temp);
        if(!strcmp(temp,".")) break;
        strcpy(input[count],temp);
        count++;
    }
    return count;
}

void sort(char words[20],char input[20][16], int count){
    int index = 0;
    for (int i = 15; i >=0; i--){
        for (int j = 0; j < count; j++){
            if(strlen(input[j])==i){
                strcpy(words.[index],input[j]);
                index++;
            }
        }
    }
}

int addFirstWord(char board[15][15],char word[16]){
    int l = strlen(word);
    //account for over 15?
    for (int i = 0; i < l; i++){
        board[7][7-l/2+i]=word[i];
    }
    return 1;
}

int addWord(char board[15][15], char word[16]){
    int l = strlen(word);
    for (int i = 0; i < 15; i++){
        for (int j = 0; j < 15; j++){
            for (int k = 0; k < l; k++){
                if(board[i][j]==word[k]){
                    int valid = 1;
                    //check horizontal
                    if(j-k >= 0||j-k+l<15){
                        for (int h = 0; h < k; h++){
                        if(board[i][j-k+h]!='\0'){
                            valid = 0;
                            break;
                        }
                    }
                    }
                    
                    //check vertical
                    for (int h = 0; h < k; h++){
                        if(board[i-j+h][k])
                    }
                }
            }
            
        }
    }
}

void displayBoard(char board[15][15]){
    printf("+---------------+\n");
    for (int i = 0; i < 15; i++){
        printf("|");
        for (int j = 0; j < 15; j++){
            if (board[i][j]!='\0'){
                printf("%c", board[i][j]);
            } else {
                printf(".");
            }
            
        }
        printf("|\n");
    }
    printf("+---------------+\n");
}
