#pragma once

/* Constants */
#define ARRAY_DEFAULT_CAPACITY 1 << 2

/* Structure */

typedef struct {
    char **data;	   // Internal array
    int    capacity;   // Total number of elements
    int    size;	   // Number of valid elements
} string_array;

/* Functions */

string_array*   string_array_create();
void            string_array_delete(string_array *array);
void            string_array_append(string_array *array, char *str);
char*           string_array_at(string_array *array, int index);
int             string_array_index(string_array *array, char *str);
void            string_array_insert(string_array *array, int index, char *str);
void            string_array_remove(string_array *array, int index);
void            string_array_sort(string_array *array);
