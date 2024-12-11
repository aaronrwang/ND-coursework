#!/usr/bin/env python3

''' center_star.py - Center Star '''

import sys
from graph import AdjacencyMatrix, read_adjacency_matrix

# Functions

def find_center(graph: AdjacencyMatrix) -> int:
    for i, row in enumerate(graph):
        flag = True
        for j, n in enumerate(row):
            if n == 0 and j!=i:
                flag = False
                break
        if flag:
            return i
    return -1

# Main Execution

def main(stream=sys.stdin) -> None:
    res = find_center(read_adjacency_matrix(stream))
    if res == -1:
        print('There is no center')
    else:
        print(f'Vertex {res} is the center')

    pass

if __name__ == '__main__':
    main()