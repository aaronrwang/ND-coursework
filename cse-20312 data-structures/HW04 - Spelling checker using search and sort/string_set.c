#include "string_set.h"
#include "string_array.h"
#include "utilities.h"
#include <string.h>
#include <stdbool.h>

string_set* string_set_create() {
    return string_array_create();
}

void string_set_delete(string_set *set) {
    string_array_delete(set);
}

void string_set_add(string_set *set, char *str) {
    // TODO:
    // Use binary_search_insert_index to find where to insert str
    // into the data array in alphabetical order.  If the string is
    // already in the set, return -1.  Otherwise, insert it at the
    // proper index or append it if it should go at the end.
    // Use existing string_array methods where possible

    int index = binary_search_insert_index(set->data, set->size, str);
    if (index == -1) return;
    string_array_insert(set, index, str);
}

bool string_set_contains(string_set *set, char *str) {
    // TODO:
    // Use binary_search to determine if str is in the set
    // Return false if it is not in the set and true if it is.
    return (binary_search(set->data, set->size,  str)!=-1);
}

void string_set_remove(string_set *set, char *str) {
    // TODO:
    // Use binary_search to determine if str is in the set
    // If it is, remove it.
    // Use existing string_array methods where possible
    int index = binary_search(set->data, set->size,  str);
    if (index==-1) return; 
    string_array_remove(set, index);
}

string_set *string_set_from_array(string_array *array) {
    // TODO:
    // Create a string_set from a string_array by sorting it into
    // alphabetical order and removing any duplicates.  Note that
    // when the array is in alphabetical order, it is easy to identify
    // duplicates since they will be adjacent to each other.
    // Use existing string_array methods wherever possible.
    
    string_array_sort(array);
    for(int i = (array->size)-2; i >=0; i--){
        if(!strcmp(string_array_at(array, i + 1), string_array_at(array, i))){
            string_array_remove(array, i+1);
        }
    }

    return (string_set*) array;
}
