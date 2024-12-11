#include "func.h"

void upperCase(Word words[20], int count){
    for(int i = 0; i < count; i++){
        int l = strlen(words[i].str);
        for(int j = 0; j < l; j++){
            words[i].str[j]=toupper(words[i].str[j]);
        }
    }
}

Word scramble (Word word){
    strcpy(word.scramble,word.str);
    int l = strlen(word.scramble);

    //choose a random index to switch with the first character 100 times to randomize
    for (int j = 0; j < 100; j++){
        int k = rand()%l;
        char temp = word.scramble[0];
        word.scramble[0] = word.scramble[k];
        word.scramble[k] = temp;
    }
    return word;
}
int readFile(FILE *fp, char input[20][16]){
    char temp[100] = {};
    int count = 0;
    while(count < 20){
        fscanf(fp, "%s", temp);
        if(!strcmp(temp,".")) break;
        int l = strlen(temp);
        if(l<2 || l > 15){
            printf("Word is too short.\n");
            continue;
        }
        int flag = 0;
        for(int i = 0; i < l; i++){
            if(!isalpha(temp[i])){
                flag = 1;
                break;
            }
        }
        if(flag){
            printf("Word contains nonalphabetical characters.\n");
            continue;
        }
        strcpy(input[count],temp);
        count++;
    }
    return count;
}

void sort(Word words[20],char input[20][16], int count){
    int index = 0;

    //goes from 15 to 2; if it finds a word of that lenght it adds it to the struct array
    for (int i = 15; i >=1; i--){
        for (int j = 0; j < count; j++){
            if(strlen(input[j])==i){
                strcpy(words[index].str,input[j]);
                index++;
            }
        }
    }
}

void addFirstWord(char board[15][15],Word words[20]){
    int l = strlen(words[0].str);
    words[0].x=7-l/2;
    words[0].y=7;
    words[0].use=1;
    for (int i = 0; i < l; i++){
        board[7][7-l/2+i]=words[0].str[i];
    }
}

int addWord(char board[15][15], Word words[20], int id, int count){
    displayWord(words[2]);
    int l1 = strlen(words[id].str);
    for(int i = 0; i < l1; i++){
        char checkFor = words[id].str[i]; //saves char from the word trying to fit in
        for (int j = 0; j < count && words[j].use != 0; j++){
            int l2 = strlen(words[j].str);
            for(int k = 0; k < l2; k++){
                if (checkFor==words[j].str[k]){ //finds a matching char already on the board
                    int flag = 1;
                    if (words[j].use==1){ //checks proper conditions assuming the word already on the board is horizontal
                        int x = words[j].x+k;
                        int y = words[j].y-i;
                        if (y<0||y+l1>15) break; //check if word fits on board
                        if (y!=0 && board[y-1][x]!='\0') break; //check if character above is null
                        if (y+l1!=15 && board[y+l1][x]!='\0') break; //check if character bellow is null
                        for(int r = 0; r < l1; r++){
                            if(board[y+r][x] && y+r != words[j].y){
                                flag = 0;
                                break;
                            } 
                        }
                        if(x-1>=0){
                            for(int r = 0; r < l1; r++){
                                if(board[y+r][x-1] && y+r != words[j].y){
                                    flag = 0;
                                    break;
                                } 
                            }
                        } // check left of word
                        if(x+1<15){
                            for(int r = 0; r < l1; r++){
                                if(board[y+r][x+1] && y+r != words[j].y){
                                    flag = 0;
                                    break;
                                } 
                            }
                        } // check right of word
                        if(flag){
                            words[id].x=x;
                            words[id].y=y;
                            words[id].use = 2;
                            for (int s = 0; s < l1; s++){
                                board[y+s][x]=words[id].str[s];
                            }
                            return 1;
                        }
                    } else if (words[j].use==2){ //checks proper conditions assuming the word already on the board is vertical
                        int x = words[j].x-i;
                        int y = words[j].y+k;
                        if (x<0||x+l1>15) break; //check if word fits on board
                        if (x!=0 && board[y][x-1]!='\0') break; //check if character left is null
                        if (x+l1!=15 && board[y][x+l1]!='\0') break; //check if character right is null
                        for(int c = 0; c < l1; c++){
                            if(board[y][x+c] && x+c != words[j].x){
                                flag = 0;
                                break;
                            } 
                        }
                        if(y-1>=0){
                            for(int c = 0; c < l1; c++){
                                if(board[y-1][x+c] && x+c != words[j].x){
                                    flag = 0;
                                    break;
                                } 
                            }
                        } // check above of word
                        if(x+1<15){
                            for(int c = 0; c < l1; c++){
                                if(board[y+1][x+c] && x+c != words[j].x){
                                    flag = 0;
                                    break;
                                } 
                            }
                        } // check below of word
                        if(flag){
                            words[id].x=x;
                            words[id].y=y;
                            words[id].use = 1;
                            for (int s = 0; s < l1; s++){
                                board[y][x+s]=words[id].str[s];
                            }
                            return 1;
                        }
                    }
                }
            }
        }
    }
    printf("%s could not be placed in crossword.\n", words[id].str);
    return 0;
}

void displaySolution(char board[15][15]){
    printf("Solution:\n");
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

void displayBoard(char board[15][15]){
    printf("Crossword Puzzle:\n");
    printf("+---------------+\n");
    for (int i = 0; i < 15; i++){
        printf("|");
        for (int j = 0; j < 15; j++){
            if (board[i][j]!='\0'){
                printf(" ");
            } else {
                printf("#");
            }
            
        }
        printf("|\n");
    }
    printf("+---------------+\n");
}

void printClues(Word words[20], int count){
    printf("Clues:\n");
    for (int i = 0; i < count; i++){
        if (words[i].use==1||words[i].use==2){
            printf("%2d, %2d",words[i].x,words[i].y);
            if (words[i].use==1){
                printf(" Down\t");
            } else {
                printf(" Across\t");
            }
            printf("%s\n", words[i].scramble);
        }
    }
}

void displayWord(Word word){
    printf("%s, %s, %d, %d, %d\n",word.str,word.scramble,word.use,word.x,word.y);
}