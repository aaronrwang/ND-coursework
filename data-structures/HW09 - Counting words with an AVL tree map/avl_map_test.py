#!/usr/bin/env python3

import unittest
from avl_map import AVLMap

class AvlMapTest(unittest.TestCase):
    AssignmentTotal = 45
    Total = 11
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

    def test_insert_or_update(self):
        avl_map = AVLMap()
        avl_map.root = avl_map._insert_or_update(avl_map.root, 'd', 4)
        self.assertEqual(avl_map.root.key, ['d', 4])
        avl_map.root = avl_map._insert_or_update(avl_map.root, 'd', 40)
        self.assertEqual(avl_map.root.key, ['d', 40])
        avl_map.root = avl_map._insert_or_update(avl_map.root, 'b', 2)
        self.assertEqual(avl_map.root.left.key, ['b', 2])
        avl_map.root = avl_map._insert_or_update(avl_map.root, 'b', 20)
        self.assertEqual(avl_map.root.left.key, ['b', 20])
        avl_map.root = avl_map._insert_or_update(avl_map.root, 'f', 6)
        self.assertEqual(avl_map.root.right.key, ['f', 6])
        avl_map.root = avl_map._insert_or_update(avl_map.root, 'f', 60)
        self.assertEqual(avl_map.root.right.key, ['f', 60])
        avl_map.root = avl_map._insert_or_update(avl_map.root, 'a', 1)
        self.assertEqual(avl_map.root.left.left.key, ['a', 1])
        avl_map.root = avl_map._insert_or_update(avl_map.root, 'a', 10)
        self.assertEqual(avl_map.root.left.left.key, ['a', 10])
        avl_map.root = avl_map._insert_or_update(avl_map.root, 'c', 3)
        self.assertEqual(avl_map.root.left.right.key, ['c', 3])
        avl_map.root = avl_map._insert_or_update(avl_map.root, 'c', 30)
        self.assertEqual(avl_map.root.left.right.key, ['c', 30])
        AvlMapTest.Points += 1

    def test_setitem(self):
        avl_map = AVLMap()
        avl_map['d'] = 4
        self.assertEqual(avl_map.root.key, ['d', 4])
        avl_map['d'] = 40
        self.assertEqual(avl_map.root.key, ['d', 40])
        avl_map['b'] = 2
        self.assertEqual(avl_map.root.left.key, ['b', 2])
        avl_map['b'] = 20
        self.assertEqual(avl_map.root.left.key, ['b', 20])
        avl_map['f'] = 6
        self.assertEqual(avl_map.root.right.key, ['f', 6])
        avl_map['f'] = 60
        self.assertEqual(avl_map.root.right.key, ['f', 60])
        avl_map['a'] = 1
        self.assertEqual(avl_map.root.left.left.key, ['a', 1])
        avl_map['a'] = 10
        self.assertEqual(avl_map.root.left.left.key, ['a', 10])
        avl_map['c'] = 3
        self.assertEqual(avl_map.root.left.right.key, ['c', 3])
        avl_map['c'] = 30
        self.assertEqual(avl_map.root.left.right.key, ['c', 30])
        AvlMapTest.Points += 1

    def test_get_node(self):
        avl_map = AVLMap()
        avl_map['d'] = 4
        self.assertEqual(avl_map._get_node(avl_map.root, 'd').key, ['d', 4])
        avl_map['b'] = 2
        self.assertEqual(avl_map._get_node(avl_map.root, 'b').key, ['b', 2])
        avl_map['f'] = 6
        self.assertEqual(avl_map._get_node(avl_map.root, 'f').key, ['f', 6])
        avl_map['a'] = 1
        self.assertEqual(avl_map._get_node(avl_map.root, 'a').key, ['a', 1])
        avl_map['c'] = 3
        self.assertEqual(avl_map._get_node(avl_map.root, 'c').key, ['c', 3])
        AvlMapTest.Points += 1

    def test_getitem(self):
        avl_map = AVLMap()
        avl_map['d'] = 4
        self.assertEqual(avl_map['d'], 4)
        avl_map['b'] = 2
        self.assertEqual(avl_map['b'], 2)
        avl_map['f'] = 6
        self.assertEqual(avl_map['f'], 6)
        avl_map['a'] = 1
        self.assertEqual(avl_map['a'], 1)
        avl_map['c'] = 3
        self.assertEqual(avl_map['c'], 3)
        self.assertRaises(KeyError, avl_map.__getitem__, 'z')
        AvlMapTest.Points += 1

    def test_get(self):
        avl_map = AVLMap()
        avl_map['d'] = 4
        self.assertEqual(avl_map.get('d'), 4)
        avl_map['b'] = 2
        self.assertEqual(avl_map.get('b'), 2)
        avl_map['f'] = 6
        self.assertEqual(avl_map.get('f'), 6)
        avl_map['a'] = 1
        self.assertEqual(avl_map.get('a'), 1)
        avl_map['c'] = 3
        self.assertEqual(avl_map.get('c'), 3)
        self.assertEqual(avl_map.get('z'), None)
        self.assertEqual(avl_map.get('z', 1), 1)
        AvlMapTest.Points += 1

    def test_contains(self):
        avl_map = AVLMap()
        avl_map['d'] = 4
        self.assertTrue('d' in avl_map)
        avl_map['b'] = 2
        self.assertTrue('b' in avl_map)
        avl_map['f'] = 6
        self.assertTrue('f' in avl_map)
        avl_map['a'] = 1
        self.assertTrue('a' in avl_map)
        avl_map['c'] = 3
        self.assertTrue('c' in avl_map)
        self.assertFalse('z' in avl_map)
        AvlMapTest.Points += 1

    def test_pop(self):
        avl_map = AVLMap()
        avl_map['d'] = 4
        avl_map['b'] = 2
        avl_map['f'] = 6
        avl_map['a'] = 1
        avl_map['c'] = 3
        self.assertEqual(avl_map.pop('d'), 4)
        self.assertEqual(avl_map.pop('b'), 2)
        self.assertEqual(avl_map.pop('f'), 6)
        self.assertEqual(avl_map.pop('a'), 1)
        self.assertEqual(avl_map.pop('c'), 3)
        AvlMapTest.Points += 1

    def test_inorder_generator(self):
        avl_map = AVLMap()
        avl_map['d'] = 4
        avl_map['b'] = 2
        avl_map['f'] = 6
        avl_map['a'] = 1
        avl_map['c'] = 3
        self.assertEqual(list(avl_map.inorder_generator()), [['a', 1], ['b', 2], ['c', 3], ['d', 4], ['f', 6]])
        AvlMapTest.Points += 1

    def test_items(self):
        avl_map = AVLMap()
        avl_map['d'] = 4
        avl_map['b'] = 2
        avl_map['f'] = 6
        avl_map['a'] = 1
        avl_map['c'] = 3
        self.assertEqual(list(avl_map.items()), [['a', 1], ['b', 2], ['c', 3], ['d', 4], ['f', 6]])
        AvlMapTest.Points += 1

    def test_iter(self):
        avl_map = AVLMap()
        avl_map['d'] = 4
        avl_map['b'] = 2
        avl_map['f'] = 6
        avl_map['a'] = 1
        avl_map['c'] = 3
        result = []
        for key in avl_map:
            result.append(key)
        self.assertEqual(result, ['a', 'b', 'c', 'd', 'f'])
        self.assertEqual(list(iter(avl_map)), ['a', 'b', 'c', 'd', 'f'])
        AvlMapTest.Points += 1

    def test_next(self):
        avl_map = AVLMap()
        avl_map['d'] = 4
        avl_map['b'] = 2
        avl_map['f'] = 6
        avl_map['a'] = 1
        avl_map['c'] = 3
        it = iter(avl_map)
        self.assertEqual(next(it), 'a')
        self.assertEqual(next(it), 'b')
        self.assertEqual(next(it), 'c')
        self.assertEqual(next(it), 'd')
        self.assertEqual(next(it), 'f')
        self.assertRaises(StopIteration, next, it)
        AvlMapTest.Points += 1

if __name__ == '__main__':
    unittest.main()