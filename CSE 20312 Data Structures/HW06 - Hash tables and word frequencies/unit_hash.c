/* unit_hash.c: Hash Functions Unit Test */

#include "hash.h"
#include "unit_assert.h"

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Constants */

static struct {
    char *	key;
    long	fnv_hash;
} DATA_HASHES[] = {
    {"wake me up inside", 0x7d9454fa584a0a56L},
    {"123"              , 0x456fc2181822c4dbL},
    {"deadool"          , 0x7d517630945dadbbL},
    {"wolverine"        , 0x874d0d8868f684c8L},
    {"hell and back"    , 0x204ad978881e7a46L},
    {NULL               , 0},
};

/* Tests */

int test_00_fnv_hash() {
    for (int i = 0; DATA_HASHES[i].key; i++) {
    	long hash = fnv_hash(DATA_HASHES[i].key);
    	printf("%20s = 0x%lx\n", DATA_HASHES[i].key, hash);
    	unit_assert(DATA_HASHES[i].fnv_hash == hash);
    }
    return EXIT_SUCCESS;
}

/* Main Execution */

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s NUMBER\n\n", argv[0]);
        fprintf(stderr, "Where NUMBER is right of the following:\n");
        // fprintf(stderr, "    0  Test fnv_hash\n");
        fprintf(stderr, "    0  Test fnv_hash\n");
        return EXIT_FAILURE;
    }

    int number = atoi(argv[1]);
    int status = EXIT_FAILURE;

    switch (number) {
        // case 0:  status = test_00_djb_hash(); break;
        case 0:  status = test_00_fnv_hash(); break;
        default: fprintf(stderr, "Unknown NUMBER: %d\n", number); break;
    }

    if (status == EXIT_SUCCESS) {
        printf("Unit test passed\n");
    }
    return status;
}
