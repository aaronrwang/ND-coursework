//Aaron Wang - Fund Comp - Lab 7 - states function file - statesfunc.c
//Contains functions for states program
#include "statesfunc.h"

void lowerString(char str[]){
    int i=0;
    while(str[i]!='\0'){
        str[i]=tolower(str[i]);
        i++;
    }
}

void displayData(state states[], int count){
    for (int i = 0; i < count; i++){
        printf("%s,%s,%s,%d\n",states[i].abbreviation, states[i].name, states[i].capital, states[i].year);
    }
    printf("\n");
}

void capitals(state states[], int count){
    int numQuestions;
    printf("Enter desired number of questions: ");
    scanf("%d", &numQuestions);
    getchar();
    while(numQuestions<1){
        printf("Enter a positive number: ");
        scanf("%d", &numQuestions);
        getchar();
    }
    printf("\n");
    int score = 0;
    for (int i = 1; i <= numQuestions; i++){
        int n = rand() % count;
        printf("%d. Capital of %s: ",i, states[n].name);
        char answer[256];
        fgets(answer, 256, stdin);
        answer[strlen(answer)-1] = '\0';
        lowerString(answer);
        if (!strcmp(answer, states[n].capital)){
            score++;
            printf("Correct!\n\n");
        } else {
            printf("The right answer was %s.\n\n", states[n].capital);
        }
    }
    printf("You got %d/%d correct.\n\n", score, numQuestions);
}

void abbreviations(state states[], int count){
    int numQuestions;
    printf("Enter desired number of questions: ");
    scanf("%d", &numQuestions);
    getchar();
    while(numQuestions<1){
        printf("Enter a positive number: ");
        scanf("%d", &numQuestions);
        getchar();
    }
    printf("\n");
    int score = 0;
    for(int i = 1; i <= numQuestions; i++){
        int n = rand() % count;
        printf("%d. Abbreviation for %s: ", i, states[n].name);
        char answer[256];
        fgets(answer, 256, stdin);
        answer[strlen(answer)-1] = '\0';
        lowerString(answer);
        if (!strcmp(answer, states[n].abbreviation)){
            score++;
            printf("Correct!\n\n");
        } else {
            printf("The right answer was %s.\n\n", states[n].abbreviation);
        }
    }
    printf("You got %d/%d correct.\n\n", score, numQuestions);
}

void statesBefore(state states[], int count){
    printf("Enter a year: ");
    int n = 0;
    scanf("%d", &n);
    getchar();
    int displayCounter = 0;
    for(int i = 0; i < count; i++){
        if(states[i].year<n){
            printf("%s\n",states[i].name);
            displayCounter++;
        }
    }
    if(displayCounter==0){
        printf("There are no states that match this criteria.\n");
    }
    printf("\n");
}

void statesAfter(state states[], int count){
    printf("Enter a year: ");
    int n = 0;
    scanf("%d", &n);
    getchar();
    int displayCounter = 0;
    for(int i = 0; i < count; i++){
        if(states[i].year>n){
            printf("%s\n",states[i].name);
            displayCounter++;
        }
    }
    if(displayCounter==0){
        printf("There are no states that match this criteria.\n");
    }
    printf("\n");
}

void displayMenu(){
    printf("1: Display all info.\n");
    printf("2: Capitals Quiz.\n");
    printf("3: Abbreviations Quiz.\n");
    printf("4: Display states that joined before n year.\n");
    printf("5: Display states that joined after n year.\n");
    printf("6: Quit Program\n");
    printf("Enter choice: ");
}

int readFile(state states[], FILE* fp){
    int count = -1;
    while(1){
        if(feof(fp)) break;
        count++;
        char line[250];
        fgets(line, 250, fp);
        char *token = strtok(line, ",");
        strcpy(states[count].abbreviation, token);
        token = strtok(NULL, ",");
        if (token == NULL) continue;
        strcpy(states[count].name, token);
        token = strtok(NULL, ",");
        if (token == NULL) continue;
        strcpy(states[count].capital, token);
        token = strtok(NULL, ",");
        if (token == NULL) continue;
        states[count].year = atoi(token);
        lowerString(states[count].abbreviation);
        lowerString(states[count].name);
        lowerString(states[count].capital);
    }
    return count;
}