#include "string_set.h"
#include "utilities.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define TEXT_BUFSIZE 2<<14

string_set *read_common_words(char *fname) {
    FILE *infile = fopen(fname, "r");
    if (infile == NULL) {
        printf("Error opening %s\n", fname);
        exit(EXIT_FAILURE);
    }

    char buf[80];

    string_set *common_words = string_set_create();

    while (fscanf(infile, "%s", buf) == 1) {
        string_array_append(common_words, buf);
    }
    string_array_sort(common_words);

    fclose(infile);
    return common_words;
}

string_set *read_text(char *fname) {
    FILE *infile = fopen(fname, "r");
    if (infile == NULL) {
        printf("Error opening %s\n", fname);
        exit(EXIT_FAILURE);
    }

    char line[TEXT_BUFSIZE];

    // Use all punctuation and special symbols as delimiters
    const char delim[] = " ,.!?;:-/$#&*~@^_+=<>()[]{}\r\n\t\"\'";
    char *token;

    string_array *words = string_set_create();

    // read all words that don't contain numbers
    while (fgets(line, TEXT_BUFSIZE, infile)) {
        token = strtok(line, delim);
        while (token) {
            if (string_isalpha(token)) {
                string_array_append(words, string_tolower(token));
            }
            token = strtok(NULL, delim);
        }
    }

    // remove duplicates by converting to set
    string_set *unique_words = string_set_from_array(words);

    fclose(infile);
    return unique_words;
}

int main(int argc, char **argv) {
    if (argc != 3) {
        puts("Usage spellcheck <wordlist_file> <text_file>\n");
    }

    string_set *common_words = read_common_words(argv[1]);    
    string_set *text         = read_text(argv[2]);

    for (int i = 0;  i < text->size;  i++) {
        char *word = string_array_at(text, i);
        if (!string_set_contains(common_words, word)) {
            puts(word);
        }
    }

    string_set_delete(common_words);
    string_set_delete(text);
}