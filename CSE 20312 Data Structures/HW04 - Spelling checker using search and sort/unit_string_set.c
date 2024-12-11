#include "string_set.h"
#include "utilities.h"
#include "unit_assert.h"

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool test_00_string_set_create() {
    string_set *set = string_set_create();
    unit_assert(set->capacity == ARRAY_DEFAULT_CAPACITY);
    unit_assert(set->size == 0);
    free(set->data);
    free(set);
    return EXIT_SUCCESS;
}

bool test_01_string_set_delete() {
    string_set *set = string_set_create();
    for (int i = 0;  i < set->size;  i++) {
        set->data[i] = malloc(8);
    }
    string_set_delete(set);
    return EXIT_SUCCESS;
}

bool test_02_string_set_contains() {
    string_set *set = string_set_create();
    // must be appended in alphabetical order for binary search to work
    char* sorted[10] = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"};

    for (int i = 0;  i < 10;  i++) {
        string_array_append(set, sorted[i]);
    }

    for (int i = 0;  i < 10;  i++) {
        unit_assert(string_set_contains(set, sorted[i]) == true);
    }

    unit_assert(string_set_contains(set, "aa") == false);
    unit_assert(string_set_contains(set, "jj") == false);

    string_set_delete(set);
    return EXIT_SUCCESS;
}

bool test_03_string_set_add() {
    string_set *set = string_set_create();
    char* sorted[10] = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"};
    char* unsorted[10] = {"c", "a", "h", "d", "e", "j", "g", "b", "f", "i"};

    for (int i = 0;  i < 10;  i++) {
        string_set_add(set, unsorted[i]);
    }

    for (int i = 0;  i < 10;  i++) {
        unit_assert(string_set_contains(set, sorted[i]) == true);
    }

    unit_assert(set->size == 10);
    for (int i = 0;  i < 10;  i++) {
        unit_assert(string_set_contains(set, sorted[i]) == true);
    }
    unit_assert(set->size == 10);

    string_set_delete(set);
    return EXIT_SUCCESS;
}

bool test_04_string_set_remove() {
    string_set *set = string_set_create();
    char* sorted[10] = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"};
    char* unsorted[10] = {"c", "a", "h", "d", "e", "j", "g", "b", "f", "i"};

    for (int i = 0;  i < 10;  i++) {
        string_set_add(set, unsorted[i]);
    }

    for (int i = 0;  i < 10;  i++) {
        // remove it
        string_set_remove(set, sorted[i]);
        unit_assert(string_set_contains(set, sorted[i]) == false);
        unit_assert(set->size == 9 - i);
        // try again
        string_set_remove(set, sorted[i]);
        unit_assert(set->size == 9 - i);
    }

    string_set_delete(set);
    return EXIT_SUCCESS;
}

bool test_05_string_set_from_array() {
    string_array *array = string_array_create();
    char* array_data[8] = {"c", "e", "a", "b", "a", "c", "d", "b"};
    char* set_data[5] = {"a", "b", "c", "d", "e"};

    for (int i = 0;  i < 8;  i++) {
        string_array_append(array, array_data[i]);
    }
    string_set *set = string_set_from_array(array);
    unit_assert(compare_array_of_strings(set->data, set_data, set->size));
    string_array_delete(array);
    return EXIT_SUCCESS;
}

/* Main Execution */

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s NUMBER\n\n", argv[0]);
        fprintf(stderr, "Where NUMBER is one of the following:\n");
        fprintf(stderr, "    0  Test string_set_create\n");
        fprintf(stderr, "    1  Test string_set_delete\n");
        fprintf(stderr, "    2  Test string_set_contains\n");
        fprintf(stderr, "    3  Test string_set_add\n");
        fprintf(stderr, "    4  Test string_set_remove\n");
        fprintf(stderr, "    5  Test string_set_from_array\n");
        return EXIT_FAILURE;
    }   

    int number = atoi(argv[1]);
    int status = EXIT_FAILURE;

    switch (number) {
        case 0:  status = test_00_string_set_create();     break;
        case 1:  status = test_01_string_set_delete();     break;
        case 3:  status = test_02_string_set_contains();   break;
        case 2:  status = test_03_string_set_add();        break;
        case 4:  status = test_04_string_set_remove();     break;
        case 5:  status = test_05_string_set_from_array(); break;
        default: fprintf(stderr, "Unknown NUMBER: %d\n", number); break;
    }
    
    if (status == EXIT_SUCCESS) {
        printf("Unit test passed\n");
    }
    return status;
}