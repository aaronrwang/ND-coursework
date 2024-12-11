#include "string_array.h"
#include "utilities.h"
#include "unit_assert.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <assert.h>

bool test_00_string_array_create(){
    string_array* array = string_array_create();
    unit_assert(array->size == 0);
    unit_assert(array->capacity == ARRAY_DEFAULT_CAPACITY);
    free(array->data);
    free(array);
    return EXIT_SUCCESS;
}

bool test_01_string_array_delete() {
    string_array* array = string_array_create();
    string_array_delete(array);
    return EXIT_SUCCESS;
}

bool test_02_string_array_append() {
    string_array* array = string_array_create();
    string_array_append(array, "apple");
    string_array_append(array, "banana");
    string_array_append(array, "cherry");
    string_array_append(array, "durian");
    unit_assert(array->size == 4);
    unit_assert(array->capacity == 4);
    string_array_append(array, "elderberry");
    unit_assert(array->size == 5);
    unit_assert(array->capacity == 8);
    unit_assert(!strcmp(array->data[0], "apple"));
    unit_assert(!strcmp(array->data[1], "banana"));
    unit_assert(!strcmp(array->data[2], "cherry"));
    unit_assert(!strcmp(array->data[3], "durian"));
    unit_assert(!strcmp(array->data[4], "elderberry"));
    string_array_delete(array);
    return EXIT_SUCCESS;
}

bool test_03_string_array_at() {
    string_array* array = string_array_create();
    string_array_append(array, "apple");
    string_array_append(array, "banana");
    string_array_append(array, "cherry");
    string_array_append(array, "durian");
    string_array_append(array, "elderberry");
    unit_assert(!strcmp(string_array_at(array, 0), "apple"));
    unit_assert(!strcmp(string_array_at(array, 1), "banana"));
    unit_assert(!strcmp(string_array_at(array, 2), "cherry"));
    unit_assert(!strcmp(string_array_at(array, 3), "durian"));
    unit_assert(!strcmp(string_array_at(array, 4), "elderberry"));
    string_array_delete(array);
    return EXIT_SUCCESS;
}

bool test_04_string_array_index() {
    string_array* array = string_array_create();
    string_array_append(array, "apple");
    string_array_append(array, "banana");
    string_array_append(array, "cherry");
    string_array_append(array, "durian");
    string_array_append(array, "elderberry");
    unit_assert(string_array_index(array, "apple") == 0);
    unit_assert(string_array_index(array, "elderberry") == 4);
    unit_assert(string_array_index(array, "grape") == -1);
    string_array_delete(array);
    return EXIT_SUCCESS;
}

bool test_05_string_array_insert() {
    string_array* array = string_array_create();
    string_array_append(array, "banana");
    string_array_append(array, "cherry");
    string_array_append(array, "elderberry");
    string_array_insert(array, 0, "apple");
    unit_assert(array->size == 4);
    unit_assert(array->capacity == 4);
    unit_assert(!strcmp(array->data[0], "apple"));
    unit_assert(!strcmp(array->data[1], "banana"));
    unit_assert(!strcmp(array->data[2], "cherry"));
    string_array_insert(array, 3, "durian");
    unit_assert(array->size == 5);
    unit_assert(array->capacity == 8);
    unit_assert(!strcmp(array->data[3], "durian"));
    unit_assert(!strcmp(array->data[4], "elderberry"));
    string_array_delete(array);
    return EXIT_SUCCESS;
}

bool test_06_string_array_remove() {
    string_array* array = string_array_create();
    string_array_append(array, "apple");
    string_array_append(array, "banana");
    string_array_append(array, "cherry");
    string_array_append(array, "durian");
    string_array_remove(array, 0);
    unit_assert(array->size == 3);
    unit_assert(!strcmp(array->data[0], "banana"));
    unit_assert(!strcmp(array->data[2], "durian"));
    string_array_remove(array, 1);
    unit_assert(array->size == 2);
    unit_assert(!strcmp(array->data[0], "banana"));
    unit_assert(!strcmp(array->data[1], "durian"));
    string_array_remove(array, 1);
    unit_assert(array->size == 1);
    unit_assert(!strcmp(array->data[0], "banana"));
    string_array_delete(array);
    return EXIT_SUCCESS;
}

bool test_07_string_array_sort() {
    string_array* array = string_array_create();
    char* sorted[10]   = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"};
    char* unsorted[10] = {"c", "a", "h", "d", "e", "j", "g", "b", "f", "i"};
    for (int i = 0;  i < 10;  i++) {
        string_array_append(array, unsorted[i]);
    }
    string_array_sort(array);
    unit_assert(compare_array_of_strings(array->data, sorted, 10));
    string_array_delete(array);
    return EXIT_SUCCESS;
}


/* Main Execution */

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s NUMBER\n\n", argv[0]);
        fprintf(stderr, "Where NUMBER is right of the following:\n");
        fprintf(stderr, "    0  Test string_array_create\n");
        fprintf(stderr, "    1  Test string_array_delete\n");
        fprintf(stderr, "    2  Test string_array_append\n");
        fprintf(stderr, "    3  Test string_array_at\n");
        fprintf(stderr, "    4  Test string_array_index\n");
        fprintf(stderr, "    5  Test string_array_insert\n");
        fprintf(stderr, "    6  Test string_array_remove\n");
        fprintf(stderr, "    7  Test string_array_sort\n");
        return EXIT_FAILURE;
    }   

    int number = atoi(argv[1]);
    int status = EXIT_FAILURE;

    switch (number) {
        case 0:  status = test_00_string_array_create(); break;
        case 1:  status = test_01_string_array_delete(); break;
        case 2:  status = test_02_string_array_append(); break;
        case 3:  status = test_03_string_array_at();     break;
        case 4:  status = test_04_string_array_index();  break;
        case 5:  status = test_05_string_array_insert(); break;
        case 6:  status = test_06_string_array_remove(); break;
        case 7:  status = test_07_string_array_sort();   break;
        default: fprintf(stderr, "Unknown NUMBER: %d\n", number); break;
    }
    
    if (status == EXIT_SUCCESS) {
        printf("Unit test passed\n");
    }
    return status;
}