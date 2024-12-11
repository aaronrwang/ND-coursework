#include "utilities.h"
#include "unit_assert.h"

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool test_00_binary_search(){
    char* sa[5] = {"a", "b", "c", "d", "e"};
    unit_assert(binary_search(sa, 5, "a") == 0);
    unit_assert(binary_search(sa, 5, "b") == 1);
    unit_assert(binary_search(sa, 5, "c") == 2);
    unit_assert(binary_search(sa, 5, "d") == 3);
    unit_assert(binary_search(sa, 5, "e") == 4);
    unit_assert(binary_search(sa, 5, "f") == -1);
    return EXIT_SUCCESS;
}

bool test_01_binary_search_insert_index(){
    char* sa[] = {"b", "d", "f", "h", "k"};
    unit_assert(binary_search_insert_index(sa, 5, "a") == 0);
    unit_assert(binary_search_insert_index(sa, 5, "e") == 2);
    unit_assert(binary_search_insert_index(sa, 5, "m") == 5);
    unit_assert(binary_search_insert_index(sa, 5, "b") == -1);
    unit_assert(binary_search_insert_index(sa, 5, "f") == -1);
    unit_assert(binary_search_insert_index(sa, 5, "k") == -1);
    return EXIT_SUCCESS;
}

bool test_02_partition(){
    char* sa1[5] = {"a", "b", "c", "d", "e"};
    char* pa1[5] = {"a", "b", "c", "d", "e"};
    unit_assert(partition(sa1, 0, 4) == 2);
    unit_assert(compare_array_of_strings(sa1, pa1, 5));

    char* sa2[5] = {"b", "c", "a", "d", "e"};
    char* pa2[5] = {"a", "c", "b", "d", "e"};
    unit_assert(partition(sa2, 0, 4) == 0);
    unit_assert(compare_array_of_strings(sa2, pa2, 5));

    char* sa3[5] = {"a", "b", "e", "c", "d"};
    char* pa3[5] = {"a", "b", "d", "c", "e"};
    unit_assert(partition(sa3, 0, 4) == 3);
    unit_assert(compare_array_of_strings(sa3, pa3, 5));

    char* sa4[5] = {"a", "b", "d", "c", "e"};
    char* pa4[5] = {"a", "b", "c", "d", "e"};
    unit_assert(partition(sa4, 0, 4) == 2);
    unit_assert(compare_array_of_strings(sa4, pa4, 5));

    char* sa5[5] = {"d", "e", "c", "a", "b"};
    char* pa5[5] = {"b", "a", "c", "e", "d"};
    unit_assert(partition(sa5, 0, 4) == 2);
    unit_assert(compare_array_of_strings(sa5, pa5, 5));

    return EXIT_SUCCESS;
}

bool test_03_quicksort(){
    char *sorted[10] = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"};

    char *s1[10] = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"};
    quicksort(s1, 0, 9);
    unit_assert(compare_array_of_strings(s1, sorted, 10));

    char* s2[10] = {"e", "g", "j", "b", "f", "c", "h", "a", "d", "i"};
    quicksort(s2, 0, 9);
    unit_assert(compare_array_of_strings(s2, sorted, 10));

    char* s3[10] = {"j", "i", "h", "g", "f", "e", "d", "c", "b", "a"};
    quicksort(s3, 0, 9);
    unit_assert(compare_array_of_strings(s3, sorted, 10));

    return EXIT_SUCCESS;
}

/* Main Execution */

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s NUMBER\n\n", argv[0]);
        fprintf(stderr, "Where NUMBER is right of the following:\n");
        fprintf(stderr, "    0  Test binary_search\n");
        fprintf(stderr, "    1  Test binary_search_insert_index\n");
        fprintf(stderr, "    2  Test partition\n");
        fprintf(stderr, "    3  Test quicksort\n");
        return EXIT_FAILURE;
    }   

    int number = atoi(argv[1]);
    int status = EXIT_FAILURE;

    switch (number) {
        case 0:  status = test_00_binary_search(); break;
        case 1:  status = test_01_binary_search_insert_index(); break;
        case 2:  status = test_02_partition(); break;
        case 3:  status = test_03_quicksort(); break;
        default: fprintf(stderr, "Unknown NUMBER: %d\n", number); break;
    }
    
    if (status == EXIT_SUCCESS) {
        printf("Unit test passed\n");
    }
    return status;
}