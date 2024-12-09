#!/usr/bin/env python3

from avl_map import AVLMap
from list_map import ListMap
import sys
import re

def count_words(filename, word_count_map):
    with open(filename) as f:
        for line in f:
            # Split the string at any whitespace or punctuation
            words = re.split(r'[\W_]+', line)
            # Filter out any empty strings and non-alphabetic strings and convert to lowercase
            words = [word.lower() for word in words if word.isalpha()]
            # Count the words
            for word in words:
                if word in word_count_map:
                    word_count_map[word] += 1
                else:
                    word_count_map[word] = 1

def main():
    if len(sys.argv) != 3:
        script = sys.argv[0]
        sys.stderr.write(f'Usage: {script} [dict|list|bst|avl] filename\n')
        sys.exit(1)
    map_type = sys.argv[1]
    filename = sys.argv[2]

    if map_type == 'avl':
        word_count_map = AVLMap(do_balance=True)
    elif map_type == 'bst':
        word_count_map = AVLMap(do_balance=False)
    elif map_type == 'list':
        word_count_map = ListMap()
    elif map_type == 'dict':
        word_count_map = {}
    else:
        sys.stderr.write(f'Invalid map type: {map_type}\n')
        sys.exit(1)

    count_words(filename, word_count_map)

    for word, count in word_count_map.items():
        print(f'{count} {word}')

if __name__ == '__main__':
    main()