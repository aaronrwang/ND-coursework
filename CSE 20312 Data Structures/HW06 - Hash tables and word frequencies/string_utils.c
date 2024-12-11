#include "string_utils.h"

#include <ctype.h>
#include <string.h>
#include <stdio.h>

/**
 * Convert all the characters in the string to lowercase.
 *
 * @param   s       String to convert.
 * @return  Pointer to the first character in string.
 **/
char *	str_lower(char *s) {
    // TODO:
    int i = 0;
    while(*(s+i)){
        *(s+i) = tolower(*(s+i));
        i++;
    }
    return s;
}

/**
 * Trim front and back of string of any non-alphanumeric characters.
 *
 * @param   s       String to convert.
 * @return  Pointer to the first alphanumeric character in string.
 **/
char *	str_trim(char *s) {
    // TODO:
    // Check for null or empty string
    if (s == NULL || *s == '\0') {
        return s;
    }

    // Move head pointer to the first alphanumeric character
    char *head = s;
    while (*head && !isalnum((unsigned char)*head)) {
        head++;
    }

    // If the entire string is non-alphanumeric
    if (*head == '\0') {
        *head = '\0'; // Null-terminate the string
        return head;
    }

    // Move tail pointer to the last alphanumeric character
    char *tail = head;
    while (*tail) {
        tail++;
    }
    tail--; // Move back to the last character

    while (tail >= head && !isalnum((unsigned char)*tail)) {
        tail--;
    }

    // Null-terminate the trimmed string
    *(tail + 1) = '\0';

    // Return the pointer to the first alphanumeric character
    return head;
}
