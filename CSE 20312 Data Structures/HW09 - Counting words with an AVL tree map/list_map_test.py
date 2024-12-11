#!/usr/bin/env python3

import unittest
from list_map import ListMap

class ListMapTest(unittest.TestCase):
    AssignmentTotal = 45
    Total = 9
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

    def test_binary_search(self):
        list_map = ListMap()
        list_map.data = [['a', 1], ['b', 2], ['c', 3], ['d', 4], ['e', 5]]
        self.assertEqual(list_map._binary_search('a'), (0, 1))
        self.assertEqual(list_map._binary_search('b'), (1, 2))
        self.assertEqual(list_map._binary_search('c'), (2, 3))
        self.assertEqual(list_map._binary_search('d'), (3, 4))
        self.assertEqual(list_map._binary_search('e'), (4, 5))
        self.assertEqual(list_map._binary_search('f'), (5, None))
        ListMapTest.Points += 1

    def test_setitem(self):
        list_map = ListMap()
        list_map['a'] = 1
        list_map['b'] = 2
        list_map['c'] = 3
        list_map['d'] = 4
        list_map['e'] = 5
        self.assertEqual(list_map.data, [['a', 1], ['b', 2], ['c', 3], ['d', 4], ['e', 5]])
        list_map['c'] = 33
        self.assertEqual(list_map.data, [['a', 1], ['b', 2], ['c', 33], ['d', 4], ['e', 5]])
        ListMapTest.Points += 1

    def test_getitem(self):
        list_map = ListMap()
        list_map['a'] = 1
        list_map['b'] = 2
        list_map['c'] = 3
        list_map['d'] = 4
        list_map['e'] = 5
        self.assertEqual(list_map['a'], 1)
        self.assertEqual(list_map['b'], 2)
        self.assertEqual(list_map['c'], 3)
        self.assertEqual(list_map['d'], 4)
        self.assertEqual(list_map['e'], 5)
        with self.assertRaises(KeyError):
            list_map['f']
        ListMapTest.Points += 1

    def test_get(self):
        list_map = ListMap()
        list_map['a'] = 1
        list_map['b'] = 2
        list_map['c'] = 3
        list_map['d'] = 4
        list_map['e'] = 5
        self.assertEqual(list_map.get('a'), 1)
        self.assertEqual(list_map.get('b'), 2)
        self.assertEqual(list_map.get('c'), 3)
        self.assertEqual(list_map.get('d'), 4)
        self.assertEqual(list_map.get('e'), 5)
        self.assertEqual(list_map.get('f'), None)
        self.assertEqual(list_map.get('f', 'default'), 'default')
        ListMapTest.Points += 1

    def test_contains(self):
        list_map = ListMap()
        list_map['a'] = 1
        list_map['b'] = 2
        list_map['c'] = 3
        list_map['d'] = 4
        list_map['e'] = 5
        self.assertTrue('a' in list_map)
        self.assertTrue('b' in list_map)
        self.assertTrue('c' in list_map)
        self.assertTrue('d' in list_map)
        self.assertTrue('e' in list_map)
        self.assertFalse('f' in list_map)
        ListMapTest.Points += 1

    def test_pop(self):
        list_map = ListMap()
        list_map['a'] = 1
        list_map['b'] = 2
        list_map['c'] = 3
        list_map['d'] = 4
        list_map['e'] = 5
        self.assertEqual(list_map.pop('a'), 1)
        self.assertEqual(list_map.pop('c'), 3)
        self.assertEqual(list_map.pop('e'), 5)
        self.assertEqual(list_map.pop('b'), 2)
        self.assertEqual(list_map.pop('d'), 4)
        with self.assertRaises(KeyError):
            list_map.pop('f')
        ListMapTest.Points += 1

    def test_iter(self):
        list_map = ListMap()
        list_map['a'] = 1
        list_map['b'] = 2
        list_map['c'] = 3
        list_map['d'] = 4
        list_map['e'] = 5
        result = []
        for key in list_map:
            result.append(key)
        self.assertEqual(result, ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(list(list_map), ['a', 'b', 'c', 'd', 'e'])
        ListMapTest.Points += 1

    def test_items(self):
        list_map = ListMap()
        list_map['a'] = 1
        list_map['b'] = 2
        list_map['c'] = 3
        list_map['d'] = 4
        list_map['e'] = 5
        self.assertEqual(list(list_map.items()), [['a', 1], ['b', 2], ['c', 3], ['d', 4], ['e', 5]])
        ListMapTest.Points += 1

    def test_next(self):
        list_map = ListMap()
        list_map['a'] = 1
        list_map['b'] = 2
        list_map['c'] = 3
        list_map['d'] = 4
        list_map['e'] = 5
        iter_map = iter(list_map)
        self.assertEqual(next(iter_map), 'a')
        self.assertEqual(next(iter_map), 'b')
        self.assertEqual(next(iter_map), 'c')
        self.assertEqual(next(iter_map), 'd')
        self.assertEqual(next(iter_map), 'e')
        with self.assertRaises(StopIteration):
            next(iter_map)
        ListMapTest.Points += 1
        

if __name__ == '__main__':
    unittest.main()