#include "string_array.h"
#include "utilities.h"

#include <assert.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

string_array *string_array_create() {
    // Allocate string_array structure, exit if it fails
    string_array *sarray = malloc(sizeof(string_array));

    // Initialize capacity and size
    sarray->capacity = ARRAY_DEFAULT_CAPACITY;
    sarray->size = 0;

    // Allocate the data sarray, exit if it fails
    sarray->data = calloc(sarray->capacity, sizeof(char*));

    // return pointer to string_array
    return sarray;
}

void string_array_delete(string_array *sarray) {
    // free the strings
    for (int i = 0;  i < sarray->size;  i++) {
        free(sarray->data[i]);
    }

    // Free the data sarray
    free(sarray->data);

    // Free the string_array structure
    free(sarray);
}

void string_array_append(string_array *sarray, char *str) {
    // If the size is at capacity, double the capacity, exit if it fails
    if (sarray->size == sarray->capacity) {
        sarray->capacity *= 2;  // Double the capacity
        sarray->data = realloc(sarray->data, sarray->capacity * sizeof(string_array *));
    }

    // Store value at end of sarray and increment size
    sarray->data[sarray->size] = strdup(str);
    sarray->size++;
}

char* string_array_at(string_array *sarray, int index) {
    // Make sure index is in bounds
    assert(index < sarray->size && index >= 0);
    // Return the value at the index
    return sarray->data[index];
}

int string_array_index(string_array *sarray, char *str) {
    // Scan internal sarray for first element
    // that matches value and return its index         
    for (int index = 0; index < sarray->size; index++)
        if (strcmp(sarray->data[index], str) == 0) {
            return index;
        }

    // Return -1 if no match found
    return -1;
}

void string_array_insert(string_array *sarray, int index, char *str) {
    // If the size is at capacity, double the capacity
    if (sarray->size == sarray->capacity) {
        sarray->capacity *= 2;  // Double the capacity
        sarray->data = realloc(sarray->data, sarray->capacity * sizeof(char*));
    }

    // Shift the values from index to the end of the sarray one element ahead
    for (int i = sarray->size; i > index; i--) {
        sarray->data[i] = sarray->data[i-1];
    }

    // Store new value and increment size
    sarray->data[index] = strdup(str);
    sarray->size++;
}

void string_array_remove(string_array *sarray, int index) {
    // Remove the element at index, shifting elements that follow to the left
    // TODO: 
    free(sarray->data[index]);
    for (int i = index;  i < sarray->size - 1;  i++) {
        sarray->data[i] = sarray->data[i+1];
    }
    sarray->size--;
}

void string_array_sort(string_array *sarray) {
    quicksort(sarray->data, 0, sarray->size - 1);
}
