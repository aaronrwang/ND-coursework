#!/usr/bin/env python3

from node import Node
import unittest

class NodeTest(unittest.TestCase):

    @classmethod
    def setupClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_eq_gt_ge_lt_le(self):
        node1 = Node('key1', 1)
        node2 = Node('key2', 1)
        node3 = Node('key3', 2)
        self.assertTrue(node1 == node2)
        self.assertTrue(node3 > node1)
        self.assertTrue(node3 >= node1)
        self.assertTrue(node1 < node3)
        self.assertTrue(node1 <= node3)
        self.assertTrue(node1 <= node2)
        self.assertTrue(node1 >= node2)
