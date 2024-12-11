#!/usr/bin/env python3

''' graph.py - Graph Utilities

Each graph is in the following format:

    4   # Number of vertices
    3   # Number of edges
    1 2 # Edge 1
    2 3 # Edge 2
    4 2 # Edge 3
'''

import sys
from collections import defaultdict

# Types

AdjacencyMatrix = list[list[int]]
AdjacencyList   = dict[int, list[int]]

# Functions

def read_adjacency_matrix(stream=sys.stdin) -> AdjacencyMatrix:
    input_string = stream.read()
    inputs = input_string.split('\n')
    num_vertices = int(inputs[0])
    num_edges = int(inputs[1])

    matrix = []
    for i in range(num_vertices):
        matrix.append([0]*num_vertices)

    for i in range(2,len(inputs)):
        temp = inputs[i]
        vertices = temp.split(' ')
        try:
            a = int(vertices[0])
            b = int(vertices[1])
            matrix[a][b] = 1
            matrix[b][a] = 1
        except:
            continue
    return matrix

def read_adjacency_list(stream=sys.stdin) -> AdjacencyList:
    input_string = stream.read()
    inputs = input_string.split('\n')
    num_vertices = int(inputs[0])
    num_edges = int(inputs[1])

    res = {}
    for i in range(2,len(inputs)):
        temp = inputs[i]
        vertices = temp.split(' ')
        try:
            a = int(vertices[0])
            b = int(vertices[1])
            if a in res:
                (res[a]).append(b)
            else:
                res[a]=[b]
            if b in res:
                (res[b]).append(a)
            else:
                res[b]=[a]
        except:
            continue
    return res

