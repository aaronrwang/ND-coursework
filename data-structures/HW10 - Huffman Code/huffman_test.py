#!/usr/bin/env python3

import io
import unittest
import unittest.mock
import types
import textwrap

import huffman

# Huffman Unit Tests

class HuffmanTest(unittest.TestCase):
    AssignmentTotal = 80
    Total = 7
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

    def test_build_frequency_table(self):
        text = 'abbcccddddeeeee'
        expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(huffman.build_frequency_table(text), expected)

        text = 'eeeeeddddcccbba'
        expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(huffman.build_frequency_table(text), expected)

        text = 'a bb ccc'
        expected = {'a': 1, 'b': 2, 'c': 3, ' ': 2}
        self.assertEqual(huffman.build_frequency_table(text), expected)

        text = textwrap.dedent('''
            a
            bb
            ccc
        ''').strip()
        expected = {'a': 1, 'b': 2, 'c': 3, '\n': 2}
        self.assertEqual(huffman.build_frequency_table(text), expected)

        text = textwrap.dedent('''
            a bb
            ccc dddd
            eeeee ffffff
        ''').strip()
        expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, ' ': 3, '\n': 2}
        HuffmanTest.Points += 1

    def test_huffman_build_tree(self):
        tree = huffman.huffman_build_tree('a')
        self.assertEqual(tree.key, 'a')
        self.assertEqual(tree.value, 1)

        tree = huffman.huffman_build_tree('ab')
        self.assertEqual(tree.key, 'ab')
        self.assertEqual(tree.value, 2)
        self.assertEqual(tree.left.key, 'a')
        self.assertEqual(tree.left.value, 1)
        self.assertEqual(tree.right.key, 'b')
        self.assertEqual(tree.right.value, 1)

        tree = huffman.huffman_build_tree('abbccc')
        self.assertEqual(tree.key, 'cab')
        self.assertEqual(tree.value, 6)
        self.assertEqual(tree.left.key, 'c')
        self.assertEqual(tree.left.value, 3)
        self.assertEqual(tree.right.key, 'ab')
        self.assertEqual(tree.right.value, 3)
        self.assertEqual(tree.right.left.key, 'a')
        self.assertEqual(tree.right.left.value, 1)
        self.assertEqual(tree.right.right.key, 'b')
        self.assertEqual(tree.right.right.value, 2)

        tree = huffman.huffman_build_tree('aabbcccddd')
        self.assertEqual(tree.key, 'abcd')
        self.assertEqual(tree.value, 10)
        self.assertEqual(tree.left.key, 'ab')
        self.assertEqual(tree.left.value, 4)
        self.assertEqual(tree.right.key, 'cd')
        self.assertEqual(tree.right.value, 6)
        self.assertEqual(tree.left.left.key, 'a')
        self.assertEqual(tree.left.left.value, 2)
        self.assertEqual(tree.left.right.key, 'b')
        self.assertEqual(tree.left.right.value, 2)
        self.assertEqual(tree.right.left.key, 'c')
        self.assertEqual(tree.right.left.value, 3)
        self.assertEqual(tree.right.right.key, 'd')
        self.assertEqual(tree.right.right.value, 3)

        tree = huffman.huffman_build_tree('abbcccdddd')
        self.assertEqual(tree.key, 'dcab')
        self.assertEqual(tree.value, 10)
        self.assertEqual(tree.left.key, 'd')
        self.assertEqual(tree.left.value, 4)
        self.assertEqual(tree.right.key, 'cab')
        self.assertEqual(tree.right.value, 6)
        self.assertEqual(tree.right.left.key, 'c')
        self.assertEqual(tree.right.left.value, 3)
        self.assertEqual(tree.right.right.key, 'ab')
        self.assertEqual(tree.right.right.value, 3)
        self.assertEqual(tree.right.right.left.key, 'a')
        self.assertEqual(tree.right.right.left.value, 1)
        self.assertEqual(tree.right.right.right.key, 'b')
        self.assertEqual(tree.right.right.right.value, 2)
        HuffmanTest.Points += 1

    def test_huffman_get_codes(self):
        tree = huffman.Node('ab', 2)
        tree.left = huffman.Node('a', 1)
        tree.right = huffman.Node('b', 1)
        codes = huffman.huffman_get_codes(tree)
        self.assertEqual(codes['a'], '0')
        self.assertEqual(codes['b'], '1')

        tree = huffman.Node('cab', 6)
        tree.left = huffman.Node('c', 3)
        tree.right = huffman.Node('ab', 3)
        tree.right.left = huffman.Node('a', 1)
        tree.right.right = huffman.Node('b', 2)
        codes = huffman.huffman_get_codes(tree)
        self.assertEqual(codes['c'], '0')
        self.assertEqual(codes['a'], '10')
        self.assertEqual(codes['b'], '11')

        tree = huffman.Node('abcd', 10)
        tree.left = huffman.Node('ab', 4)
        tree.right = huffman.Node('cd', 6)
        tree.left.left = huffman.Node('a', 2)
        tree.left.right = huffman.Node('b', 2)
        tree.right.left = huffman.Node('c', 3)
        tree.right.right = huffman.Node('d', 3)
        codes = huffman.huffman_get_codes(tree)
        self.assertEqual(codes['a'], '00')
        self.assertEqual(codes['b'], '01')
        self.assertEqual(codes['c'], '10')
        self.assertEqual(codes['d'], '11')
        HuffmanTest.Points += 1

    def test_huffman_compress(self):
        compressed_string, tree, codes = huffman.huffman_compress('ab')
        self.assertEqual(compressed_string, '01')
        self.assertEqual(tree.key, 'ab')
        self.assertEqual(tree.value, 2)
        self.assertEqual(codes, {'a': '0', 'b': '1'})

        compressed_string, tree, codes = huffman.huffman_compress('abbccc')
        self.assertEqual(compressed_string, '101111000')
        self.assertEqual(tree.key, 'cab')
        self.assertEqual(tree.value, 6)
        self.assertEqual(codes, {'c': '0', 'a': '10', 'b': '11'})

        compressed_string, tree, codes = huffman.huffman_compress('abcd')
        self.assertEqual(compressed_string, '00111001')
        self.assertEqual(tree.key, 'adcb')
        self.assertEqual(tree.value, 4)
        self.assertEqual(codes, {'a': '00', 'd': '01', 'c': '10', 'b': '11'})

        compressed_string, tree, codes = huffman.huffman_compress('aabbcccddd')
        self.assertEqual(compressed_string, '00000101101010111111')
        self.assertEqual(tree.key, 'abcd')
        self.assertEqual(tree.value, 10)
        self.assertEqual(codes, {'a': '00', 'b': '01', 'c': '10', 'd': '11'})
        HuffmanTest.Points += 1

    def test_huffman_decompress(self):
        tree = huffman.Node('ab', 2)
        tree.left = huffman.Node('a', 1)
        tree.right = huffman.Node('b', 1)
        decompressed_string = huffman.huffman_decompress('01', tree)
        self.assertEqual(decompressed_string, 'ab')
        decompressed_string = huffman.huffman_decompress('10', tree)
        self.assertEqual(decompressed_string, 'ba')

        tree = huffman.Node('cab', 6)
        tree.left = huffman.Node('c', 3)
        tree.right = huffman.Node('ab', 3)
        tree.right.left = huffman.Node('a', 1)
        tree.right.right = huffman.Node('b', 2)
        decompressed_string = huffman.huffman_decompress('101111000', tree)
        self.assertEqual(decompressed_string, 'abbccc')
        decompressed_string = huffman.huffman_decompress('01011', tree)
        self.assertEqual(decompressed_string, 'cab')

        compressed_string, tree, codes = huffman.huffman_compress('abcd')
        decompressed_string = huffman.huffman_decompress(compressed_string, tree)
        self.assertEqual(decompressed_string, 'abcd')

        compressed_string, tree, codes = huffman.huffman_compress('aabbcccddd')
        decompressed_string = huffman.huffman_decompress(compressed_string, tree)
        self.assertEqual(decompressed_string, 'aabbcccddd')
        HuffmanTest.Points += 1

    def test_huffman_compression_ratio(self):
        original_string = 'ab'
        compressed_string = '01'
        ratio = huffman.huffman_compression_ratio(original_string, compressed_string)
        self.assertEqual(f'{ratio:.2f}', '8.00')

        original_string = 'abcd'
        compressed_string = '00111011'
        ratio = huffman.huffman_compression_ratio(original_string, compressed_string)
        self.assertEqual(f'{ratio:.2f}', '4.00')

        original_string = 'abbcccdddd'
        compressed_string = '1101111111010100000'
        ratio = huffman.huffman_compression_ratio(original_string, compressed_string)
        self.assertEqual(f'{ratio:.2f}', '4.21')
        HuffmanTest.Points += 1

    def test_main(self):
        input_text = 'ab\n'
        expected_output = textwrap.dedent('''
            Original string:
            ab
            Codes:
            a 0
            b 1
            Compressed string:
            01
            Decompressed string:
            ab
            Compression ratio: 8.00
        ''')
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as output:
            huffman.main(io.StringIO(input_text))
            self.assertEqual(output.getvalue().strip(), expected_output.strip())

        input_text = 'abbccc\n'
        expected_output = textwrap.dedent('''
            Original string:
            abbccc
            Codes:
            c 0
            a 10
            b 11
            Compressed string:
            101111000
            Decompressed string:
            abbccc
            Compression ratio: 5.33
        ''')
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as output:
            huffman.main(io.StringIO(input_text))
            self.assertEqual(output.getvalue().strip(), expected_output.strip())
        
        HuffmanTest.Points += 1

if __name__ == '__main__':
    unittest.main()