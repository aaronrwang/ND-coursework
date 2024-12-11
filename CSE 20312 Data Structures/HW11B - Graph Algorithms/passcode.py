#!/usr/bin/env python3

import sys

from collections import defaultdict, deque

# Types

Graph   = dict[int, set[int]]
Degrees = dict[int, int]

# Functions

def read_graph(stream) -> Graph:
    graph: Graph = defaultdict(set)
    for line in stream:
        a = int(line[0])
        b = int(line[1])
        c = int(line[2])
        graph[a].add(b)
        graph[b].add(c)
    return graph

def compute_degrees(graph: Graph) -> Degrees:
    degrees:Degrees = {}
    for key in graph:
        degrees[key] = 0
    for key in graph:
        for value in graph[key]:
            if value not in degrees:
                degrees[value] = 0
            degrees[value]+=1
    return degrees


def find_passcode(graph: Graph) -> list[int]:
    in_degree = compute_degrees(graph)

    # Find all nodes with no incoming edges
    deq = deque([node for node in graph if in_degree[node] == 0])
    res = []
    while len(deq) > 0:
        node = deq.popleft()
        res.append(node)
        if node not in graph:
            continue
        for value in list(graph[node]):
            in_degree[value]-=1
            if in_degree[value] == 0:
                deq.append(value)
    return res
            
    

# Main Execution

def main(args=None) -> None:
    if args is None:
        args = sys.argv[1:]

    with open(args[0], 'r') as stream:
        graph = read_graph(stream)
        
    passcode = find_passcode(graph)
    print(''.join(map(str, passcode)))

if __name__ == '__main__':
    main()