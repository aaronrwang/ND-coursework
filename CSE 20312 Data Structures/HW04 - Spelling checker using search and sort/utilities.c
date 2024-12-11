#include "utilities.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

int binary_search(char **strings, int size, char *key) {
   // TODO: 
   // Return the index where key is found or -1 if it is not found
   int mid;
   int low = 0;
   int high = size - 1;
   while (low <= high){
      mid = (low+high)/2;
      if (!strcmp(strings[mid],key)){
         return mid;
      } else if (strcmp(strings[mid],key) < 0){
         low = mid+1;
      } else {
         high = mid-1;
      }
   }
   return -1; // not found
}

int binary_search_insert_index(char **strings, int size, char *key) {
   // TODO:
   // Return the index where key should be inserted, which
   // is typically the lower bound of the search interval.  If key
   // is found to be in the array, return -1
   int mid;
   int low = 0;
   int high = size - 1;
   while (low <= high){
      mid = (low+high)/2;
      if (!strcmp(strings[mid],key)){
         return -1;
      } else if (strcmp(strings[mid],key) < 0){
         low = mid+1;
      } else {
         high = mid-1;
      }
   }
   
   return low;
}

int partition(char **strings, int low_index, int high_index) {
   // Pick middle element as pivot
   int midpoint = (low_index + high_index) / 2;
   char *pivot = strings[midpoint];
   bool done = false;
   while (!done) {
      // TODO:
      // Increment low_index while strings[low_index] < pivot
      while (strcmp(strings[low_index],pivot)<0){
         low_index++;
      }
      // TODO:
      // Decrement high_index while pivot < strings[high_index] 
      while (strcmp(strings[high_index],pivot)>0){
         high_index--;
      }  
      // TODO:
      // If zero or one elements remain, then all strings are 
      // partitioned. Return high_index.
      if (high_index<=low_index ){
         return high_index;
      } else {
      // Else swap strings[low_index] and strings[high_index]
      // and update low_index and high_index
         char* temp = strings[low_index];
         strings[low_index]=strings[high_index];
         strings[high_index]=temp;
         low_index++;
         high_index--;
      }      
   }
   
   return high_index;
}

void quicksort(char **strings, int low_index, int high_index) {
   // TODO:
   // Base case: If the partition size is 1 or zero 
   // elements, then the partition is already sorted
   if (high_index <= low_index) return;
   
   // TODO:
   // Partition the data within the array. Value low_end_index 
   // returned from partitioning is the index of the low 
   // partition's last element.
   int lowEndIndex = partition(strings, low_index, high_index);
   
   // TODO:
   // Recursively sort low partition (low_index to low_end_index) 
   quicksort(strings, low_index, lowEndIndex);
   // and high partition (low_end_index + 1 to high_index)
   quicksort(strings, lowEndIndex+1, high_index);
   
}

bool string_isalpha(char *str) {
    char *ch = str;
    while (*ch) {
        if (!isalpha(*ch)) {
            return false;
        }
        ch++;
    }
    return true;
}

char *string_tolower(char *str) {
    char *ch = str;
    while (*ch) {
        *ch = tolower(*ch);
        ch++;
    }
    return str;
}

bool compare_array_of_strings(char **s1, char **s2, int n) {
   for (int i = 0;  i < n;  i++) {
      if (strcmp(s1[i], s2[i])) {
         return false;
      }
   }
   return true;
}
