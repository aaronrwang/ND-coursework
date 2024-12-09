# Aaron Wang
# awang27@nd.edu

import argparse

def readFile (fileName):
    print("file: " + fileName, end=" ")
    count = 0
    codeLines = []
    f = open(fileName, "r")

    # read file into a list line by line and count lines
    for x in f:
        codeLines.append(x)
        count+=1
    print("lines:",end=" ")
    print(count,end=" ")
    return codeLines

def countInclude(code):
    count = 0
    for x in code:
        if(x[:8] == '#include'): #check if line starts with '#include' and count
            count+=1
    print("include:", end=" ")
    print(count, end=" ")
    
def countCombo(code):
    count = 0

    for x in code:
        count+=x.count("::") #check if line has with '::' and count
    print("combination:", end=" ")
    print(count, end=" ")

def countPtr(code):
    count = 0
    for x in code:
        count+=x.count("->") #check if line has '->' and count
    print("pointer:", end=" ")
    print(count, end=" ")

def countSimpleFunc(code):
    count = 0
    for i in range(len(code)-2):
        #check first char is '{' and first char two lines down is '}' to find 1-line functions
        if code[i][0] == "{" and code[i+2][0] == "}": 
            count+=1
    print("simplefunc:", end=" ")
    print(count, end=" ")

def countSimpleFuncec(code):
    count = 0
    for i in range(len(code)-2):
        #check if last char is '{' (excluding \n) and first char two lines down is '}' to find 1-line functions
        if code[i][-2:][0] == "{" and code[i+2][0] == "}":
            count+=1
    print("simplefuncec:", end=" ")
    print(count, end=" ")


# main code

parser = argparse.ArgumentParser()

# add all arguments to parse 
parser.add_argument("file", type=str)
parser.add_argument("--include", action="store_true")
parser.add_argument("--member", action="store_true")
parser.add_argument("--ptr", action="store_true")
parser.add_argument("--simplefunc", action="store_true")
parser.add_argument("--simplefuncec", action="store_true")

args = parser.parse_args()

code = readFile(args.file)
if args.include:
    countInclude(code)
if args.member:
    countCombo(code)
if args.ptr:
    countPtr(code)
if args.simplefunc:
    countSimpleFunc(code)
if args.simplefuncec:
    countSimpleFuncec(code)

