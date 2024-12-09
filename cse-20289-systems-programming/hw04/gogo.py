import checktests
import yaml
import argparse
import os
import subprocess
import concurrent.futures
from spire.doc import *
from spire.doc.common import *

#converts a dictionary (task) of data entries to a pdf of computed statistics
def dictToPDF(task):
        taskName = list(task.keys())[0]
        taskDict = task[taskName]

        # create and get word docs
        checktests.main(taskDict['Year'], taskDict['Month'], taskDict['StartText'], taskDict['URL'], taskDict['Prepend'])
        fileName = taskDict['Prepend'] + "-{:04d}-{:02d}".format(taskDict['Year'], taskDict['Month'])

        wirelessDoc = Document()
        wiredDoc = Document()
        wirelessDoc.LoadFromFile("{}-WiFi.docx".format(fileName))
        wiredDoc.LoadFromFile("{}-Wired.docx".format(fileName))

        #create PDFs
        wirelessDoc.SaveToFile("{}-WiFi.pdf".format(fileName), FileFormat.PDF)
        wiredDoc.SaveToFile("{}-Wired.pdf".format(fileName), FileFormat.PDF)

        #cleanup word docs
        wirelessDoc.Close()
        wiredDoc.Close()
        subprocess.run("rm {}-WiFi.docx".format(fileName), shell=True)
        subprocess.run("rm {}-Wired.docx".format(fileName), shell=True)

        print("Task", taskName, "Done!")

parser = argparse.ArgumentParser()
parser.add_argument('File', type=str, nargs='?')
parser.add_argument("--multi", type=int, required=False)
args = parser.parse_args()

#check for invalid multi argument
if args.multi and (args.multi > 4 or args.multi < 1):
    print("Error:", args.multi, "must be a value 1-4")
    exit(1)

#check for invalid file argument
if not os.path.isfile(args.File):
    print("Error:", args.File, "is not found")
    exit(1)

# Catch error where file isn't yaml
if args.File[-5:] != ".yaml":
    print("Error:", args.File, "is not a yaml")
    exit(2)

with open(args.File, 'r') as file: 
    data = yaml.safe_load(file)

# check for proper formatting
if 'tasks' not in data:
    print(args.File, "had the wrong format.")
    exit(3)

data = data['tasks'] 

# check for all necessary arguments for each instruction
for item in data:
    taskName = list(item.keys())[0]
    task = item[taskName]
    if not taskName[:4] == 'task' or 'URL' not in task or 'Year' not in task or 'Month' not in task or 'StartText' not in task or 'Prepend' not in task:
        print(args.File, "is missing data.")
        exit(4)
    if type(task['Month']) is not int or type(task['Year']) is not int:
        print(args.File, "has improper dates.")
        exit(5)

if not args.multi:
    #run PDF creation sequentially
    for task in data:
        dictToPDF(task)

    print("Completed", str(len(data)), "task(s)!")
else:
    #run PDF creation in parallel
    with concurrent.futures.ProcessPoolExecutor(args.multi) as executor:
         executor.map(dictToPDF, data)

    print("Completed", str(len(data)), "task(s)!")