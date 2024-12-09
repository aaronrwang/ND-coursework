import unittest
import subprocess
import requests
import os
import json
import processdata


class TestClass (unittest.TestCase):
    JSON_URL="http://ns-mn1.cse.nd.edu/cse20289-fa24/hw03/data-10.json"
    response = requests.get(JSON_URL)
    jsonPath = os.path.basename(JSON_URL)
    with open(jsonPath, 'wb') as fs:
        fs.write(response.content)

    # Filter and sort JSON data into dictionary
    theData = json.loads(open(jsonPath).read()) # load json into list of dicts
    theData = sorted(theData, key=lambda x: x['timestamp']) # sort data by time stamp
    subprocess.run(["rm", jsonPath]) #delete JSON

    def setup(cls):
        self.theData = theData

    def test_filter_date(self):
        self.assertEqual(len(processdata.filter_date(self.theData,'*')),10)
        self.assertEqual(len(processdata.filter_date(self.theData,'2024-05-')),0) # test invalid argument
        self.assertEqual(len(processdata.filter_date(self.theData,'2024-05-29')),1)
        self.assertEqual(len(processdata.filter_date(self.theData,'*-05-29')),1)
        self.assertEqual(len(processdata.filter_date(self.theData,'2024-*-29')),2)
        self.assertEqual(len(processdata.filter_date(self.theData,'2024-05-*')),3)
    
    def test_filter_time(self):
        self.assertEqual(len(processdata.filter_time(self.theData,'*')),10)
        self.assertEqual(len(processdata.filter_time(self.theData,'1')),1)

    def test_filter(self):
        self.assertEqual(len(processdata.filter(self.theData,'*')),10)
        self.assertEqual(len(processdata.filter(self.theData,'direction=uplink')),4)
        self.assertEqual(len(processdata.filter(self.theData,'interface=wlan0')),5)

    def test_stat_count(self):
        self.assertEqual(processdata.stat(self.theData, "count"),10)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'direction=uplink'), "count"),4)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'interface=wlan0'), "count"),5)
    
    def test_stat_mean(self):
        self.assertEqual(processdata.stat(self.theData, "mean")//1,388)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'direction=uplink'), "mean")//1,20)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'interface=wlan0'), "mean")//1,27)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'interface=slkdjfhlskjf'), "mean")//1,0)
    
    def test_stat_median(self):
        self.assertEqual(processdata.stat(self.theData, "median")//1,375)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'direction=uplink'), "median")//1,19)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'interface=wlan0'), "median")//1,20)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'interface=slkdjfhlskjf'), "median")//1,0)

    def test_stat_min(self):
        self.assertEqual(processdata.stat(self.theData, "min")//1,18)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'direction=uplink'), "min")//1,18)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'interface=wlan0'), "min")//1,18)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'interface=slkdjfhlskjf'), "min")//1,0)

    def test_stat_max(self):
        self.assertEqual(processdata.stat(self.theData, "max")//1,794)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'direction=uplink'), "max")//1,23)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'interface=wlan0'), "max")//1,53)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'interface=slkdjfhlskjf'), "max")//1,0)
    
    def test_stat_stdev(self):
        self.assertEqual(processdata.stat(self.theData, "stdev")//1,363)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'direction=uplink'), "stdev")//1,2)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'interface=wlan0'), "stdev")//1,13)
        self.assertEqual(processdata.stat(processdata.filter(self.theData,'interface=slkdjfhlskjf'), "stdev")//1,0)

    def test_stat_list(self):
        gen = None
        count, gen = processdata.stat(self.theData, "list")
        self.assertEqual(count, processdata.stat(self.theData, "count"))
        i = 0
        for j in range(15):
            try:
                if gen:
                    value = next(gen)
                    self.assertEqual(self.theData[i], value)
                    i+=1
                    count -= 1
                    continue
                print("No generator")
            except StopIteration:
                self.assertEqual(count, 0)

if __name__ == "__main__":
    unittest.main()