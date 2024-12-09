/* rpn.c: Reverse Polish Notation Calculator */

#include "stack.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Evaluate the given RPN expression using a stack.
 *
 * @param   expression	String containing RPN expression.
 * @return  Result of evaluating RPN expression using stack.
 **/
int evaluate_expression(char *expression) {
    // TODO
    // create a stack and declare other variables
    Stack *stack = stack_create();
    // Use strtok to get first token
    char* s = " ";
    char* token = strtok(expression, s);
    // while token available, process it using a stack
    
    while (token != NULL){
        int a;
        if(sscanf(token,"%d", &a)){
            stack_push(stack, a);
        } else {
            char c;
            sscanf(token,"%c", &c);
            if(stack_empty(stack)) return 0;
            a = stack_pop(stack);
            int b = stack_pop(stack);
            if(c=='+'){
                stack_push(stack, b+a);
            } else if (c=='-'){
                stack_push(stack, b-a);
            } else if (c=='*'){
                stack_push(stack, b*a);
            } else if (c=='/'){
                stack_push(stack, b/a);
            }
        }
        token = strtok(NULL, s);
    }
    if(stack_empty(stack)) return 0;
    int a = stack_pop(stack);
    stack_delete(stack);
    return a;
    // Get result, clean up, and return
}

/* Main Execution */
int main() {
    // TODO: For each line in standard input, evaluate the RPN expression
    // while(1){
    //     char* line = calloc(sizeof(char),99);
    //     fgets(line, 99, stdin); 
    //     printf("%d\n", evaluate_expression(line));
    //     free(line);  
    // }
    char line[1024];

    while (fgets(line, sizeof(line), stdin)) {
        int result = evaluate_expression(line);
        printf("%d\n", result);
    }
}
