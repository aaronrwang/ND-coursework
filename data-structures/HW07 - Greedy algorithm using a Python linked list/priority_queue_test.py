#!/usr/bin/env python3

import unittest
from priority_queue import PriorityQueue

class PriorityQueueTest(unittest.TestCase):
    AssignmentTotal = 30
    Total  = 5
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

    def test_push(self):
        pq = PriorityQueue()
        pq.push(2)
        pq.push(3)
        pq.push(1)
        self.assertEqual(str(pq), "1 2 3")
        PriorityQueueTest.Points += 1

    def test_pop(self):
        pq = PriorityQueue([2, 3, 1])
        self.assertEqual(pq.pop(), 3)
        self.assertEqual(pq.pop(), 2)
        self.assertEqual(pq.pop(), 1)
        self.assertEqual(str(pq), "")
        PriorityQueueTest.Points += 1

    def test_peek(self):
        pq = PriorityQueue([2, 3, 1])
        self.assertEqual(pq.peek(), 3)
        self.assertEqual(str(pq), "1 2 3")
        PriorityQueueTest.Points += 1

    def test_bool(self):
        pq = PriorityQueue()
        self.assertFalse(pq)
        pq.push(1)
        self.assertTrue(pq)
        pq.pop()
        self.assertFalse(pq)
        PriorityQueueTest.Points += 1

    def test_len(self):
        pq = PriorityQueue([2, 3, 1])
        self.assertEqual(len(pq), 3)
        pq.pop()
        self.assertEqual(len(pq), 2)
        pq.pop()
        self.assertEqual(len(pq), 1)
        pq.pop()
        self.assertEqual(len(pq), 0)
        PriorityQueueTest.Points += 1

if __name__ == '__main__':
    unittest.main()