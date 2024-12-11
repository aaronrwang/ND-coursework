import time
import zmq
import argparse
import requests
import os
import json
import subprocess
import processdata

'''
For testing
URL="http://ns-mn1.cse.nd.edu/cse20289-fa24/hw03/data-all.json"
PORT_NUM="40931"
'''

parser = argparse.ArgumentParser()
parser.add_argument('URL', type=str)
parser.add_argument('PORT_NUM', type=int)


args = parser.parse_args()
url = args.URL

# What happens if the URL does not fetch anything? Valid / good JSON?
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

# Don't know if sorting is necessary
theData = sorted(theData, key=lambda x: x['timestamp']) # sort data by time stamp
subprocess.run(["rm", jsonPath]) #delete JSON

# Pick 40000 + last three digits of your 900 ID
serverPort = args.PORT_NUM

context = zmq.Context()
socket = context.socket(zmq.REP)

try: 
    print('Starting up server on port ' + str(serverPort))
    socket.bind("tcp://*:" + str(serverPort))
except:
    print('Failed to bind on port ' + str(serverPort))
    exit()

list_gen = None
list_count = 0

try:
    while True:
        #  Wait for next request from client
        print('Waiting for a new command')
        message = socket.recv()
        message = message.decode('utf-8') #decode to string
        print(f"RCVD: {message}")
        
        #turn message into list of filters
        data_filters = message.split(',')
        data_filters = [item.strip() for item in data_filters]

        # deal with more
        if (len(data_filters) == 1 and data_filters[0] == 'more'):
            try:
                if list_gen:
                    data = next(list_gen)

                    msg = [] #list of key, value pairs in data
                    for key in data:
                        msg.append(key)
                        msg.append(str(data[key]))

                    msg = ", ".join(msg)
                    list_count -= 1
                    result = f"{list_count}, {msg}"
                    print(f"SENT: {result}")
                    socket.send_string(result)
                    continue
                result = f"failure, no more data to send"
                print(f"SENT: {result}")
                socket.send_string(result)
            except StopIteration:
                result = f"failure, no more data to send"
                print(f"SENT: {result}")
                socket.send_string(result)
            continue

        #check for valid number of filters
        if len(data_filters) != 4:
            print("Error: invalid number of filters")
            result = f"failure, invalid number of filters"
            print(f"SENT: {result}")
            socket.send_string(result)
            continue

        stat = data_filters[0]
        date = data_filters[1]
        time = data_filters[2]
        filters = data_filters[3]

        #check for valid command
        if stat not in ["count", "list", "mean", "median", "min", "max", "stddev"]:
            print(f"Error: invalid command {stat}")
            result = f"failure, invalid command {stat}"
            print(f"SENT: {result}")
            socket.send_string(result)
            continue

        #filter data before doing stat calculation
        filtered_data = processdata.filter_date(theData, date)
        filtered_data = processdata.filter_time(filtered_data, time)
        filtered_data = processdata.filter(filtered_data, filters)
        
        #  Send reply back to client
        result = processdata.stat(filtered_data, stat)

        if stat == 'list':
            list_count, list_gen = result
            result = f"success, {list_count}"
        else:
            # get rid of previous generator
            list_gen = None
            list_count = 0  
            
            # format response
            result = f"success, {stat}, {result}"
        
        print(f"SENT: {result}")
        socket.send_string(result)
except KeyboardInterrupt:
    print("\nKeyboardInterrupt: Terminating server")
finally:
    print("Cleaning up...")
    socket.close()
    context.term()
    print("Server shut down")