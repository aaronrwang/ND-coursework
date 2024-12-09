#!/usr/bin/env python3

''' sim_city.py - Sim City '''

import sys

from collections import defaultdict
from heapq       import heappop, heappush
from math        import dist

# Types

Points = list[tuple[int, float, float]]
Graph  = dict[int, dict[int, float]]
Edges  = dict[int, int]

# Functions

def read_points(stream) -> Points:
    points: Points = []
    point = 0
    for line in stream:
        x, y = line.split()
        points.append((point,float(x),float(y)))
        point+=1
    return points

def build_graph(points: Points) -> Graph:
    # TODO:
    graph = Graph = {}
    n = len(points)
    for point in points:
        graph[point[0]] = {}
    for i in range(n-1):
        for j in range(i+1,n):
            distance = dist((points[i][1],points[i][2]),(points[j][1],points[j][2]))
            graph[points[i][0]][points[j][0]] = distance
            graph[points[j][0]][points[i][0]] = distance
    return graph

def construct_mst(graph) -> tuple[float, Edges]:
    frontier: list[tuple[int, int, int]] = []
    origin = list(graph.keys())[0]
    edges: Edges = {}
    heappush(frontier, (0, origin, origin))
    total = 0
    while frontier:
        distance, vertex, source = heappop(frontier)
        if vertex in edges:
            continue
        edges[vertex] = source
        total+= distance
        for neighbor, weight in graph[vertex].items():
            if neighbor not in edges:
                heappush(frontier, (weight, neighbor, vertex))
    del edges[origin]
    return (total, edges)


        

# Main Execution

def main(args=None) -> None:
    if args is None:
        args = sys.argv[1:]

    points_fname = args[0]

    with open(points_fname) as stream:
        points = read_points(stream)
    graph = build_graph(points)
    total_length, edges = construct_mst(graph)
    print(f'Length: {total_length:.2f}', end=' ')
    print('Edges: '+', '.join(f'{p1}-{p2}' for p1, p2 in edges.items()))

if __name__ == '__main__':
    main()