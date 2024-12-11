#!/usr/bin/env python3

import io
import unittest
import unittest.mock
import textwrap

import flights

# Flights Unit Tests

class FlightsTests(unittest.TestCase):
    AssignmentTotal = 35
    Total = 4
    Points = 0

    EdgeList1 = textwrap.dedent('''
        0 1 100
        1 2 50
        0 2 365
    ''').strip()
    Graph1 = {0: {1: 100, 2: 365}, 1: {2: 50}}

    EdgeList2 = textwrap.dedent('''
        0 1 1
        0 2 5
        1 2 1
        2 3 1
    ''').strip()
    Graph2 = {0: {1: 1, 2: 5}, 1: {2: 1}, 2: {3: 1}}

    EdgeList3 = textwrap.dedent('''
        0 1 50
        0 2 200
        1 2 100
        1 3 50
        2 5 100
        2 4 50
        2 3 50
        3 4 200
        4 6 300
        5 6 50
        5 0 600
        6 2 50
    ''').strip()
    Graph3 = {
        0: {1: 50, 2: 200},
        1: {2: 100, 3: 50},
        2: {5: 100, 4: 50, 3: 50},
        3: {4: 200},
        4: {6: 300},
        5: {6: 50, 0: 600},
        6: {2: 50}
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

    def test_00_read_graph(self):
        stream = io.StringIO(self.EdgeList1)
        graph = flights.read_graph(stream)
        self.assertEqual(graph, self.Graph1)

        stream = io.StringIO(self.EdgeList2)
        graph = flights.read_graph(stream)
        self.assertEqual(graph, self.Graph2)

        stream = io.StringIO(self.EdgeList3)
        graph = flights.read_graph(stream)
        self.assertEqual(graph, self.Graph3)

        FlightsTests.Points += 1

    def test_01_find_cheapest_flight_plan(self):
        cost, plan = flights.find_cheapest_flight_plan(0, 2, self.Graph1)
        self.assertEqual((cost, plan), (150, {1: 0, 2: 1}))
        cost, plan = flights.find_cheapest_flight_plan(0, 1, self.Graph1)
        self.assertEqual((cost, plan), (100, {1: 0}))

        cost, plan = flights.find_cheapest_flight_plan(0, 2, self.Graph2)
        self.assertEqual((cost, plan), (2, {1: 0, 2: 1}))
        cost, plan = flights.find_cheapest_flight_plan(0, 3, self.Graph2)
        self.assertEqual((cost, plan), (3, {1: 0, 2: 1, 3: 2}))

        cost, plan = flights.find_cheapest_flight_plan(0, 1, self.Graph3)
        self.assertEqual((cost, plan), (50, {1: 0}))
        cost, plan = flights.find_cheapest_flight_plan(0, 2, self.Graph3)
        self.assertEqual((cost, plan), (150, {1: 0, 2: 1, 3: 1}))
        cost, plan = flights.find_cheapest_flight_plan(0, 3, self.Graph3)
        self.assertEqual((cost, plan), (100, {1: 0, 3: 1}))
        cost, plan = flights.find_cheapest_flight_plan(0, 4, self.Graph3)
        self.assertEqual((cost, plan), (200, {1: 0, 2: 1, 3: 1, 4: 2}))
        cost, plan = flights.find_cheapest_flight_plan(0, 5, self.Graph3)
        self.assertEqual((cost, plan), (250, {1: 0, 2: 1, 3: 1, 4: 2, 5: 2}))
        cost, plan = flights.find_cheapest_flight_plan(0, 6, self.Graph3)
        self.assertEqual((cost, plan), (300, {1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 5}))
        cost, plan = flights.find_cheapest_flight_plan(5, 4, self.Graph3)
        self.assertEqual((cost, plan), (150, {2: 6, 3: 2, 4: 2, 6: 5}))
        cost, plan = flights.find_cheapest_flight_plan(5, 1, self.Graph3)
        self.assertEqual((cost, plan), (650, {0: 5, 1: 0, 2: 6, 3: 2, 4: 2, 6: 5}))
        cost, plan = flights.find_cheapest_flight_plan(5, 3, self.Graph3)
        self.assertEqual((cost, plan), (150, {2: 6, 3: 2, 6: 5}))

        FlightsTests.Points += 1

    def test_02_generate_flight_path(self): 
        edges = {1: 0}
        route = flights.generate_flight_path(0, 0, edges)
        self.assertEqual(list(route), [0])
        route = flights.generate_flight_path(0, 1, edges)
        self.assertEqual(list(route), [0, 1])

        edges = {1: 0, 2: 1}
        route = flights.generate_flight_path(0, 0, edges)
        self.assertEqual(list(route), [0])
        route = flights.generate_flight_path(0, 1, edges)
        self.assertEqual(list(route), [0, 1])
        route = flights.generate_flight_path(0, 2, edges)
        self.assertEqual(list(route), [0, 1, 2])

        edges = {1: 3, 2: 4, 4: 1}
        route = flights.generate_flight_path(3, 3, edges)
        self.assertEqual(list(route), [3])
        route = flights.generate_flight_path(3, 1, edges)
        self.assertEqual(list(route), [3, 1])
        route = flights.generate_flight_path(3, 4, edges)
        self.assertEqual(list(route), [3, 1, 4])
        route = flights.generate_flight_path(3, 2, edges)
        self.assertEqual(list(route), [3, 1, 4, 2])

        edges = {1: 0, 2: 1, 3: 1}
        route = flights.generate_flight_path(0, 2, edges)
        self.assertEqual(list(route), [0, 1, 2])
        route = flights.generate_flight_path(0, 3, edges)
        self.assertEqual(list(route), [0, 1, 3])

        FlightsTests.Points += 1

    def test_03_main(self):   
        mock_file_content = self.EdgeList1
        mock_args = ['0', '1', 'dummy.txt']
        expected_stdout = 'Cost: $100, Plan: 0 -> 1'
        with unittest.mock.patch('builtins.open', return_value=io.StringIO(mock_file_content)), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            flights.main(mock_args)
            self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)
        
        mock_file_content = self.EdgeList1
        mock_args = ['0', '2', 'dummy.txt']
        expected_stdout = 'Cost: $150, Plan: 0 -> 1 -> 2'
        with unittest.mock.patch('builtins.open', return_value=io.StringIO(mock_file_content)), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            flights.main(mock_args)
            self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)

        mock_file_content = self.EdgeList2
        mock_args = ['0', '2', 'dummy.txt']
        expected_stdout = 'Cost: $2, Plan: 0 -> 1 -> 2'
        with unittest.mock.patch('builtins.open', return_value=io.StringIO(mock_file_content)), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            flights.main(mock_args)
            self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)

        mock_file_content = self.EdgeList2
        mock_args = ['0', '3', 'dummy.txt']
        expected_stdout = 'Cost: $3, Plan: 0 -> 1 -> 2 -> 3'
        with unittest.mock.patch('builtins.open', return_value=io.StringIO(mock_file_content)), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            flights.main(mock_args)
            self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)

        mock_file_content = self.EdgeList3
        mock_args = ['0', '1', 'dummy.txt']
        expected_stdout = 'Cost: $50, Plan: 0 -> 1'
        with unittest.mock.patch('builtins.open', return_value=io.StringIO(mock_file_content)), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            flights.main(mock_args)
            self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)
        
        mock_file_content = self.EdgeList3
        mock_args = ['0', '6', 'dummy.txt']
        expected_stdout = 'Cost: $300, Plan: 0 -> 1 -> 2 -> 5 -> 6'
        with unittest.mock.patch('builtins.open', return_value=io.StringIO(mock_file_content)), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            flights.main(mock_args)
            self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)

        FlightsTests.Points += 1

# Main Execution

if __name__ == '__main__':
    unittest.main()

