#!/usr/bin/env python3

from node import Node
from heap import MinHeap
from huffman_tree_print import pretty_tree
from typing import Optional
import sys

def build_frequency_table(input_string: str) -> dict[str, int]:
    table = {}
    for i in range(len(input_string)):
        curr = input_string[i]
        table[curr] = table.get(curr,0) + 1
    return table


def huffman_build_tree(input_string: str) -> Node:
    # First build the frequency table
    table = build_frequency_table(input_string)

    # Make a priority queue of nodes
    nodes = MinHeap()
    for character, frequency in table.items():
        newLeaf = Node(character, frequency)
        nodes.insert(newLeaf)

    # Make parent nodes up to the root
    while len(nodes) > 1:
        # Dequeue 2 lowest-priority nodes
        left = nodes.remove()
        right = nodes.remove()

        # Make a parent for the two nodes
        freqSum = right.value + left.value
        key = left.key+right.key
        parent = Node(key, freqSum, left, right)

        # Enqueue parent back into priority queue
        nodes.insert(parent)

    return nodes.remove()

def huffman_get_codes(root: Node, prefix: str='') -> dict[str, str]:
    res = {}
    if not root.left and not root.right:
        res[root.key] = prefix
        return res
    else:
        left = huffman_get_codes(root.left, prefix + "0")
        right = huffman_get_codes(root.right, prefix + "1")
        return left|right

def huffman_compress(input_string: str) -> tuple[str, Node, dict[str, str]]:
    # Build the Huffman tree
    root = huffman_build_tree(input_string)

    # Get the compression codes from the tree
    codes = huffman_get_codes(root, "")
    
    # Build the compressed result
    result = ""
    for c in input_string:
        result += codes[c]

    return [result, root, codes]

def huffman_decompress(compressed_string: str, root: Node) -> str:
    node = root
    result = ""
    for bit in compressed_string:
        
        # Go to left or right child based on bit value
        if bit == '0':
            node = node.left
        else:
            node = node.right

        # If the node is a leaf, add the character to the 
        # decompressed result and go back to the root node
        if not node.left and not node.right:
            result += node.key
            node = root
    return result

def huffman_compression_ratio(original_string: str, compressed_string: str) -> float:
    return (len(original_string)*8.0)/len(compressed_string)

def main(stream=sys.stdin) -> None:
    text = stream.read().strip()
    compressed_string, tree, codes = huffman_compress(text)
    decompressed_string = huffman_decompress(compressed_string, tree)
    print('Original string:')
    print(text)
    print('Codes:')
    for symbol, code in sorted(codes.items(), key=lambda x: (len(x[1]), x[1])):
        print(f'{repr(symbol)[1:-1]} {code}')
    print(f'Compressed string:')
    print(compressed_string)
    print(f'Decompressed string:')
    print(decompressed_string)
    print(f'Compression ratio: {huffman_compression_ratio(text, compressed_string):.2f}')


if __name__ == "__main__":
    main()