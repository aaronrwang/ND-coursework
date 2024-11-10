//Aaron Wang - Fund Comp - Lab 7 - states driver file - usastates.c
//Driver file for the states program
#include "statesfunc.h"
const int MAX_SIZE = 100;
int main(){
    srand(time(NULL));
    FILE* fp;
     char infile[30];
    printf("Enter a file name: ");
    scanf("%s", infile);

    fp = fopen(infile, "r");
    if (!fp){
        printf("file %s not found\n", infile);
        return 1;
    }

    state states[MAX_SIZE];
    int count = readFile(states, fp);
    fclose(fp);
    
    int choice = 0;
    while(choice != 6){
        displayMenu();
        scanf("%d", &choice);
        getchar();
        while(choice <1 || choice > 6){
            printf("Enter a VALID choice: ");
            scanf("%d", &choice);
            getchar();
        }
        printf("\n");
        if (choice == 1){
            displayData(states, count);
        } else if (choice == 2){
            capitals(states, count);
        } else if (choice == 3){
            abbreviations(states, count);
        } else if (choice == 4){
            statesBefore(states, count);
        } else if (choice == 5){
            statesAfter(states, count);
        }
    }
    printf("Goodbye!\n");
}
