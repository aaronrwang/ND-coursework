#pragma once

#include "string_array.h"
#include <stdbool.h>

/* Structures */

typedef string_array string_set;

/* Functions */

string_set* string_set_create();
void        string_set_delete(string_set *set);
void        string_set_add(string_set *set, char *str);
bool        string_set_contains(string_set *set, char *str);
void        string_set_remove(string_set *set, char *str);
string_set *string_set_from_array(string_array *array);