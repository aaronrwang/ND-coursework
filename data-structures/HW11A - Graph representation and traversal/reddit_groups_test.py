#!/usr/bin/env python3

import io
import unittest
import unittest.mock

import reddit_groups

class RedditGroupsTests(unittest.TestCase):
    AssignmentTotal = 40
    Total = 3
    Points = 0

    Graph1 = '4\n3\n0 1\n1 2\n3 0\n'
    AL1    = {0: [1, 3], 1: [0, 2], 2: [1], 3: [0]}

    Graph2 = '4\n2\n0 1\n2 3\n'
    AL2    = {0: [1], 1: [0], 2: [3], 3: [2]}

    Graph3 = '10\n7\n0 1\n5 7\n7 0\n9 5\n6 4\n2 5\n5 1\n'
    AL3    = {
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


    def test_00_walk_graph(self):
        self.assertEqual(reddit_groups.walk_graph(self.AL1, 0), {0, 1, 2, 3})
        self.assertEqual(reddit_groups.walk_graph(self.AL2, 0), {0, 1})
        self.assertEqual(reddit_groups.walk_graph(self.AL2, 2), {2, 3})
        self.assertEqual(reddit_groups.walk_graph(self.AL3, 0), {0, 1, 2, 5, 7, 9})
        self.assertEqual(reddit_groups.walk_graph(self.AL3, 4), {4, 6})
        RedditGroupsTests.Points += 1


    def test_01_find_groups(self):
        groups = reddit_groups.find_groups(self.AL1)
        self.assertEqual(next(groups), [0, 1, 2, 3])
        groups = reddit_groups.find_groups(self.AL2)
        self.assertEqual(next(groups), [0, 1])
        self.assertEqual(next(groups), [2, 3])
        groups = reddit_groups.find_groups(self.AL3)
        self.assertEqual(next(groups), [0, 1, 2, 5, 7, 9])
        self.assertEqual(next(groups), [4, 6])
        RedditGroupsTests.Points += 1


    def test_02_main(self):
        mock_stdin = io.StringIO(self.Graph1)
        expected_stdout = '0 1 2 3'
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            reddit_groups.main(mock_stdin)
            self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)

        mock_stdin = io.StringIO(self.Graph2)
        expected_stdout = '0 1\n2 3'
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            reddit_groups.main(mock_stdin)
            self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)

        mock_stdin = io.StringIO(self.Graph3)
        expected_stdout = '0 1 2 5 7 9\n4 6'
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            reddit_groups.main(mock_stdin)
            self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)

        with open('reddit_groups_input.graph', 'r') as infile:
            mock_stdin = io.StringIO(infile.read())
            expected_stdout = f'1 2 3 4\n5 6 7\n8 9'
            with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
                reddit_groups.main(mock_stdin)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)

        RedditGroupsTests.Points += 1


if __name__ == '__main__':
    unittest.main()
