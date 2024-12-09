# Aaron Wang
# awang27@nd.edu
import os
import subprocess
import re
import argparse
import csv
import statistics

# run searchsrc.py on file and return the output in a dictionary
def searchsrc(path, file):
    fullPath = os.path.join(path, file)
    result = subprocess.run(
        ['python3', 'searchsrc.py', fullPath, '--include', '--includelocal', '--memberfuncs', '--onelinefuncs'],
        stdout=subprocess.PIPE,
        universal_newlines=True)
    dictionaryRegex = re.compile(r'(.*): (.*)')
    mo = dictionaryRegex.findall(result.stdout)
    fileStats = dict(mo)
    return fileStats

# print searchsrc.py data output toggle with --quiet
def printFileData(fileStats):
    print(fileStats['path'], end=', ')
    print(fileStats['file'], end=', ')
    print(fileStats['lines'], end=' LOC, ')
    print(fileStats['include'], end=' I, ')
    print(fileStats['includelocal'], end=' LI, ')
    print(fileStats['memberfuncs'], end=' MF, ')
    print(fileStats['onelinefuncs'], end=' OLF ')
    print()

# scan through directories and get files to call searchsrc.py on; if -r, do subdirectories as well
def scanDirectory(path, quiet=False, r=False):
    result = subprocess.run(['ls',path],stdout=subprocess.PIPE,universal_newlines=True)
    files = result.stdout.splitlines()
    ccRegex = re.compile(r'.cc$')
    filesData = []
    for file in files:
        fullPath = path +'/'+ file
        mo = ccRegex.search(file)
        if mo and os.path.isfile(fullPath): # if its a file and its .cc
            filesData.append(searchsrc(path, file))
            if not quiet: #print output statements if not quiet
                printFileData(filesData[-1])
        elif r and os.path.isdir(fullPath): # search subdirectory and append to current data
            filesData+=scanDirectory(fullPath, quiet, r)
    return filesData
            
# ouputs the data from all the files into a csv
def listToCSV(dataList, fileName):
    outputFile = open(fileName, 'w', newline='')
    outputDictWriter = csv.DictWriter(outputFile, ['path', 'file', 'lines', 'include', 'includelocal', 'memberfuncs', 'onelinefuncs'])
    outputDictWriter.writeheader()
    for data in dataList:
        outputDictWriter.writerow(data)
    outputFile.close()
     
# calculates the stats for task 6: field, max, maxfile, min, minfile, mean, median, stdev and prints
def stats(listData):
    statsList = []  # list of dictionaries of all the statistics
    for field in ['lines', 'include', 'includelocal', 'memberfuncs', 'onelinefuncs']:
        fieldData = list(map(int, [d[field] for d in listData])) # list of all the numbers for one field

        fieldStats = {} # make dictionary to store stats
        fieldStats['field'] = field

        # find max
        maxNum = int(listData[0][field])
        fileName = listData[0]['file']
        for file in listData:
            num = int(file[field])
            if num > maxNum:
                maxNum = num
                fileName = file['file']
        fieldStats['Max'] = maxNum
        fieldStats['MaxFile'] = fileName

        # find min
        minNum = int(listData[0][field])
        fileName = listData[0]['file']
        for file in listData:
            # print(file[field])
            num = int(file[field])
            if num < minNum:
                minNum = num
                fileName = file['file']
        fieldStats['Min'] = minNum
        fieldStats['MinFile'] = fileName
        
        fieldStats['Mean'] = statistics.mean(fieldData) # add mean to dict
        fieldStats['Median'] = statistics.median(fieldData) # add median to dict
        fieldStats['StdDev'] = statistics.stdev(fieldData) # add stdev to dict
        statsList.append(fieldStats) # put dict of this field in list of all
    # print out every field as specified in task 6
    for header in statsList[0]:
        print(header,end='')
        if header != 'StdDev':
            print(',',end = ' ')
    print()
    for stats in statsList:
        for field in stats:
            print(stats[field],end='')
            if field != 'StdDev':
                print(',',end = ' ')
        print(' ')
        
parser = argparse.ArgumentParser()

parser.add_argument('directory', type=str)
parser.add_argument('-r', action="store_true", default=False)
parser.add_argument('--csv', type=str, default=None)
parser.add_argument('--stats', action="store_true", default=False)
parser.add_argument('--quiet', action="store_true", default=False)

args = parser.parse_args()
# check for directory specified covered by argsparse

if not os.path.isdir(args.directory): # check for valid directory
    print(args.directory + ' is not a directory.\nTry again')
    exit(1)
listData = scanDirectory(args.directory, args.quiet, args.r)
if not listData:
    print('No files scanned')
    exit(2)
if args.csv: # check if csv file is specified
    
    if os.path.exists(args.csv): # check if csv already axists
        print('CSV file exists\nTry a new file name')
        exit(3)
    listToCSV(listData, args.csv)
else:
    print('No CSV file inputed')
if args.stats:
    stats(listData)

