// menucalc.c - Aaron Wang - Fund Comp - Lab 3 - Part 3
// This is a simple calculator 
#include <stdio.h>

void addition(float n, float m);
void subtraction(float n, float m);
void multiplication(float n, float m);
void division(float n, float m);
void printCalculation(char operator, float n, float m, float result);
int calculation();

int main(){
	
	//sets the choice to a valid int that will later correspond to a symbol
	int choice = calculation();

	//Do calculation, print and then ask for new numbers;
	while (choice != 0){	

		//ask for numbers
		float n, m;
		printf("Enter two numbers in order: ");
		scanf("%f %f", &n, &m);

		//does calculation and prints results
		if (choice == 1){
			addition(n,m);
		} else if (choice == 2){
			subtraction(n,m);
		} else if (choice == 3){
			multiplication(n,m);
		} else if (choice == 4){
			if (m != 0){	
				division(n,m);
			} else {
				printf("Error: Can not divide by zero\n\n");
			}
		}
		choice=calculation();
	}
	printf("GoodBye!\n");
}

int calculation(){
	int choice;
	printf("What would you like to do?\n 0 to quit\n 1 for addition\n 2 for subtraction\n 3 for multiplication\n 4 for division\nEnter your choice: ");
	scanf("%d", &choice);

	//make sure choice is valid
	while (choice < 0 || choice > 4){
		scanf("%d", &choice);
	}
	return choice;
}

void addition(float n, float m){
	float result = n + m;
	printCalculation('+',n,m,result);
}

void subtraction(float n, float m){
	float result = n - m;
	printCalculation('-',n,m,result);
}

void multiplication(float n, float m){
	float result = n * m;
	printCalculation('*',n,m,result);
}

void division(float n, float m){
	float result = n / m;
	printCalculation('/',n,m,result);
}

void printCalculation(char operator, float n, float m, float result){
	printf("(%f) %c (%f)=%f\n\n", n, operator, m, result);
}
