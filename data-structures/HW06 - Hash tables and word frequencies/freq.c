#include "table.h"
#include "string_utils.h"

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define WHITESPACE  " \t\r\n"

int	main() {
    double alpha = 0.5;

    Table *t = table_create(0, alpha);
    char buffer[BUFSIZ];

    /* Read input and insert or update frequency counts in table */
    while (fgets(buffer, BUFSIZ, stdin)) {
        char* s = " ";
        char* token = strtok(buffer, s);
        while (token!= NULL){
            char* word = str_trim(str_lower(token));
            if (*word){
                int count = table_lookup(t,word);
                if (count==-1) count++;
                table_insert_or_update(t,word,count+1);
            }
            token = strtok(NULL, s);
        }
    }

    table_print(t, stdout);
    table_delete(t);
}