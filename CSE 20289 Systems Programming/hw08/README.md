# Group
| **Name** | **Email** |
| --- | --- |
| Aaron Wang | awang27@nd.edu |
| Derick Shi | dshi2@nd.edu |
| Ethan Little | elittle2@nd.edu |

# Task 2a
We created 3 archive directories each representing a different test case
| **File** | **Usage** |
| --- | --- |
|bad_archives | Directory containing only bad archives (although there may be some clean files) |
|clean_archives | Directory containing only clean archives with all clean files |
|mixed_archives | Directory containing some bad archives and some clean archives |

Each directory has a corresponding shell script that copies it to the toscan directory, which is passed as an argument
feeddirectory.sh is a shell script called in each of the 3 corresponding scripts to help facilitate copying

Note: test scripts must be ran from the hw08 repo

# Task 2b
For the loop forever part this was our interpretation:
- Try to extract file: if not extractable move the archive to quarantine with reason file
- If extract, look through each file of the extraction and determine quarantine or not file (ignoring macos files)
- Note: cannot have file in hw08 directory with the same name as the temp file "temp"

# Extra Credit
- Run python scanserver.py to create a web server that returns the log entry for any given archive post in the form of a web response
- The web server must have scanner.sh is running in the background to function since that would make the most sense for an email scanning system
- Test the endpoint by posting to the server: (change "11" to you student machine and toscan and log to their appropriate paths)

```
% curl -X POST "http://student11.cse.nd.edu/scanner?toscan=./scandata/toscan&log=./scandata/log" \
    -F "file=@test/bad_archives/badsite.zip"
```

- Note: since the scanner and web server are running asynchronously, we ran into the issue of the server checking the log before the scanner has updated the log; our solution was to add a 3 second delay in the server

