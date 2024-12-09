#include "set.h"
#include <stdio.h>
#include <string.h>

#define BUF_SIZE 1024

void chomp(char *s) {
    int len = strlen(s);
    if (s[len-1] == '\n') {
        s[len-1] = '\0';
    } 
}

bool is_palindromic(char *s) {
    // Return true if string s is a palindromic permutation
    // Use a set as part of your solution
    // TODO:
    Set *set = set_create();
    int count = 0;
    while(*s!='\0'){
        if(set_contains(set, *s)){
            set_remove(set, *s);
        } else {
            set_add(set, *s);
        }
        count++;
        s++;
    }
    count%=2;
    if(set->size==count){
        set_delete(set);
        return true;
    }
    set_delete(set);
    return false;

}

int main() {
    char buffer[BUF_SIZE];
    while (fgets(buffer, BUF_SIZE, stdin)) {
        chomp(buffer);
        if (is_palindromic(buffer)) {
            puts("YEAH");
        } else {
            puts("NOPE");
        }
    }
}