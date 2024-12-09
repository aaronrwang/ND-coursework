#include "set.h"

Set* set_create() {
    return array_create();
}

void set_delete(Set *set) {
    array_delete(set);
}

bool set_contains(Set *set, int value) {
    // TODO:
    for (int i = 0; i < set->size; i++){
        if(array_at(set, i)==value){
            return true;
        }
    }
    return false;
}

void set_add(Set *set, int value) {
    // TODO:
    if(!set_contains(set, value)){
        array_append(set, value);
    }
}

void set_remove(Set *set, int value) {
    // TODO:
    for (int i = 0; i < set->size; i++){
        if(array_at(set, i)==value){
            array_remove(set, i);
            break;
        }
    }
}