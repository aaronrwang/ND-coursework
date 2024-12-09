#Ethan Little elittle2@nd.edu
#Derick Shi dshi2@nd.edu
#Aaron Wang awang27@nd.edu

import argparse
import subprocess
import json
import numpy
import requests
import os
import calendar
import plotdata
import createreport
import datetime

# task 3.2
def filter(data, year, month, interface='eth0'):
    # if all flag (0,0) do not filter by timestamp else do
    if year == 0 and month == 0:
        filteredData=[entry for entry in data if entry['interface']==interface]
    else:
        filteredData=[entry for entry in data if int(entry['timestamp'][:4])==year and int(entry['timestamp'][5:7])==month and entry['interface']==interface]
    return filteredData

# task 3.3 data should be filtered to only have correct interface before passed here
def analyze(data,interface):
    stats={}

    # Task 7 Could any of the stastical functions fail with insufficient data? If no data, no stats to calculate
    if len(data) == 0:
        return stats

    #period
    startDate = data[0]['timestamp'][:7]
    endDate = data[-1]['timestamp'][:7]
    if(startDate==endDate):
        stats["Period"] = startDate
    else:
        stats["Period"] = 'All'

    #interface
    if (interface=='eth0'):
        stats["Interface"] = 'Wired'
    elif (interface=='wlan0'):
        stats["Interface"] = 'Wireless'
    
    #numPoints
    stats["Num Points"] = len(data)

    #throughput stats
    throughputs = [entry['tput_mbps'] for entry in data]
    stats["Min"] = min(throughputs)
    stats["Max"] = max(throughputs)
    stats["Mean"] = numpy.mean(throughputs)
    stats["Median"] = numpy.median(throughputs) 
    stats["Std Dev"] = numpy.std(throughputs)
    stats["10th percentile"] = numpy.percentile(throughputs,10)
    stats["90th percentile"] = numpy.percentile(throughputs,90)
    return stats

def printStats(stats):
    for field, stat in stats.items():
        print(field, end=": ")
        print(stat)

def main(year, month, textFile, url, prepend):
    # Task 7 What happens if the URL does not fetch anything? Valid / good JSON?
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        print("Invalid URL")
        exit(1)

    fileName = prepend + "-{:04d}-{:02d}".format(year, month) #name format for output files
    # Create JSON file from URL
    jsonPath = fileName + ".json"
    with open(jsonPath, 'wb') as fs:
        fs.write(response.content)

    # Filter and sort JSON data into dictionary
    theData = json.loads(open(jsonPath).read()) # load json into list of dicts
    theData=[entry for entry in theData if entry['type']=='iperf' and entry['direction']=='downlink'] # filter data for only downlink and iperf
    theData = sorted(theData, key=lambda x: x['timestamp']) # sort data by time stamp

    numDays = calendar.monthrange(year, month)[1] #get number of days in month
    # Get only Wired data
    wiredFilteredData = filter(theData,year,month,'eth0')
    # Get only Wireless data
    wirelessFilteredData = filter(theData,year,month,'wlan0')
    # task 7 What if the year / month request has no data after filtering?
    if not wiredFilteredData: #check if no data
        print("No data after filtering for Wired Data for", fileName)
    else: 
        stats = analyze(wiredFilteredData,'eth0')
        #create plot
        wiredPlotName = "{}-Wired.png".format(fileName)
        dataDict = plotdata.dailyAvgDict(wiredFilteredData, numDays) #calendar
        plotdata.createGraph(dataDict, wiredPlotName)

        # create document
        createreport.create_word_document(textFile, wiredPlotName, stats, "{}-Wired.docx".format(fileName))
        subprocess.run("rm {}-Wired.png".format(fileName), shell=True) #delete png


    if not wirelessFilteredData: #check if no data
        print("No data after filtering for Wireless Data for", fileName)
    else:
        stats = analyze(wirelessFilteredData,'wlan0')

        #create plot
        wirelessPlotName = "{}-WiFi.png".format(fileName)
        dataDict = plotdata.dailyAvgDict(wirelessFilteredData, numDays)
        plotdata.createGraph(dataDict, wirelessPlotName)

        # create document
        createreport.create_word_document(textFile, wirelessPlotName, stats, "{}-WiFi.docx".format(fileName))
        subprocess.run("rm {}-WiFi.png".format(fileName), shell=True) #delete png

    #cleanup additional files
    subprocess.run(["rm", jsonPath]) #delete JSON

if __name__=="__main__":
    #create args and initialize parser
    parser = argparse.ArgumentParser()
    parser.add_argument('Year', type=int, nargs='?')
    parser.add_argument('Month', type=int, nargs='?')
    parser.add_argument('TextFile', type=str)
    parser.add_argument('JSON_URL', type=str)

    args = parser.parse_args()
    main(args.Year, args.Month, args.TextFile, args.JSON_URL, "RPI01")