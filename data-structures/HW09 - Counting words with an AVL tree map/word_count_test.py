#!/usr/bin/env python3

from avl_map import AVLMap
from list_map import ListMap
import unittest
import unittest.mock
import sys
import io
import word_count

class WordCountTest(unittest.TestCase):
    AssignmentTotal = 10
    Total = 5
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

    def test_count_words_dict(self):
        word_count_map = {}
        word_count.count_words('fruit.txt', word_count_map)
        self.assertEqual(word_count_map['apple'], 1)
        self.assertEqual(word_count_map['banana'], 2)
        self.assertEqual(word_count_map['cherry'], 3)
        word_count_map = {}
        word_count.count_words('quotes.txt', word_count_map)
        self.assertEqual(word_count_map['the'], 9)
        self.assertEqual(word_count_map['of'], 6)
        self.assertEqual(word_count_map['and'], 6)
        self.assertEqual(word_count_map['to'], 4)
        WordCountTest.Points += 1

    def test_count_words_avl(self):
        word_count_map = AVLMap(do_balance=True)
        word_count.count_words('fruit.txt', word_count_map)
        self.assertEqual(word_count_map['apple'], 1)
        self.assertEqual(word_count_map['banana'], 2)
        self.assertEqual(word_count_map['cherry'], 3)
        word_count_map = AVLMap(do_balance=True)
        word_count.count_words('quotes.txt', word_count_map)
        self.assertEqual(word_count_map['the'], 9)
        self.assertEqual(word_count_map['of'], 6)
        self.assertEqual(word_count_map['and'], 6)
        self.assertEqual(word_count_map['to'], 4)
        WordCountTest.Points += 1

    def test_count_words_bst(self):
        word_count_map = AVLMap(do_balance=False)
        word_count.count_words('fruit.txt', word_count_map)
        self.assertEqual(word_count_map['apple'], 1)
        self.assertEqual(word_count_map['banana'], 2)
        self.assertEqual(word_count_map['cherry'], 3)
        word_count_map = AVLMap(do_balance=False)
        word_count.count_words('quotes.txt', word_count_map)
        self.assertEqual(word_count_map['the'], 9)
        self.assertEqual(word_count_map['of'], 6)
        self.assertEqual(word_count_map['and'], 6)
        self.assertEqual(word_count_map['to'], 4)
        WordCountTest.Points += 1

    def test_count_words_list(self):
        word_count_map = ListMap()
        word_count.count_words('fruit.txt', word_count_map)
        self.assertEqual(word_count_map['apple'], 1)
        self.assertEqual(word_count_map['banana'], 2)
        self.assertEqual(word_count_map['cherry'], 3)
        word_count_map = ListMap()
        word_count.count_words('quotes.txt', word_count_map)
        self.assertEqual(word_count_map['the'], 9)
        self.assertEqual(word_count_map['of'], 6)
        self.assertEqual(word_count_map['and'], 6)
        self.assertEqual(word_count_map['to'], 4)
        WordCountTest.Points += 1

    def test_main(self):
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as output:
            sys.argv = ['word_count.py', 'dict', 'fruit.txt']
            word_count.main()
            outstrings = output.getvalue().splitlines()
            self.assertEqual(sorted(outstrings), ['1 apple', '2 banana', '3 cherry'])
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as output:
            sys.argv = ['word_count.py', 'avl', 'fruit.txt']
            word_count.main()
            outstrings = output.getvalue().splitlines()
            self.assertEqual(sorted(outstrings), ['1 apple', '2 banana', '3 cherry'])
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as output:
            sys.argv = ['word_count.py', 'bst', 'fruit.txt']
            word_count.main()
            outstrings = output.getvalue().splitlines()
            self.assertEqual(sorted(outstrings), ['1 apple', '2 banana', '3 cherry'])
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as output:
            sys.argv = ['word_count.py', 'list', 'fruit.txt']
            word_count.main()
            outstrings = output.getvalue().splitlines()
            self.assertEqual(sorted(outstrings), ['1 apple', '2 banana', '3 cherry'])

        WordCountTest.Points += 1

if __name__ == '__main__':
    unittest.main()