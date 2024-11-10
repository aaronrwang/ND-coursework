#include <stdio.h>
#include <math.h>

int main(){
	float principal, rate, monthlyPayment;
	int time;
	printf("This program takes your principal, interest rate, and monthly payment.\n");
	printf("It returns the amount of time (months) to pay off the loan.\n");
//scan for principal
	printf("Principal: ");
	scanf("%f", &principal);
	while (principal < 0){
		printf("Re-enter value, must be positive: ");
		scanf("%f", &principal);
	}
//scan for interest rate
	printf("Interest Rate: ");
	scanf("%f", &rate);
	while (rate < 0){
		printf("Re-enter value, must be positive: ");
		scanf("%f", &rate);
	}
	float minMonthlyPayment = principal*rate/1200;
//scan for monthly payment
	printf("Monthly Payment: ");
	scanf("%f", &monthlyPayment);
	while (monthlyPayment < minMonthlyPayment){
		printf("Re-enter value or you will always be in debt: ");
		scanf("%f", &monthlyPayment);
	}
//Set up variables
	float balance = principal;
	float monthlyRate = rate/1200;
	float total = 0;
//table header
	printf("Month     ");
	printf("Payment    ");
	printf("Interest     ");
	printf("Balance\n");
//calculate and print table
	while (balance > 0){
		time++;
		float interest = balance * monthlyRate;
		balance+=interest-monthlyPayment;
		if (balance < 0){
			monthlyPayment+=balance;
			balance=0;
		}
		total+=monthlyPayment;
		printf("%d\t  $%6.2lf", time, monthlyPayment);
		printf("    $%6.2lf\t", round(interest*100)/100);
		printf("$%8.2lf\n", round(balance*100)/100);
	}
	printf("You paid a total of $%.2f over %d years and %d months.\n", total, time/12, time%12);
	return 0;
}
