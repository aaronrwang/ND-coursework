#!/usr/bin/env python3

import sys

from priority_queue import PriorityQueue

# Functions

def fill_cups(cups):
    pq = PriorityQueue()
    for i in cups:
        if i > 0:
            pq.push(i)
    counter = 0
    while pq.__len__()>1:
        temp1 = pq.pop() - 1
        temp2 = pq.pop() - 1
        if temp1 != 0:
            pq.push(temp1)
        if temp2 != 0:
            pq.push(temp2)
        counter+=1
    leftover = 0 if not pq.__bool__() else pq.pop()
    return counter + leftover


def main(stream=sys.stdin):
    # TODO
    for line in stream:
        print(fill_cups(int(i) for i in line.split())) 

if __name__ == '__main__':
    main()

