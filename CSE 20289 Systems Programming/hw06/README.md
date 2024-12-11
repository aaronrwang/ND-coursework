# Notes about Homework
## Task 3
### Task 3b
In my unit tests, I compared all 5 files to outputs as given by HW1 as follows:

| File Path                           | Lines of Code | Includes | Local Includes | Member Functions | One-Line Functions |
|-------------------------------------|---------------|----------|----------------|------------------|--------------------|
| tests/data/nrd-1/fmnc_manager.cc   | 2310          | 18       | 11             | 77               | 36                 |
| tests/data/nrd-1/ParamDictionary.cc | 379           | 3        | 1              | 26               | 10                 |
| tests/data/nrd-1/PktQueue.cc       | 42            | 1        | 1              | 4                | 4                  |
| tests/data/nrd-1/RIPPS_PktPair.cc  | 607           | 5        | 3              | 50               | 23                 |
| tests/data/nrd-1/Thread_IO.cc      | 149           | 7        | 5              | 0                | 0                  |

### Task 3c

Here, I tested to see if entering valid combos of arguments would give valid answers. For the one with all of them:

```
res = result.stdout.splitlines()
self.assertEqual(res[0], 'path: tests/data/nrd-1')
self.assertEqual(res[1], 'base: fmnc_manager.cc')
self.assertEqual(res[2], 'lines: 2310')
self.assertEqual(res[3], 'include: 18')
self.assertEqual(res[4], 'includelocal: 11')
self.assertEqual(res[5], 'memberfuncs: 77')
self.assertEqual(res[6], 'onelinefuncs: 36')
```

### Task 3d
| Issue                     | Handling Method                    | Testcode|
|---------------------------|------------------------------------|------------------------------------------------------|
| No file is specified      | `argparse` catches error           |`self.assertEqual(result.stderr[:6],'usage:')`        |
| File is not present       | `if not os.path.isfile(args.file)` |`self.assertEqual(result.stdout[-6:],'path.\n')`      |
| File is not a .cc file    | `args.file[-3:] != '.cc'`          |`self.assertEqual(result.stdout[-6:],'path.\n')`      |
| File is a directory       | `if os.path.isdir(args.file)`      |`self.assertEqual(result.stdout[-11:],'directory.\n')`|
| Invalid argument is given | `argparse` catches error           |`self.assertEqual(result.stderr[:6],'usage:')`        |

## Task 4
### Non-recursive
The only part I compared was the files extracted from each directory. This is because the numbers should all be right from my prior testing. To get the expected value I ran ls {directory} and filtered only the .cc files. If these two lists matched, then my function worked.

### Recursive
The only part I compared was the files extracted from each directory. This is because the numbers should all be right from my prior testing. 

### Extra
Did the same as recursive with new test cases (ex-1,ex-2).

### Robustness
| Issue                     | Handling Method                       | Testcode|
|---------------------------|---------------------------------------|------------------------------------------------------|
| No Directory is specified | `argparse` catches error              |`self.assertEqual(result.stderr[:6],'usage:')`        |
| Not a directory           | `if not os.path.isdir(args.directory)`|`self.assertEqual(result.stdout[-11:],'directory.\n')`|
| Invalid argument is given | `argparse` catches error              |`self.assertEqual(result.stderr[:6],'usage:')`        |

## Task 6
|Original|Bug|Line|file|
|--------------|-------------------|-|-|
|`print('onelinefuncs:',count_one_line_funcs(code))`|`print('one linefuncs:',count_one_line_funcs(code))`|115|hw6searchsrc.py|

test_non_recursive (test_hw6searchdir.TestClass) ... FAIL

test_recursive (test_hw6searchdir.TestClass) ... FAIL

test_recursive_extra (test_hw6searchdir.TestClass) ... FAIL

test_all_arguments (test_hw6searchsrc.TestClass) ... FAIL

test_one_line_funcs_arguments (test_hw6searchsrc.TestClass) ... FAIL
