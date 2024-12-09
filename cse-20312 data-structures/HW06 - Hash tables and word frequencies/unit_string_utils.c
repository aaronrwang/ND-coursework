#include "string_utils.h"
#include "unit_assert.h"

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Constants */

typedef struct {
    char *old;
    char *new;
} Strings;

Strings STRINGS[] = {
    {"", ""},
    {"Vampire", "vampire"},
    {"VaMpIrE", "vampire"},

    {"vampire,", "vampire"},
    {"(vampire)", "vampire"},
    {"va'mpire?", "va'mpire"},

    {"(Vampire)", "vampire"},
    {"Vampire?", "vampire"},
};

/* Tests */

int test_00_str_lower() {
    char old[BUFSIZ];

    for (size_t i = 1; i <= 2; i++) {
        strcpy(old, STRINGS[i].old);
    	unit_assert(strcmp(str_lower(old), STRINGS[i].new) == 0);
    }

    strcpy(old, STRINGS[0].old);
    unit_assert(strcmp(str_lower(old), STRINGS[0].new) == 0);
    return EXIT_SUCCESS;
}

int test_01_str_trim() {
    char old[BUFSIZ];

    for (size_t i = 3; i <= 5; i++) {
        strcpy(old, STRINGS[i].old);
    	unit_assert(strcmp(str_trim(old), STRINGS[i].new) == 0);
    }

    strcpy(old, STRINGS[0].old);
    unit_assert(strcmp(str_trim(old), STRINGS[0].new) == 0);
    return EXIT_SUCCESS;
}

int test_02_str_both() {
    char old[BUFSIZ];

    for (size_t i = 0; i < 8; i++) {
        strcpy(old, STRINGS[i].old);
    	unit_assert(strcmp(str_trim(str_lower(old)), STRINGS[i].new) == 0);
    }

    return EXIT_SUCCESS;
}

/* Main Execution */

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s NUMBER\n\n", argv[0]);
        fprintf(stderr, "Where NUMBER is right of the following:\n");
        fprintf(stderr, "    0  Test str_lower\n");
        fprintf(stderr, "    1  Test str_trim\n");
        fprintf(stderr, "    2  Test str_both\n");
        return EXIT_FAILURE;
    }

    int number = atoi(argv[1]);
    int status = EXIT_FAILURE;

    switch (number) {
        case 0:  status = test_00_str_lower(); break;
        case 1:  status = test_01_str_trim(); break;
        case 2:  status = test_02_str_both(); break;
        default: fprintf(stderr, "Unknown NUMBER: %d\n", number); break;
    }

    if (status == EXIT_SUCCESS) {
        printf("Unit test passed\n");
    }
    return status;
}
