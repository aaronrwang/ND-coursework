//Aaron Wang- Fund Comp - Lab 4 - part 3 ndfootball.c
//Gives people data about ND Football seasons
#include <stdio.h>

int wins[] = 
 { 6, 8, 6, 8, 5, 5, 6, 6, 8, 7, 4, 6,
   7, 7, 6, 7, 8, 6, 3, 9, 9, 10, 8, 9,
   10, 7, 9, 7, 5, 9, 10, 6, 6, 3, 6, 7, 
   6, 6, 8, 7, 7, 8, 7, 9, 8, 7, 8, 9,
   9, 10, 4, 7, 7, 9, 9, 8, 2, 7, 6, 5, 
   2, 5, 5, 2, 9, 7, 9, 8, 7, 8, 10, 8, 
   8, 11, 10, 8, 9, 11, 9, 7, 9, 5, 6, 7, 
   7, 5, 5, 8, 12, 12, 9, 10, 10, 11, 6, 9, 
   8, 7, 9, 5, 9, 5, 10, 5, 6, 9, 10, 3, 
   7, 6, 8, 8, 12, 9, 8, 10, 4, 10, 12, 11, 
   10, 11, 9, 10 };

int losses[] = 
 { 3, 1, 2, 0, 3, 4, 1, 0, 1, 0, 1, 0,
   0, 0, 2, 1, 1, 1, 1, 0, 0, 1, 1, 1,
   0, 2, 1, 1, 4, 0, 0, 2, 2, 5, 3, 1,
   2, 2, 1, 2, 2, 0, 2, 1, 2, 2, 0, 0,
   0, 0, 4, 2, 2, 0, 1, 2, 8, 3, 4, 5,
   8, 5, 5, 7, 1, 2, 0, 2, 2, 2, 1, 2,
   3, 0, 2, 3, 3, 1, 3, 4, 2, 6, 4, 5,
   5, 6, 6, 4, 0, 1, 3, 3, 1, 1, 5, 3,
   3, 6, 3, 7, 3, 6, 3, 7, 6, 3, 3, 9,
   6, 6, 5, 5, 1, 4, 5, 3, 8, 3, 1, 2,
   2, 2, 4, 3 };

void displayYearsWithBlankWins();
void displayYearsWithBlankLosses();
void displayNumberOfYearsWithBlankWins();
void displayNumberOfYearsWithBlankLosses();
void displayRecordForAGivenYear();

int main(){
	int end = 0;
	while (end == 0){

		//display options
		int option = 0;
		printf("Choose what you want to know about Notre Dame Football: \n");
		printf("1: Display years with n wins\n");
		printf("2: Display years with n losses\n");
		printf("3: Display # of years with n wins\n");
		printf("4: Display # of years with n losses\n");
		printf("5: Display the record for a given year\n");
		printf("6: Exit program\n");
		printf("Enter your choice: ");
		scanf("%d", &option);
		
		//make sure input is valid
		while(option < 1 || option > 6){
			printf("Enter VALID choice: ");
			scanf("%d", &option);
		}
		//give right information according to option
		if (option == 1){
			displayYearsWithBlankWins();	
		} else if (option == 2){
			displayYearsWithBlankLosses();	
		} else if (option == 3){
			displayNumberOfYearsWithBlankWins();
		} else if (option == 4){
			displayNumberOfYearsWithBlankLosses();
		} else if (option == 5){
			displayRecordForAGivenYear();
		} else if (option == 6){
			end = 1;
			printf("Goodbye!\n");
		}
		
	}
}

void displayYearsWithBlankWins(){
	int n;
	printf("Enter number of wins: ");
	scanf("%d", &n);
	int count = 0;	
	//cycle through and when wins match print
	for (int i = 0; i < sizeof(wins)/sizeof(wins[0]); i++){
		if(wins[i] == n){
			printf("%d\n", i+1900);
			count++;
		}
	}
	if (count==0){
		printf("NONE\n");
	}
	printf("\n");
}

void displayYearsWithBlankLosses(){
	int n;
	printf("Enter number of losses: ");
	scanf("%d", &n);
	int count = 0;
	//cycle through and when losses match print
	for (int i = 0; i < sizeof(losses)/sizeof(losses[0]); i++){
		if(losses[i] == n){
			printf("%d\n", i+1900);
			count++;
		}
	}
	if (count==0){
		printf("NONE\n");
	}
	printf("\n");
}

void displayNumberOfYearsWithBlankWins(){
	int n;
	printf("Enter number of wins: ");
	scanf("%d", &n);
	int count = 0;
	//cycle through and when losses add
	for (int i = 0; i < sizeof(wins)/sizeof(wins[0]); i++){
		if(wins[i] == n){
			count++;
		}
	}
	printf("There were %d years where ND won %d games.\n",count,n);
}

void displayNumberOfYearsWithBlankLosses(){
	int n;
	printf("Enter number of losses: ");
	scanf("%d", &n);
	int count = 0;
	//cycle through and when losses add
	for (int i = 0; i < sizeof(losses)/sizeof(losses[0]); i++){
		if(losses[i] == n){
			count++;
		}
	}
	printf("There were %d years where ND lost %d games.\n\n",count,n);
}


void displayRecordForAGivenYear(){
	int MAX_YEAR = sizeof(wins)/sizeof(wins[0])+1900;
	printf("Enter year: ");

	//get valid input
	int n;
	scanf("%d", &n);
	while(n<1900||n>MAX_YEAR){
		printf("Enter valid year (1900-present): ");
		scanf("%d", &n);
	}

	//convert to array index
	n-=1900;

	//print
	printf("%d: Wins: %d Losses: %d\n\n", n+1900, wins[n], losses[n]);
}
