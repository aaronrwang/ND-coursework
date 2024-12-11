#pragma once

#include <stdbool.h>

int     binary_search(char **strings, int size, char *key);
int     binary_search_insert_index(char **strings, int size, char *key);
int     partition(char **strings, int low_index, int high_index);
void    quicksort(char **strings, int low_index, int high_index);
bool    string_isalpha(char *str);
char   *string_tolower(char *str);
bool    compare_array_of_strings(char **s1, char **s2, int n);
