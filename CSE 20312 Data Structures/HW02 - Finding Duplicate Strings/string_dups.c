#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "string_methods.h"

int main(int argc, char *argv[]) {

    // TODO: Get the first line of input from stdin,
    // remove the final newline if necessary, and split
    // it into a string array, with ',' as the delimeter
    char line1[100];
    fgets(line1,sizeof(line1), stdin);
    string_chomp(line1);
    char** sv1 = string_split(line1, ',');

    // TODO: Get the second line of input from stdin,
    // remove the final newline if necessary, and split
    // it into a string array, with ',' as the delimeter
    char line2[100];
    fgets(line2,sizeof(line2), stdin);
    string_chomp(line2);
    char** sv2 = string_split(line2, ',');

    // TODO: Find the duplicate values and print them
    // to stdout
    char** sv = string_find_dups(sv1, sv2);
    int i =0;
    while(*(sv+i)!=NULL){
        printf("%s\n",*(sv+i));
        i++;
    }

    // TODO: Free anything that you allocated from the heap
    string_array_free(sv1);
    string_array_free(sv2);
    string_array_free(sv);

    return 0;
}