#Ethan Little elittle2@nd.edu
#Derick Shi dshi2@nd.edu
#Aaron Wang awang27@nd.edu

import argparse
import matplotlib.pyplot as plt
import numpy as np
import json

# Task 4.3 return dictionary in format {day: dailyAvg, ...} from dataset
def dailyAvgDict(data, numDays):
    dailyDict = {}

    for day in range(1, numDays + 1):
        numEntries = 0
        total = 0
        dailyDict[day] = 0

        for entry in data:
            if int(entry['timestamp'][8:10]) == day: #check the day from data
                numEntries += 1
                total += entry['tput_mbps']
        if numEntries > 0:
            dailyDict[day] = total/numEntries
    
    return dailyDict


# Task 4.4 creates a bar graph as a new file from a dictionary of daily averages
def createGraph(dailyDict, outFileName):
    x = np.arange(1, len(dailyDict) + 1)
    y = list(dailyDict.values())

    # plot data
    fig, ax = plt.subplots()
    ax.grid()
    ax.bar(x, y, label=x)

    plt.xlabel("Day")
    plt.ylabel("Average Throughput (Mb/s)")

    plt.savefig(outFileName)



# task 4.1/4.2/4.5
if __name__ == "__main__": #detect whether or not code is being invoked directly as opposed to imported

    #initilize parser
    parser = argparse.ArgumentParser(description = "Parse through file")
    #add arguments to parser
    parser.add_argument("InputJSON", type=str)
    parser.add_argument("NumDays", type=int)
    parser.add_argument("OutputFile", type=str)

    args = parser.parse_args()

    with open(args.InputJSON, 'r') as file:
        data = json.load(file)

    dataDict = dailyAvgDict(data, args.NumDays)
    createGraph(dataDict, args.OutputFile)