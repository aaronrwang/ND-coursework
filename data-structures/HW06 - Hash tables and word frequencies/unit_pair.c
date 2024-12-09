#include "pair.h"

#include "unit_assert.h"
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/* Constants */

const Pair PAIRS[] = {
    {"wake me up inside", 0},
    {"123", 1},
    {"deadpool", 2},
    {"wolverine", 3},
    {"hell and back", 4},
    {NULL, 0},
};

/* Tests */

int test_00_pair_create() {
    /* Create pairs */
    for (const Pair *pa = PAIRS; pa->key; pa++) {
        Pair *p = pair_create(pa->key, pa->value);
        unit_assert(p);
        unit_assert(strcmp(pa->key, p->key) == 0);
        unit_assert(pa->value == p->value);

        free(p->key);
        free(p);
    }
    return EXIT_SUCCESS;
}

int test_01_pair_delete() {
    /* Create and delete pairs */
    for (const Pair *pa = PAIRS; pa->key; pa++) {
        Pair *p = pair_create(pa->key, pa->value);
        unit_assert(p);
        unit_assert(strcmp(pa->key, p->key) == 0);
        unit_assert(pa->value == p->value);

        pair_delete(p);
    }
    return EXIT_SUCCESS;
}

int test_02_pair_format() {
    /* Create temporary file */
    char path[BUFSIZ] = "/tmp/test_pair_XXXXXXX";
    int   fd = mkstemp(path);
    unit_assert(fd > 0);
    unlink(path);

    FILE *fs = fdopen(fd, "w+");
    unit_assert(fs);

    /* Dump pairs to file */
    for (const Pair *pa = PAIRS; pa->key; pa++) {
        pair_print((Pair *)pa, fs);
    }

    /* Rewind file */
    unit_assert(fseek(fs, 0, SEEK_SET) == 0);

    /* Read and compare output */
    char buffer[BUFSIZ];
    char format[BUFSIZ];
    for (const Pair *pa = PAIRS; pa->key; pa++) {
        sprintf(format, "%ld\t%s\n", pa->value, pa->key);
        unit_assert(fgets(buffer, BUFSIZ, fs));
        unit_assert(strcmp(buffer, format) == 0);
    }

    fclose(fs);
    return EXIT_SUCCESS;
}

/* Main Execution */

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s NUMBER\n\n", argv[0]);
        fprintf(stderr, "Where NUMBER is right of the following:\n");
        fprintf(stderr, "    0  Test pair_create\n");
        fprintf(stderr, "    1  Test pair_delete\n");
        fprintf(stderr, "    2  Test pair_format\n");
        return EXIT_FAILURE;
    }

    int number = atoi(argv[1]);
    int status = EXIT_FAILURE;

    switch (number) {
        case 0:  status = test_00_pair_create(); break;
        case 1:  status = test_01_pair_delete(); break;
        case 2:  status = test_02_pair_format(); break;
        default: fprintf(stderr, "Unknown NUMBER: %d\n", number); break;
    }

    if (status == EXIT_SUCCESS) {
        printf("Unit test passed\n");
    }
    return status;
}
