#include "list.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LINE_SIZE 1024

int main() {
    char line[1024];
    while (fgets(line, LINE_SIZE, stdin)) {
        // Parse the line and append each data element to the tail of a linked list
        // using list_append_tail
        Node *head = NULL;
        char *token;
        token = strtok(line, " ");
        while (token != NULL){
            int n = atoi(token);
            head = list_append_tail(head, n);
            token = strtok(NULL, " ");
        }
        // Use list_merge_sort to sort the data
        head=list_merge_sort(head);
        // Print the sorted data using list_print
        list_print(head);
        // Free the list using list_delete
        list_delete(head);
    }
}