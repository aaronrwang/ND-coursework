#!/usr/bin/env python3

# import doctest
import io
import unittest
import unittest.mock
from math import isclose

import cups

# Unit Tests

class CupsTest(unittest.TestCase):
    AssignmentTotal = 35
    Total  = 2
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
    
    def test_fill_cups(self):
        self.assertEqual(cups.fill_cups([1, 4, 2]), 4)
        self.assertEqual(cups.fill_cups([5, 4, 4]), 7)
        self.assertEqual(cups.fill_cups([5, 0, 0]), 5)
        CupsTest.Points += 1.0
    
    def test_main(self):
        indata = io.StringIO('1 4 2\n5 4 4\n5 0 0\n')
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as output:
            cups.main(indata)
            outstrings = output.getvalue().splitlines()
            outvalues = [int(s) for s in outstrings]
            self.assertEqual(outvalues, [4, 7, 5])
        CupsTest.Points += 1.0

# Main Execution

if __name__ == '__main__':
    unittest.main()
