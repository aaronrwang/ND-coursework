#include "string_functions.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>

int test_00_my_strlen() {
    assert(my_strlen("") == 0);
    assert(my_strlen("a") == 1);
    assert(my_strlen("Hello, world!") == 13);
    return EXIT_SUCCESS;
}

int test_01_my_strcmp() {
    assert(my_strcmp("apple", "apple") == 0);
    assert(my_strcmp("apply", "apple") > 0);
    assert(my_strcmp("apple", "apply") < 0);
    assert(my_strcmp("applesauce", "apple") > 0);
    assert(my_strcmp("apple", "applesauce") < 0);
    return EXIT_SUCCESS;
}

int test_02_my_strdup() {
    char *original = "leprechaun";
    char *duplicate = my_strdup(original);
    assert(my_strcmp(original, duplicate) == 0);
    assert(original != duplicate);
    free(duplicate);
    return EXIT_SUCCESS;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s NUMBER\n\n", argv[0]);
        fprintf(stderr, "Where NUMBER is one of the following:\n");
        fprintf(stderr, "    0  Test my_strlen\n");
        fprintf(stderr, "    1  Test my_strcmp\n");
        fprintf(stderr, "    2  Test my_strdup\n");
        return EXIT_FAILURE;
    }

    int number = atoi(argv[1]);
    int status = EXIT_FAILURE;

    switch (number) {
        case 0: status = test_00_my_strlen(); break;
        case 1: status = test_01_my_strcmp(); break;
        case 2: status = test_02_my_strdup(); break;
        default: fprintf(stderr, "Unknown NUMBER: %d\n", number); break;
    }

    if (status == EXIT_SUCCESS)
        printf("Unit test passed\n");
    return status;
}