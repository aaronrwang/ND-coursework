#!/usr/bin/env python3

''' reddit_groups.py - Reddit Groups '''

import sys

from typing import Iterator
from graph  import AdjacencyList, read_adjacency_list

# Functions

def walk_graph(graph: AdjacencyList, origin: int) -> set[int]:
    visited = set([])
    queue = [origin]
    while queue:
        new_queue = []
        for vertice in queue:
            neighbors = graph[vertice]
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_queue.append(neighbor)
        queue = new_queue
    return visited

def find_groups(graph: AdjacencyList) -> Iterator[list[int]]:
    visited = set([])
    nodes = list(graph.keys())
    for node in nodes:
        if node in visited:
            continue
        new_visited=walk_graph(graph, node)
        for n in new_visited:
            visited.add(n)
        yield list(new_visited)

    pass

# Main Execution

def main(stream=sys.stdin) -> None:
    graph = read_adjacency_list(stream)
    gen = find_groups(graph)
    for value in gen:
        value.sort()
        for i,n in enumerate(value):
            if i != len(value)-1:
                print(n, end=" ")
            else:
                print(n)

if __name__ == '__main__':
    main()