#!/usr/bin/env python3

from heap import MinHeap
from node import Node
import unittest

class MinHeapTest(unittest.TestCase):
    AssignmentTotal = 20
    Total = 4
    Points = 0

    @classmethod
    def setupClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        assignment_points = cls.AssignmentTotal * cls.Points / cls.Total
        print()
        print(f'   Score {assignment_points:.2f} / {cls.AssignmentTotal:.2f}')
        print(f'  Status {"Success" if cls.Points >= cls.Total else "Failure"}')

    def test_min_heap_insert_int(self):
        min_heap = MinHeap()
        min_heap.insert(10)
        self.assertEqual(min_heap.heap_array, [10])
        min_heap.insert(5)
        self.assertEqual(min_heap.heap_array, [5, 10])
        min_heap.insert(2)
        self.assertEqual(min_heap.heap_array, [2, 10, 5])
        min_heap.insert(1)
        self.assertEqual(min_heap.heap_array, [1, 2, 5, 10])
        min_heap.insert(6)
        self.assertEqual(min_heap.heap_array, [1, 2, 5, 10, 6])
        MinHeapTest.Points += 1

    def test_min_heap_remove_int(self):
        min_heap = MinHeap()
        min_heap.insert(10)
        min_heap.insert(5)
        min_heap.insert(2)
        min_heap.insert(1)
        min_heap.insert(6)
        self.assertEqual(min_heap.heap_array, [1, 2, 5, 10, 6])
        self.assertEqual(min_heap.remove(), 1)
        self.assertEqual(min_heap.heap_array, [2, 6, 5, 10])
        self.assertEqual(min_heap.remove(), 2)
        self.assertEqual(min_heap.heap_array, [5, 6, 10])
        self.assertEqual(min_heap.remove(), 5)
        self.assertEqual(min_heap.heap_array, [6, 10])
        self.assertEqual(min_heap.remove(), 6)
        self.assertEqual(min_heap.heap_array, [10])
        self.assertEqual(min_heap.remove(), 10)
        self.assertEqual(min_heap.heap_array, [])
        MinHeapTest.Points += 1

    def test_min_heap_len(self):
        min_heap = MinHeap()
        self.assertEqual(len(min_heap), 0)
        # __bool__ defaults to len() > 0
        self.assertFalse(min_heap)
        min_heap.insert(10)
        self.assertEqual(len(min_heap), 1)
        self.assertTrue(min_heap)
        min_heap.insert(20)
        self.assertEqual(len(min_heap), 2)
        min_heap.remove()
        self.assertEqual(len(min_heap), 1)
        min_heap.remove()
        self.assertEqual(len(min_heap), 0)
        self.assertFalse(min_heap)
        MinHeapTest.Points += 1

    def test_min_heap_insert_remove_node(self):
        min_heap = MinHeap()
        # Test inserting and removing nodes
        min_heap.insert(Node('a', 10))
        self.assertEqual(min_heap.heap_array[0].value, 10)
        self.assertEqual(min_heap.heap_array[0].key, 'a')
        min_heap.insert(Node('b', 5))
        self.assertEqual(min_heap.heap_array[0].value, 5)
        self.assertEqual(min_heap.heap_array[0].key, 'b')
        self.assertEqual(min_heap.heap_array[1].value, 10)
        self.assertEqual(min_heap.heap_array[1].key, 'a')
        min_heap.insert(Node('c', 5))
        self.assertEqual(min_heap.heap_array[2].value, 5)
        self.assertEqual(min_heap.heap_array[2].key, 'c')
        self.assertEqual(min_heap.remove().key, 'b')
        self.assertEqual(min_heap.remove().key, 'c')
        self.assertEqual(min_heap.remove().key, 'a')
        self.assertEqual(min_heap.heap_array, [])
        # Check that there is no perolating up when values are the same
        min_heap.insert(Node('a', 10))
        min_heap.insert(Node('b', 10))
        min_heap.insert(Node('c', 10))
        self.assertEqual(min_heap.heap_array[0].key, 'a')
        self.assertEqual(min_heap.heap_array[1].key, 'b')
        self.assertEqual(min_heap.heap_array[2].key, 'c')
        # Check that there is no perolating down when values are the same
        min_heap.remove()
        self.assertEqual(min_heap.heap_array[0].key, 'c')
        min_heap.remove()
        self.assertEqual(min_heap.heap_array[0].key, 'b')
        min_heap.remove()
        self.assertEqual(min_heap.heap_array, [])
        # Check that the left child is prioritized when percolating down
        min_heap.insert(Node('a', 1))
        min_heap.insert(Node('b', 2))
        min_heap.insert(Node('c', 3))
        min_heap.insert(Node('d', 3))
        min_heap.insert(Node('e', 3))
        min_heap.insert(Node('f', 4))
        self.assertEqual(min_heap.heap_array[0].key, 'a')
        self.assertEqual(min_heap.heap_array[1].key, 'b')
        self.assertEqual(min_heap.heap_array[2].key, 'c')
        self.assertEqual(min_heap.heap_array[3].key, 'd')
        self.assertEqual(min_heap.heap_array[4].key, 'e')
        self.assertEqual(min_heap.heap_array[5].key, 'f')
        min_heap.remove()
        self.assertEqual(min_heap.heap_array[1].key, 'd')
        self.assertEqual(min_heap.heap_array[3].key, 'f')
        min_heap.remove()
        MinHeapTest.Points += 1

if __name__ == '__main__':
    unittest.main()