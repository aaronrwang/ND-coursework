#!/usr/bin/env python3

import io
import unittest
import unittest.mock

import passcode

class PasscodeTests(unittest.TestCase):
    AssignmentTotal = 30
    Total = 4
    Points = 0

    Input1    = '352\n154\n542\n315\n152\n'
    Graph1    = {3: {1, 5}, 5: {2, 4}, 1: {5}, 4: {2}}
    Degrees1  = {3: 0, 1: 1, 5: 2, 2: 2, 4: 1}
    Ordering1 = [3, 1, 5, 4, 2]

    Input2    = '219\n183\n804\n376\n043\n904\n357\n857\n206\n180\n983\n284\n843\n'
    Graph2    = {
        0: {4, 6},
        1: {8, 9},
        2: {0, 1, 8},
        3: {5, 7},
        4: {3},
        5: {7},
        7: {6},
        8: {0, 3, 4, 5},
        9: {0, 8},
    }
    Degrees2  = {2: 0, 0: 3, 1: 1, 8: 3, 9: 1, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2}
    Ordering2 = [2, 1, 9, 8, 0, 4, 3, 5, 7, 6]

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
        stream = io.StringIO(self.Input1)
        self.assertEqual(passcode.read_graph(stream), self.Graph1)

        stream = io.StringIO(self.Input2)
        self.assertEqual(passcode.read_graph(stream), self.Graph2)

        PasscodeTests.Points += 1

    def test_01_compute_degrees(self):
        self.assertEqual(passcode.compute_degrees(self.Graph1), self.Degrees1)
        self.assertEqual(passcode.compute_degrees(self.Graph2), self.Degrees2)

        PasscodeTests.Points += 1

    def test_02_find_passcode(self):
        self.assertEqual(passcode.find_passcode(self.Graph1), self.Ordering1)
        self.assertEqual(passcode.find_passcode(self.Graph2), self.Ordering2)

        PasscodeTests.Points += 1

    def test_03_main(self):
        mock_file_contents = self.Input1
        mock_args = ['dummy.txt']
        expected_stdout = ''.join(map(str, self.Ordering1))
        with unittest.mock.patch('builtins.open', return_value=io.StringIO(mock_file_contents)), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
                passcode.main(mock_args)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)

        mock_file_contents = self.Input2
        mock_args = ['dummy.txt']
        expected_stdout = ''.join(map(str, self.Ordering2))
        with unittest.mock.patch('builtins.open', return_value=io.StringIO(mock_file_contents)), \
             unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
                passcode.main(mock_args)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_stdout)

        PasscodeTests.Points += 1

# Main Execution

if __name__ == '__main__':
    unittest.main()

