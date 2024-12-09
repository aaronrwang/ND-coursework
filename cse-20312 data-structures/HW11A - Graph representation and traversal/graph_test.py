#!/usr/bin/env python3

import io
import unittest
import textwrap

from graph import (
    read_adjacency_matrix,
    read_adjacency_list,
)

class GraphTests(unittest.TestCase):
    AssignmentTotal = 30
    Total = 2
    Points = 0

    Graph1 = textwrap.dedent('''
        4
        3
        0 1
        1 2
        3 1        
    ''').strip()
    AM1 =  [[0, 1, 0, 0], 
            [1, 0, 1, 1], 
            [0, 1, 0, 0], 
            [0, 1, 0, 0]]

    Graph2 = textwrap.dedent('''
        5
        4
        0 1
        4 0
        0 2
        0 3
    ''').strip()
    AM2 =  [[0, 1, 1, 1, 1], 
            [1, 0, 0, 0, 0], 
            [1, 0, 0, 0, 0], 
            [1, 0, 0, 0, 0], 
            [1, 0, 0, 0, 0]]

    Graph3 = textwrap.dedent('''
        5
        4
        0 1
        4 0
        0 2
        1 3
    ''').strip()
    AM3 =  [[0, 1, 1, 0, 1], 
            [1, 0, 0, 1, 0], 
            [1, 0, 0, 0, 0], 
            [0, 1, 0, 0, 0], 
            [1, 0, 0, 0, 0]]

    Graph4 = textwrap.dedent('''
        4
        3
        0 1
        1 2
        3 0
    ''').strip()
    AL4 = {0: [1, 3], 1: [0, 2], 2: [1], 3: [0]}

    Graph5 = textwrap.dedent('''
        4
        2
        0 1
        2 3
    ''').strip()
    AL5 = {0: [1], 1: [0], 2: [3], 3: [2]}

    Graph6 = textwrap.dedent('''
        8
        7
        0 1
        5 7
        7 0
        9 5
        6 4
        2 5
        5 1
    ''').strip()
    AL6 = {
        0: [1, 7],
        1: [0, 5],
        2: [5],
        4: [6],
        5: [7, 9, 2, 1],
        6: [4],
        7: [5, 0],
        9: [5]
    }

    @classmethod
    def setupClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        assignment_points = cls.AssignmentTotal * cls.Points / cls.Total
        print()
        print(f'   Score {assignment_points:.2f} / {cls.AssignmentTotal:.2f}')
        print(f'  Status {"Success" if cls.Points >= cls.Total else "Failure"}')

    def test_00_read_adjacency_matrix(self):
        mock_stdin = io.StringIO(self.Graph1)
        self.assertEqual(read_adjacency_matrix(mock_stdin), self.AM1)
        mock_stdin = io.StringIO(self.Graph2)
        self.assertEqual(read_adjacency_matrix(mock_stdin), self.AM2)
        mock_stdin = io.StringIO(self.Graph3)
        self.assertEqual(read_adjacency_matrix(mock_stdin), self.AM3)
        GraphTests.Points += 1

    def test_01_read_adjacency_list(self):
        mock_stdin = io.StringIO(self.Graph4)
        self.assertEqual(read_adjacency_list(mock_stdin), self.AL4)
        mock_stdin = io.StringIO(self.Graph5)
        self.assertEqual(read_adjacency_list(mock_stdin), self.AL5)
        mock_stdin = io.StringIO(self.Graph6)
        self.assertEqual(read_adjacency_list(mock_stdin), self.AL6)
        GraphTests.Points += 1


if __name__ == '__main__':
    unittest.main()
