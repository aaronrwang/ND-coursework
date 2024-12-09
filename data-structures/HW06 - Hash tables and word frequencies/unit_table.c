#include "table.h"
#include "unit_assert.h"

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/* Constants */

const Pair PAIRS[] = {
    {"wake me up inside", 6},
    {"123", 3},
    {"134", 4},
    {"deadpool", 5},
    {"wolverine", 0},
    {"barbaric", 7},
    {"hell and back", 1},
    {NULL, 0},
};

/* Tests */

int test_00_table_create() {
    /* Create Table with default capacity */
    Table *t = table_create(0, 0.5);
    unit_assert(t != NULL);
    unit_assert(t->capacity == DEFAULT_CAPACITY);
    unit_assert(t->size     == 0);
    unit_assert(t->alpha    == 0.5);
    free(t->buckets);
    free(t);

    /* Create Table with custom capacity */
    t = table_create(10, 0.75);
    unit_assert(t->capacity == 10);
    unit_assert(t->size     == 0);
    unit_assert(t->alpha    == 0.75);
    free(t->buckets);
    free(t);

    return EXIT_SUCCESS;
}

int test_01_table_delete() {
    /* Create Table with default capacity */
    Table *t = table_create(0, 0.5);
    unit_assert(t != NULL);
    unit_assert(t->capacity == DEFAULT_CAPACITY);
    unit_assert(t->size     == 0);
    unit_assert(t->alpha    == 0.5);

    size_t bucket = 0;
    for (const Pair *pa = PAIRS; pa->key; pa++)
        t->buckets[bucket++] = pair_create(pa->key, pa->value);

    table_delete(t);

    /* Create Table with custom capacity */
    t = table_create(10, 0.75);
    unit_assert(t->capacity == 10);
    unit_assert(t->size     == 0);
    unit_assert(t->alpha    == 0.75);

    bucket = 0;
    for (const Pair *pa = PAIRS; pa->key; pa++)
        t->buckets[bucket++] = pair_create(pa->key, pa->value);

    table_delete(t);
    return EXIT_SUCCESS;
}

int test_02_table_locate() {
    Table *t = table_create(0, 0.5);
    unit_assert(t != NULL);
    unit_assert(t->capacity == DEFAULT_CAPACITY);
    unit_assert(t->size     == 0);
    unit_assert(t->alpha    == 0.5);

    for (const Pair *pa = PAIRS; pa->key; pa++)
        t->buckets[pa->value] = pair_create(pa->key, pa->value);

    for (const Pair *pa = PAIRS; pa->key; pa++)
        unit_assert(table_locate(t, pa->key) == pa->value);

    unit_assert(table_locate(t, "globes and maps") == 2);
    table_delete(t);
    return EXIT_SUCCESS;
}

int test_03_table_insert() {
    Table *t = table_create(0, 1.0);
    unit_assert(t != NULL);
    unit_assert(t->capacity == DEFAULT_CAPACITY);
    unit_assert(t->size     == 0);
    unit_assert(t->alpha    == 1.0);

    for (const Pair *pa = PAIRS; pa->key; pa++)
        table_insert_or_update(t, pa->key, pa->value);

    for (const Pair *pa = PAIRS; pa->key; pa++)
        unit_assert(table_locate(t, pa->key) == pa->value);

    unit_assert(t->capacity == DEFAULT_CAPACITY);
    unit_assert(t->size     == (sizeof(PAIRS) / sizeof(Pair)) - 1);

    table_delete(t);
    return EXIT_SUCCESS;
}

int test_04_table_lookup() {
    Table *t = table_create(0, 1.0);
    unit_assert(t != NULL);
    unit_assert(t->capacity == DEFAULT_CAPACITY);
    unit_assert(t->size     == 0);
    unit_assert(t->alpha    == 1.0);

    for (const Pair *pa = PAIRS; pa->key; pa++)
        table_insert_or_update(t, pa->key, pa->value);

    for (const Pair *pa = PAIRS; pa->key; pa++)
        unit_assert(table_lookup(t, pa->key) == pa->value);
    unit_assert(table_lookup(t, "globes and maps") == -1);
    unit_assert(t->capacity == DEFAULT_CAPACITY);
    unit_assert(t->size     == (sizeof(PAIRS) / sizeof(Pair)) - 1);

    table_delete(t);
    return EXIT_SUCCESS;
}

int test_05_table_resize() {
    Table *t = table_create(0, 1.0);
    unit_assert(t != NULL);
    unit_assert(t->capacity == DEFAULT_CAPACITY);
    unit_assert(t->size     == 0);
    unit_assert(t->alpha    == 1.0);

    for (const Pair *pa = PAIRS; pa->key; pa++)
        table_insert_or_update(t, pa->key, pa->value);

    for (const Pair *pa = PAIRS; pa->key; pa++)
        unit_assert(table_lookup(t, pa->key) == pa->value);
    unit_assert(table_lookup(t, "globes and maps") == -1);
    table_resize(t, (t->capacity) * 2);
    unit_assert(t->capacity == DEFAULT_CAPACITY * 2);
    unit_assert(t->size     == (sizeof(PAIRS) / sizeof(Pair)) - 1);

    for (const Pair *pa = PAIRS; pa->key; pa++)
        unit_assert(table_lookup(t, pa->key) == pa->value);

    unit_assert(table_locate(t, "wake me up inside") == 7);
    unit_assert(table_locate(t, "123") == 11);
    unit_assert(table_locate(t, "134") == 12);
    unit_assert(table_locate(t, "deadpool") == 13);
    unit_assert(table_locate(t, "wolverine") == 8);
    unit_assert(table_locate(t, "barbaric") == 15);
    unit_assert(table_locate(t, "hell and back") == 6);
    unit_assert(table_locate(t, "globes and maps") == 9);
    unit_assert(table_locate(t, "mountain of regret") == 14);

    table_delete(t);
    return EXIT_SUCCESS;
}

int test_06_table_insert_resize() {
    Table *t = table_create(0, 0.5);
    unit_assert(t != NULL);
    unit_assert(t->capacity == DEFAULT_CAPACITY);
    unit_assert(t->size     == 0);
    unit_assert(t->alpha    == 0.5);

    for (const Pair *pa = PAIRS; pa->key; pa++)
        table_insert_or_update(t, pa->key, pa->value);

    for (const Pair *pa = PAIRS; pa->key; pa++)
        unit_assert(table_lookup(t, pa->key) == pa->value);

    unit_assert(table_lookup(t, "globes and maps") == -1);
    
    unit_assert(t->capacity == DEFAULT_CAPACITY * 2);
    unit_assert(t->size     == (sizeof(PAIRS) / sizeof(Pair)) - 1);

    table_delete(t);
    return EXIT_SUCCESS;
}

/* Main Execution */

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s NUMBER\n\n", argv[0]);
        fprintf(stderr, "Where NUMBER is right of the following:\n");
        fprintf(stderr, "    0  Test table_create\n");
        fprintf(stderr, "    1  Test table_delete\n");
        fprintf(stderr, "    2  Test table_locate\n");
        fprintf(stderr, "    3  Test table_insert\n");
        fprintf(stderr, "    4  Test table_lookup\n");
        fprintf(stderr, "    5  Test table_resize\n");
        fprintf(stderr, "    6  Test table_insert_resize\n");
        return EXIT_FAILURE;
    }

    int number = atoi(argv[1]);
    int status = EXIT_FAILURE;

    switch (number) {
        case 0:  status = test_00_table_create(); break;
        case 1:  status = test_01_table_delete(); break;
        case 2:  status = test_02_table_locate(); break;
        case 3:  status = test_03_table_insert(); break;
        case 4:  status = test_04_table_lookup(); break;
        case 5:  status = test_05_table_resize(); break;
        case 6:  status = test_06_table_insert_resize(); break;
        default: fprintf(stderr, "Unknown NUMBER: %d\n", number); break;
    }

    if (status == EXIT_SUCCESS) {
        printf("Unit test passed\n");
    }
    return status;
}
