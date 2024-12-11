#Ethan Little elittle2@nd.edu
#Derick Shi dhsi2@nd.edu
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

#create args and initialize parser
parser = argparse.ArgumentParser()
parser.add_argument('--all', action='store_true')
parser.add_argument('Year', type=int, nargs='?')
parser.add_argument('Month', type=int, nargs='?')
parser.add_argument('TextFile', type=str)
parser.add_argument('JSON_URL', type=str)

args = parser.parse_args()
url = args.JSON_URL

# Task 7 What happens if the URL does not fetch anything? Valid / good JSON?
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException:
    print("Invalid URL")
    exit(1)

# Create JSON file from URL
jsonPath = os.path.basename(url)
with open(jsonPath, 'wb') as fs:
    fs.write(response.content)

# Filter and sort JSON data into dictionary
theData = json.loads(open(jsonPath).read()) # load json into list of dicts
theData=[entry for entry in theData if entry['type']=='iperf' and entry['direction']=='downlink'] # filter data for only downlink and iperf
theData = sorted(theData, key=lambda x: x['timestamp']) # sort data by time stamp

if args.all:
    dates = [entry["timestamp"][:7] for entry in theData]
    dates = sorted(list(set(dates))) # get all months we need to create plots for
    fileName = "All"
    wiredData = filter(theData,0,0,'eth0')
    stats = analyze(wiredData,'eth0')
    plots = []
    # create plot for each month
    for date in dates:
        year=int(date[:4])
        month=int(date[5:7])
        numDays = calendar.monthrange(year, month)[1]
        wiredFilteredData = filter(wiredData,year,month,'eth0')

        #create plot
        wiredPlotName = "{}-Wired.png".format(date)
        dataDict = plotdata.dailyAvgDict(wiredFilteredData, numDays)
        plotdata.createGraph(dataDict, wiredPlotName)
        plots.append(wiredPlotName)
    # create document
    createreport.create_word_document(args.TextFile, plots, stats, "{}-Wired.docx".format(fileName))

    wirelessData = filter(theData,0,0,'wlan0')
    stats = analyze(wirelessData,'wlan0')
    plots = []
    # create plot for each month
    for date in dates:
        year=int(date[:4])
        month=int(date[5:7])
        numDays = calendar.monthrange(year, month)[1]
        wirelessFilteredData = filter(wirelessData,year,month,'wlan0') # 0 0 for all b/c will never happen otherwise

        #create plot
        wirelessPlotName = "{}-Wireless.png".format(date)
        dataDict = plotdata.dailyAvgDict(wirelessFilteredData, numDays) #calendar
        plotdata.createGraph(dataDict, wirelessPlotName)
        plots.append(wirelessPlotName)
    # create document
    createreport.create_word_document(args.TextFile, plots, stats, "{}-Wireless.docx".format(fileName))

else:
    if args.Year and args.Month:
        numDays = calendar.monthrange(args.Year, args.Month)[1] #get number of days in month
        fileName = "{:04d}-{:02d}".format(args.Year, args.Month) #name format for output files

        # Get only Wired data
        wiredFilteredData = filter(theData,args.Year,args.Month,'eth0')
        # Get only Wireless data
        wirelessFilteredData = filter(theData,args.Year,args.Month,'wlan0')
        # task 7 What if the year / month request has no data after filtering?
        if not wiredFilteredData: #check if no data
            print("No data after filtering for Wired Data")
        else: 
            stats = analyze(wiredFilteredData,'eth0')
            #create plot
            wiredPlotName = "{}-Wired.png".format(fileName)
            dataDict = plotdata.dailyAvgDict(wiredFilteredData, numDays) #calendar
            plotdata.createGraph(dataDict, wiredPlotName)

            # create document
            createreport.create_word_document(args.TextFile, [wiredPlotName], stats, "{}-Wired.docx".format(fileName))


        if not wirelessFilteredData: #check if no data
            print("No data after filtering for Wireless Data")
        else:
            stats = analyze(wirelessFilteredData,'wlan0')

            #create plot
            wirelessPlotName = "{}-WiFi.png".format(fileName)
            dataDict = plotdata.dailyAvgDict(wirelessFilteredData, numDays)
            plotdata.createGraph(dataDict, wirelessPlotName)

            # create document
            createreport.create_word_document(args.TextFile, [wirelessPlotName], stats, "{}-WiFi.docx".format(fileName))
    else:
        print("No time period provided") 

#cleanup additional files
subprocess.run(["rm", jsonPath]) #delete JSON
subprocess.run('rm *.png', shell=True) #delete png