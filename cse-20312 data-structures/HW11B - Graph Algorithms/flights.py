#!/usr/bin/env python3

import sys

from collections import defaultdict
from heapq       import heappop, heappush
from typing      import Iterator

# Types

Graph = dict[int, dict[int, int]]
Plan  = dict[int, int]

# Functions

def read_graph(stream) -> Graph:
    graph = defaultdict(dict)
    for line in stream:
        source, target, weight = line.split()
        graph[int(source)][int(target)] = int(weight)
    return graph

def find_cheapest_flight_plan(origin: int, destination: int, graph: Graph) -> tuple[int, Plan]:
    # TODO:
    # frontier is a priority queue of tuples (distance, vertex)
    frontier: list[tuple[int, int, int]] = []

    # visited is a dict of vertex:distance
    visited: dict[int, int] = {}
    plan: Plan = {}
    # use heap to implement frontier priority queue
    heappush(frontier, (0, origin, origin))

    while frontier:
        # pop total_distance, vertex from frontier
        total_distance, vertex, source = heappop(frontier)

        # if vertex in visited, continue to next iteration
        if vertex in visited:
            continue
        
        # add vertex:total_distance to visited
        visited[vertex] = total_distance
        plan[vertex] = source
        if vertex == destination:
            break
        # push each unvisited neighbor with its total_distance to frontier
        if vertex not in graph:
            continue

        for neighbor, weight in graph[vertex].items():
            if neighbor not in visited:
                heappush(frontier, (total_distance + weight, neighbor, vertex))
    del plan[origin]
    return (visited[destination], plan)


def generate_flight_path(origin: int, destination: int, plan: Plan) -> Iterator[int]:
    # TODO:
    if origin == destination:
        yield origin
    else:
        yield from generate_flight_path(origin, plan[destination], plan)
        yield destination

def main(args=None) -> None:
    if args is None:
        args = sys.argv[1:]
    
    origin      = int(args[0])
    destination = int(args[1])
    graph_fname = args[2]

    with open(graph_fname) as stream:
        graph = read_graph(stream)
    
    cost, plan = find_cheapest_flight_plan(origin, destination, graph)
    stops = generate_flight_path(origin, destination, plan)
    print(f'Cost: ${cost}, Plan: {" -> ".join(map(str, stops))}')

if __name__ == '__main__':
    main()