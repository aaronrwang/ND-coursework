#include "string_functions.h"
#include <stdlib.h>

size_t my_strlen(const char *str) {
    int count = 0;
    while(*(str+count) != 0){
        count++;
    }
    return count;
}

int my_strcmp(const char *str1, const char *str2) {
    int l1 = my_strlen(str1);
    int l2 = my_strlen(str2);
    if (l1 > l2) return 1;
    if (l1 < l2) return -1;
    int a = 0, b = 0;
    for (int i = 0; i < l1; i++){
        a+=*(str1+i);
        b+=*(str2+i);
    }
    if (a > b) return 1;
    if (a < b) return -1;
    return 0;
}

char *my_strdup(const char *s) {
    int l = my_strlen(s);
    char* str = (char*)malloc((l+1)*sizeof(char));
    for (int i = 0; i <= l; i++){
        *(str+i)=*(s+i);
    }
    return str;
}
