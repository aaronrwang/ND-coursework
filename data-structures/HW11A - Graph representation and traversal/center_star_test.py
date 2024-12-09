#!/usr/bin/env python3

import io
import unittest
import unittest.mock
import center_star

class CenterStarTests(unittest.TestCase):
    AssignmentTotal = 30
    Total = 2
    Points = 0

    Graph1  = '4\n3\n0 1\n1 2\n3 1\n'
    AM1     = [[0, 1, 0, 0], 
               [1, 0, 1, 1], 
               [0, 1, 0, 0], 
               [0, 1, 0, 0]]
    Center1 = 1

    Graph2  = '5\n4\n0 1\n4 0\n0 2\n0 3\n'
    AM2     = [[0, 1, 1, 1, 1], 
               [1, 0, 0, 0, 0], 
               [1, 0, 0, 0, 0], 
               [1, 0, 0, 0, 0], 
               [1, 0, 0, 0, 0]]
    Center2 = 0

    Graph3  = '5\n4\n0 1\n4 0\n0 2\n1 3\n'
    AM3     = [[0, 1, 1, 0, 1], 
               [1, 0, 0, 1, 0], 
               [1, 0, 0, 0, 0], 
               [0, 1, 0, 0, 0], 
               [1, 0, 0, 0, 0]]
    Center3 = -1

    @classmethod
    def setupClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        assignment_points = cls.AssignmentTotal * cls.Points / cls.Total
        print()
        print(f'   Score {assignment_points:.2f} / {cls.AssignmentTotal:.2f}')
        print(f'  Status {"Success" if cls.Points >= cls.Total else "Failure"}')

    def test_00_find_center(self):
        self.assertEqual(center_star.find_center(self.AM1), self.Center1)
        self.assertEqual(center_star.find_center(self.AM2), self.Center2)
        self.assertEqual(center_star.find_center(self.AM3), self.Center3)
        CenterStarTests.Points += 1

    def test_01_main(self):
        mock_stdin = io.StringIO(self.Graph1)
        expected_stdout = f'Vertex {self.Center1} is the center'
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            center_star.main(mock_stdin)
            self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)

        mock_stdin = io.StringIO(self.Graph2)
        expected_stdout = f'Vertex {self.Center2} is the center'
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            center_star.main(mock_stdin)
            self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)

        mock_stdin = io.StringIO(self.Graph3)
        expected_stdout = 'There is no center'
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            center_star.main(mock_stdin)
            self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)

        with open('center_star_input.graph', 'r') as infile:
            mock_stdin = io.StringIO(infile.read())
            expected_stdout = f'Vertex 4 is the center'
            with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
                center_star.main(mock_stdin)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)
        
        CenterStarTests.Points += 1


if __name__ == '__main__':
    unittest.main()
