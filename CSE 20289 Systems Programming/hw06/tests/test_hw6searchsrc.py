import unittest
import subprocess
from hw6searchsrc import *

class TestClass (unittest.TestCase):
    file_name = [
            "tests/data/nrd-1/fmnc_manager.cc",
            "tests/data/nrd-1/ParamDictionary.cc",
            "tests/data/nrd-1/PktQueue.cc",
            "tests/data/nrd-1/RIPPS_PktPair.cc",
            "tests/data/nrd-1/Thread_IO.cc"
        ]
    code = [read_file(item) for item in file_name]

# Task 3a -> 3b: see read me

    def setup(cls):
        cls.file_name = file_name
        cls.code = [read_file(item) for item in cls.file_name]   

    def test_lines(self):
        self.assertEqual(count_lines(self.code[0]),2310)
        self.assertEqual(count_lines(self.code[1]),379)
        self.assertEqual(count_lines(self.code[2]),42)
        self.assertEqual(count_lines(self.code[3]),607)
        self.assertEqual(count_lines(self.code[4]),149)
    
    def test_include(self):
        self.assertEqual(count_include(self.code[0]),18)
        self.assertEqual(count_include(self.code[1]),3)
        self.assertEqual(count_include(self.code[2]),1)
        self.assertEqual(count_include(self.code[3]),5)
        self.assertEqual(count_include(self.code[4]),7)
    
    def test_include_local(self):
        self.assertEqual(count_include_local(self.code[0]),11)
        self.assertEqual(count_include_local(self.code[1]),1)
        self.assertEqual(count_include_local(self.code[2]),1)
        self.assertEqual(count_include_local(self.code[3]),3)
        self.assertEqual(count_include_local(self.code[4]),5)
    
    def test_member_functions(self):
        self.assertEqual(count_member_funcs(self.code[0]),77)
        self.assertEqual(count_member_funcs(self.code[1]),26)
        self.assertEqual(count_member_funcs(self.code[2]),4)
        self.assertEqual(count_member_funcs(self.code[3]),50)
        self.assertEqual(count_member_funcs(self.code[4]),0)

    def test_one_line_funcs(self):
        self.assertEqual(count_one_line_funcs(self.code[0]),36)
        self.assertEqual(count_one_line_funcs(self.code[1]),10)
        self.assertEqual(count_one_line_funcs(self.code[2]),4)
        self.assertEqual(count_one_line_funcs(self.code[3]),23)
        self.assertEqual(count_one_line_funcs(self.code[4]),0)

    def test_path_name(self):
        for file in self.file_name:
            self.assertEqual(path_name(file),'tests/data/nrd-1')

    def test_base_name(self):
        self.assertEqual(base_name(self.file_name[0]),'fmnc_manager.cc')
        self.assertEqual(base_name(self.file_name[1]),'ParamDictionary.cc')
        self.assertEqual(base_name(self.file_name[2]),'PktQueue.cc')
        self.assertEqual(base_name(self.file_name[3]),'RIPPS_PktPair.cc')
        self.assertEqual(base_name(self.file_name[4]),'Thread_IO.cc')


# Task 3c: see ReadMe

    def test_minimum_arguments(self):
        result = subprocess.run(['python3', 'hw6searchsrc.py', 'tests/data/nrd-1/fmnc_manager.cc'], stdout=subprocess.PIPE,universal_newlines=True)
        res = result.stdout.splitlines()
        self.assertEqual(res[0], 'path: tests/data/nrd-1')
        self.assertEqual(res[1], 'base: fmnc_manager.cc')

    def test_include_arguments(self):
        result = subprocess.run(['python3', 'hw6searchsrc.py', 'tests/data/nrd-1/fmnc_manager.cc','--include'], stdout=subprocess.PIPE,universal_newlines=True)
        res = result.stdout.splitlines()
        self.assertEqual(res[0], 'path: tests/data/nrd-1')
        self.assertEqual(res[1], 'base: fmnc_manager.cc')
        self.assertEqual(res[2], 'lines: 2310')
        self.assertEqual(res[3], 'include: 18')
    
    def test_include_local_arguments(self):
        result = subprocess.run(['python3', 'hw6searchsrc.py', 'tests/data/nrd-1/fmnc_manager.cc','--includelocal'], stdout=subprocess.PIPE,universal_newlines=True)
        res = result.stdout.splitlines()
        self.assertEqual(res[0], 'path: tests/data/nrd-1')
        self.assertEqual(res[1], 'base: fmnc_manager.cc')
        self.assertEqual(res[2], 'lines: 2310')
        self.assertEqual(res[3], 'includelocal: 11')
    
    def test_member_funcs_arguments(self):
        result = subprocess.run(['python3', 'hw6searchsrc.py', 'tests/data/nrd-1/fmnc_manager.cc','--memberfuncs'], stdout=subprocess.PIPE,universal_newlines=True)
        res = result.stdout.splitlines()
        self.assertEqual(res[0], 'path: tests/data/nrd-1')
        self.assertEqual(res[1], 'base: fmnc_manager.cc')
        self.assertEqual(res[2], 'lines: 2310')
        self.assertEqual(res[3], 'memberfuncs: 77')

    def test_one_line_funcs_arguments(self):
        result = subprocess.run(['python3', 'hw6searchsrc.py', 'tests/data/nrd-1/fmnc_manager.cc','--onelinefuncs'], stdout=subprocess.PIPE,universal_newlines=True)
        res = result.stdout.splitlines()
        self.assertEqual(res[0], 'path: tests/data/nrd-1')
        self.assertEqual(res[1], 'base: fmnc_manager.cc')
        self.assertEqual(res[2], 'lines: 2310')
        self.assertEqual(res[3], 'onelinefuncs: 36')

    
    def test_all_arguments(self):
        result = subprocess.run(['python3', 'hw6searchsrc.py', 'tests/data/nrd-1/fmnc_manager.cc','--include','--includelocal','--memberfuncs','--onelinefuncs'], stdout=subprocess.PIPE,universal_newlines=True)
        res = result.stdout.splitlines()
        self.assertEqual(res[0], 'path: tests/data/nrd-1')
        self.assertEqual(res[1], 'base: fmnc_manager.cc')
        self.assertEqual(res[2], 'lines: 2310')
        self.assertEqual(res[3], 'include: 18')
        self.assertEqual(res[4], 'includelocal: 11')
        self.assertEqual(res[5], 'memberfuncs: 77')
        self.assertEqual(res[6], 'onelinefuncs: 36')

# Task 3d: see ReadMe
    def test_no_file(self):
        result = subprocess.run(['python3', 'hw6searchsrc.py'],universal_newlines=True,stderr=subprocess.PIPE)
        self.assertEqual(result.stderr[:6],'usage:')

    def test_file_not_present(self):
        result = subprocess.run(['python3', 'hw6searchsrc.py', 'tests/data/nrd-1/fmnc.cc'], stdout=subprocess.PIPE,universal_newlines=True)
        self.assertEqual(result.stdout[-6:],'path.\n')
    
    def test_file_invalid(self):
        result = subprocess.run(['python3', 'hw6searchsrc.py', 'tests/data/nrd-1/fmnc_manager'], stdout=subprocess.PIPE,universal_newlines=True)
        self.assertEqual(result.stdout[-5:],'.cc.\n')

    def test_directory(self):
        result = subprocess.run(['python3', 'hw6searchsrc.py', 'tests/data/nrd-1'], stdout=subprocess.PIPE,universal_newlines=True)
        self.assertEqual(result.stdout[-11:],'directory.\n')
    
    def test_invalid_arg(self):
        result = subprocess.run(['python3', 'hw6searchsrc.py','tests/data/nrd-1/fmnc.cc','--skdjlfhalkjsdf'],universal_newlines=True,stderr=subprocess.PIPE)
        self.assertEqual(result.stderr[:6],'usage:')
    

if __name__ == "__main__":
    unittest.main(verbosity=2)