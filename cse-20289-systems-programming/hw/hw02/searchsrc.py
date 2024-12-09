# Aaron Wang
# awang27@nd.edu

import argparse
import re

def readFile (fileName):
    fileRegex = re.compile(r'^(.*\/)([^\/]*)$') # greedy 
    mo = fileRegex.search(fileName)
    print("path: " + mo[1])
    print("file: " + mo[2])

    count = 0
    codeLines = []
    f = open(fileName, "r")
    
    # read file into a list line by line and count lines
    for x in f:
        codeLines.append(x)
        count+=1
    print("lines:",end=" ")
    print(count)
    return codeLines

def countInclude(code):
    count = 0
    includeRegex = re.compile(r'^#include')
    for x in code:
        mo = includeRegex.search(x)
        if(mo): #check if line starts with '#include' and count
            count+=1
    print("include:", end=" ")
    print(count)

def countIncludeLocal(code):
    count = 0
    includeLocalRegex = re.compile(r'^#include\s+\".*\"')
    for x in code:
        mo = includeLocalRegex.search(x)
        if(mo): #check if line starts with '#include "' and count
            count+=1
    print("includelocal:", end=" ")
    print(count)
    
def countMemberFunctions(code):
    count = 0
    memberRegex = re.compile(r'^[a-zA-Z0-9].*::.*') #\w potentially instead???
    for x in code:
        mo = memberRegex.search(x)
        if mo:
            count+=1 #check if line has with '::' and count
    print("memberfuncs:", end=" ")
    print(count)

def countOneLineFuncs(code):
    count = 0
    funcRegex1 = re.compile(r'^[a-zA-Z0-9].*')
    funcRegex2 = re.compile(r'^[a-zA-Z0-9].*{')
    funcRegex3 = re.compile(r'^{')
    funcRegex4 = re.compile(r'^}')
    for i in range(len(code)-2):
        mo1 = funcRegex1.search(code[i])
        if mo1: #check if member function text exists
            mo2 = funcRegex2.search(code[i])
            if mo2: # check case that bracket is on same line
                mo4 = funcRegex4.search(code[i+2])
                if mo4: # check ending
                    count+=1
            mo3 = funcRegex3.search(code[i+1])
            if mo3 and i < len(code)-3: # check case that bracket is on next line make sure no overflow
                mo4 = funcRegex4.search(code[i+3])
                if mo4: # check ending
                    count+=1
    print("onelinefuncs:", end=" ")
    print(count)



# main code

parser = argparse.ArgumentParser()

# add all arguments to parse 
parser.add_argument("file", type=str)
parser.add_argument("--include", action="store_true")
parser.add_argument("--includelocal", action="store_true")
parser.add_argument("--memberfuncs", action="store_true")
parser.add_argument("--onelinefuncs", action="store_true")

args = parser.parse_args()

code = readFile(args.file)
if args.include:
    countInclude(code)
if args.includelocal:
    countIncludeLocal(code)
if args.memberfuncs:
    countMemberFunctions(code)
if args.onelinefuncs:
    countOneLineFuncs(code)

