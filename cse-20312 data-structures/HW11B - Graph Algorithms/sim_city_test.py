#!/usr/bin/env python3

import io
import unittest
import unittest.mock
import textwrap
from math import sqrt

import sim_city

class SimCityTests(unittest.TestCase):
    AssignmentTotal = 35
    Total = 4
    Points = 0

    # Test Case 1
    Input1 = textwrap.dedent('''
        0.0 0.0
        3.0 4.0
    ''').strip()
    PointList1 = [(0, 0.0, 0.0), (1, 3.0, 4.0)]
    Graph1 = {
        0: {1: 5.0},
        1: {0: 5.0}
    }
    MST1 = {1: 0}
    Length1 = 5.0
    
    # Test Case 2
    Input2 = textwrap.dedent('''
        0.0 0.0
        3.0 4.0
        3.0 0.0
    ''').strip()
    PointList2 = [(0, 0.0, 0.0), (1, 3.0, 4.0), (2, 3.0, 0.0)]
    Graph2 = {
        0: {1: 5.0, 2: 3.0},
        1: {0: 5.0, 2: 4.0},
        2: {0: 3.0, 1: 4.0}
    }
    MST2 = {2: 0, 1: 2}
    Length2 = 7.0

    # Test Case 3
    Input3 = textwrap.dedent('''
        0.0 0.0
        0.0 2.0
        3.0 2.0
        1.0 0.0
    ''').strip()
    PointList3 = [(0, 0.0, 0.0), (1, 0.0, 2.0), (2, 3.0, 2.0), (3, 1.0, 0.0)]
    Graph3 = {
        0: {1: 2.0, 2: sqrt(13), 3: 1.0},
        1: {0: 2.0, 2: 3.0, 3: sqrt(5)},
        2: {0: sqrt(13), 1: 3.0, 3: sqrt(8)},
        3: {0: 1.0, 1: sqrt(5), 2: sqrt(8)}
    }
    MST3 = {3: 0, 1: 0, 2: 3}
    Length3 = 2 + 1 + sqrt(8)

    # Test Case 4: from zyBook MST section
    Graph4 = {
        1: {2: 80.0, 3: 105.0, 5: 182.0}, 
        2: {1: 80.0, 3: 90.0, 4: 60.0, 8: 100.0}, 
        3: {1: 105.0, 2: 90.0, 8: 132.0}, 
        4: {2: 60.0, 5: 80.0}, 
        5: {1: 182.0, 4: 80.0, 6: 70.0}, 
        6: {5: 70.0, 7: 72.0, 8: 145.0}, 
        7: {6: 72.0, 8: 180.0},
        8: {2: 100.0, 3: 132.0, 6: 145.0, 7: 180.0}
    }
    MST4 = {2: 1, 4: 2, 5: 4, 6: 5, 7: 6, 3: 2, 8: 2}
    Length4 = 552.0


    @classmethod
    def setupClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        assignment_points = cls.AssignmentTotal * cls.Points / cls.Total
        print()
        print(f'   Score {assignment_points:.2f} / {cls.AssignmentTotal:.2f}')
        print(f'  Status {"Success" if cls.Points >= cls.Total else "Failure"}')

    def test_00_read_points(self):

        stream = io.StringIO(self.Input1)
        point_list = sim_city.read_points(stream)
        self.assertEqual(point_list, self.PointList1)

        stream = io.StringIO(self.Input2)
        point_list = sim_city.read_points(stream)
        self.assertEqual(point_list, self.PointList2)

        stream = io.StringIO(self.Input3)
        point_list = sim_city.read_points(stream)
        self.assertEqual(point_list, self.PointList3)

        SimCityTests.Points += 1

    def test_01_build_graph(self):

        graph = sim_city.build_graph(self.PointList1)
        self.assertEqual(len(graph), 2)
        for vertex in graph:
            self.assertEqual(len(graph[vertex]), 1)
        self.assertAlmostEqual(graph[0][1], 5.0)
        self.assertAlmostEqual(graph[1][0], 5.0)

        graph = sim_city.build_graph(self.PointList2)
        self.assertEqual(len(graph), 3)
        for vertex in graph:
            self.assertEqual(len(graph[vertex]), 2)
        self.assertAlmostEqual(graph[0][1], 5.0)
        self.assertAlmostEqual(graph[0][2], 3.0)
        self.assertAlmostEqual(graph[1][0], 5.0)
        self.assertAlmostEqual(graph[1][2], 4.0)
        self.assertAlmostEqual(graph[2][0], 3.0)
        self.assertAlmostEqual(graph[2][1], 4.0)

        graph = sim_city.build_graph(self.PointList3)
        self.assertEqual(len(graph), 4)
        for vertex in graph:
            self.assertEqual(len(graph[vertex]), 3)
        self.assertAlmostEqual(graph[0][1], 2.0)
        self.assertAlmostEqual(graph[0][2], sqrt(13))
        self.assertAlmostEqual(graph[0][3], 1.0)
        self.assertAlmostEqual(graph[1][0], 2.0)
        self.assertAlmostEqual(graph[1][2], 3.0)
        self.assertAlmostEqual(graph[1][3], sqrt(5))
        self.assertAlmostEqual(graph[2][0], sqrt(13))
        self.assertAlmostEqual(graph[2][1], 3.0)
        self.assertAlmostEqual(graph[2][3], sqrt(8))
        self.assertAlmostEqual(graph[3][0], 1.0)
        self.assertAlmostEqual(graph[3][1], sqrt(5))
        self.assertAlmostEqual(graph[3][2], sqrt(8))

        SimCityTests.Points += 1

    def test_02_construct_mst(self):

        distance, edges = sim_city.construct_mst(self.Graph1)
        self.assertEqual(edges, self.MST1)
        self.assertAlmostEqual(distance, self.Length1)

        distance, edges = sim_city.construct_mst(self.Graph2)
        self.assertEqual(edges, self.MST2)
        self.assertAlmostEqual(distance, self.Length2)

        distance, edges = sim_city.construct_mst(self.Graph3)
        self.assertEqual(edges, self.MST3)
        self.assertAlmostEqual(distance, self.Length3)

        distance, edges = sim_city.construct_mst(self.Graph4)
        self.assertEqual(edges, self.MST4)
        self.assertAlmostEqual(distance, self.Length4)

        SimCityTests.Points += 1

    def test_03_main(self):

        mock_file_contents = self.Input1
        mock_args = ['dummy.txt']
        expected_stdout = (
             f'Length: {self.Length1:.2f} ' +
             'Edges: ' + ', '.join(f'{p1}-{p2}' for p1, p2 in self.MST1.items())
        )
        with unittest.mock.patch('builtins.open', return_value=io.StringIO(mock_file_contents)), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
                sim_city.main(mock_args)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)

        mock_file_contents = self.Input2
        mock_args = ['dummy.txt']
        expected_stdout = (
             f'Length: {self.Length2:.2f} ' +
             'Edges: ' + ', '.join(f'{p1}-{p2}' for p1, p2 in self.MST2.items())
        )
        with unittest.mock.patch('builtins.open', return_value=io.StringIO(mock_file_contents)), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
                sim_city.main(mock_args)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)

        mock_file_contents = self.Input3
        mock_args = ['dummy.txt']
        expected_stdout = (
             f'Length: {self.Length3:.2f} ' +
             'Edges: ' + ', '.join(f'{p1}-{p2}' for p1, p2 in self.MST3.items())
        )
        with unittest.mock.patch('builtins.open', return_value=io.StringIO(mock_file_contents)), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
                sim_city.main(mock_args)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)

        SimCityTests.Points += 1

# Main Execution

if __name__ == '__main__':
    unittest.main()

