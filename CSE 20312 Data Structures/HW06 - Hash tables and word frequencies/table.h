#pragma once

#include "hash.h"
#include "pair.h"

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define DEFAULT_CAPACITY    (1<<3)
#define DEFAULT_ALPHA       0.5

typedef struct {
    Pair          **buckets;
    size_t          capacity;
    size_t          size;
    double          alpha;
    // HashFunction    hash;
} Table;

// Table*  table_create(int capacity, double alpha, HashFunction hash);
Table*  table_create(int capacity, double alpha);
void    table_delete(Table *t);
int     table_locate(Table *t, const char *key);
void    table_insert_or_update(Table *t, const char *key, long value);
long    table_lookup(Table *t, const char *key);
void    table_print(Table *t, FILE *stream);
void    table_resize(Table *t, int capacity);
