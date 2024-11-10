//Aaron Wang - Fund Comp - Lab 5 - Part 2 mysayings.c
//Gives options to edit/view a database of sayings

#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define MAX 256

int giveChoice();
void displayAll(char [][MAX], int);
void addNewSaying(char [][MAX], int);
void displaySelected(char [][MAX], int);
void copyToFile(char [][MAX], int);

int main()
{
    //read in file
    FILE *fp;
    char infile[30];

    printf("Welcome to the Sayings Database!\n");
    printf("enter a file name: ");
    scanf("%s", infile);

    //check if file exists
    fp = fopen(infile, "r");    // connect to the file
    if (!fp) {                  // OR:  if (fp == NULL);
        printf("file %s not found\n", infile);
        return 1;
    }

    //read file into a 2d array
    char database[50][MAX] = {};
    int sayingsCount = 0;
    while (1){
        char line[MAX];
        
        fgets(line, MAX, fp); 
        if(feof(fp)) break; 
        sayingsCount++;
        line[strlen(line)-1] = '\0';
        strcpy(database[sayingsCount-1], line);
        
    }
    fclose(fp);

    int choice = giveChoice();

    while(choice!=5){
        if (choice == 1){
            displayAll(database,sayingsCount);
        } else if (choice == 2){
            addNewSaying(database,sayingsCount);
            sayingsCount++;
        } else if (choice == 3){
            displaySelected(database,sayingsCount);
        } else if (choice == 4){
            copyToFile(database,sayingsCount);
        }
        choice = giveChoice();
    }
    printf("Goodbye!\n");
    
}

int giveChoice(){
    int choice = 0;
    //menu
    printf("\nMenu of options\n");
    printf("1. display all sayings currently in the database\n");
    printf("2. enter a new saying into the database\n");
    printf("3. list sayings that contain a given substring entered by the user\n");
    printf("4. save all sayings in a new text file\n");
    printf("5. quit the program\n");
    printf("Choose your option: ");
    scanf("%d", &choice);
    //make sure option is valid
    while (choice < 1 || choice > 5){
        printf("Choose a VALID option: ");
        scanf("%d", &choice);
    }
    return choice;
}

void displayAll(char database[][MAX], int size){
    printf("\n");
    for (int i = 0 ; i < size; i++){
        printf(" - %s\n", database[i]);
    }
}

void addNewSaying(char database[][MAX], int size){

    //take new saying
    printf("Enter a saying: ");
    getchar();
    char line[256];
    fgets(line, 256, stdin);
    line[strlen(line)-1] = '\0';

    //write to array
    strcpy(database[size],line);
}

void displaySelected(char database[][MAX], int size){


    //take substring, find length and set new line to null to end string
    printf("Enter substring: ");
    getchar();
    char substring[256];
    fgets(substring, 256, stdin);
    substring[strlen(substring)-1] = '\0';
    printf("\n");


    //check for substring in line and print if true
    for (int i = 0; i < size; i++){
        if(strstr(database[i],substring)!=NULL){
            printf("-> %s\n",database[i]);
        }                   
    }
}

void copyToFile(char database[][MAX], int size){
    char outfile[30];

    printf("enter a file name: ");
    scanf("%s", outfile);

    FILE *output = fopen(outfile, "w");

    for (int i = 0; i < size; i++){
        char line[256];
        strcpy(line,database[i]);
        int l = strlen(line);
        line[l] = '\n';
        fwrite(line,1,l+1,output);
    }
    fclose(output);
}