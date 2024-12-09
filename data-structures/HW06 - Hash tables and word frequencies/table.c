#include "table.h"
#include <string.h>
#include <stdio.h>

/**
 * Allocate and initialize new Table structure.
 *
 * @param   capacity        Number of buckets in the hash table.
 * @param   alpha           Maximum load factor for hash table.
 * @param   hash            Hash function to use for hash table.
 * @return  New Table structure (must be deleted later).
 **/

Table *table_create(int capacity, double alpha) {
    // TODO:
    Table* t = calloc(1, sizeof(Table));

    // set table capacity; set default if 0
    t->capacity = capacity;
    if (t->capacity == 0){
        t->capacity=DEFAULT_CAPACITY;
    }

    //create as many buckets as capacity
    t->buckets = calloc(t->capacity, sizeof(Pair *));

    //set size and load factor
    t->size = 0;
    t->alpha = alpha;

    return t;
}

/**
 * Release internal pairs and buckets and then the Table structure itself.
 *
 * @param   t               Pointer to the Table structure.
 **/
void table_delete(Table *t) {
    for (int i = 0; i < t->capacity; i++){
        if (t->buckets[i]){
            pair_delete(t->buckets[i]);
        }
    }
    free(t->buckets);
    free(t);
}

/**
 * Locate bucket index for given key using linear probing.
 *
 *  1. If key is already in table, it returns the index of Pair with the
 *  corresponding key.
 *
 *  2. If key is not in table, it returns the index where a new Pair should be
 *  inserted.
 *
 *  3. If key is not in table and it is not possible to insert a new Pair, it
 *  returns -1.
 *
 * @param   t       Pointer to the Table structure.
 * @param   key     Key string to locate.
 * @return          Index where Pair with key can be found or inserted (-1 if not possible).
 **/
int table_locate(Table *t, const char *key) {
    int bucket = fnv_hash(key) % t->capacity;
    int i = bucket;
    do{
        if(!(t->buckets[i])){
            return i;
        } 
        if(!strcmp(t->buckets[i]->key,key)){
            return i;
        }
        i++;
        i %= t->capacity;
    } while (i!=bucket);
    return -1;
}

/**
 * Add key/value Pair to Table structure if the key is not already present.
 * Otherwise, update the value associated with the key.
 *
 * @param   t               Pointer to the Table structure.
 * @param   key             String key of Pair.
 * @param   value           Integer value of Pair.
 **/
void table_insert_or_update(Table *t, const char *key, long value) {
    
    
    // Resize table if necessary by doubling the capacity
    // TODO:
    if (t->size == t->alpha * t->capacity){
        table_resize(t, (t->capacity)*2); // should resize
    }
    // Locate bucket
    // TODO:
    int index = table_locate(t, key);

    // Perform insert or update
    // TODO:
    if (t->buckets[index]){
        t->buckets[index]->value = value;
    } else {
        t->buckets[index] = pair_create(key, value);
    }
    
    t->size++;
}

/**
 * Lookup key in Table structure.
 *
 * @param   t               Pointer to the Table structure.
 * @param   key             String Key of Pair.
 * @return  Value associated with key if it is in table, otherwise -1.
 **/
long table_lookup(Table *t, const char *key) {
    // Locate bucket and return corresponding value
    // TODO:
    int index = table_locate(t, key);
    if (t->buckets[index]){
        return t->buckets[index]->value;
    }
    return -1;
}

/**
 * Print all the pairs in the Table structure.
 *
 * @param   t               Pointer to the Table structure.
 * @param   stream          File stream to write to.
 **/
void table_print(Table *t, FILE *stream) {
    for (int bucket = 0; bucket < t->capacity; bucket++) {
        if (t->buckets[bucket])
            pair_print(t->buckets[bucket], stream);
    }
}

/**
 * Resize the current Table structure with the new capacity.
 *
 * @param   t               Pointer to the Table structure.
 * @param   capacity        New capacity of Table structure.
 **/
void table_resize(Table *t, int capacity) {
    Table *new = table_create(capacity, t->alpha);
    // put all in new
    for (int i = 0; i < t->capacity; i++){
        if (t->buckets[i]){
            table_insert_or_update(new,t->buckets[i]->key,t->buckets[i]->value);
        }
    }
    //change capacity and buckets of new and old
    Pair** temp = t->buckets;
    size_t tCap = t->capacity;
    t->buckets = new->buckets;
    t->capacity = new->capacity;
    new->capacity = tCap;
    new->buckets = temp;

    //delete old buckets and table info.
    table_delete(new);
}
