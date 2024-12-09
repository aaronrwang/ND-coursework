/* pair.h: Key/Value Pair Structure */

#pragma once

#include <stdint.h>
#include <stdio.h>

/* Structures */

typedef struct {
    char   *key;
    long value;
} Pair;

/* Functions */

Pair *      pair_create(const char *key, long value);
void        pair_delete(Pair *p);
void        pair_print(Pair *p, FILE *stream);

