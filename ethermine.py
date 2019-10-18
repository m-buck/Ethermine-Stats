#!/usr/bin/python
#
# ethermine.py
#
# Pull info from ethermine and send as notification
#
# Import required Python libraries
import time
import datetime
import requests
import json

print "ethermine data fetch (CTRL-C to exit)"

url = "https://api.ethermine.org/miner/a90d5c63849632c24c0ce05e86abccac1025d025/dashboard"
data = requests.get(url).json()
#print data
print "Timestamp: " + str(time.ctime(int(data['data']['currentStatistics']['time']))) 
print "Active workers: " + str(data['data']['currentStatistics']['activeWorkers'])
print "Current Hash Rate: " + str(round(float((data['data']['currentStatistics']['reportedHashrate']))/ 1000000,2)) + " MH/s"
print "1 hour Avg Rate: " + str(round(float((data['data']['currentStatistics']['currentHashrate']))/ 1000000,2)) + " MH/s"
print "Unpaid: " + str(round(float(data['data']['currentStatistics']['unpaid']) / 1000000000000000000,5)) + " ETH"
print "Valid Shares: " + str(data['data']['currentStatistics']['validShares'])
print "Invalid Shares: " + str(data['data']['currentStatistics']['invalidShares'])
print "Stale Shares: " + str(data['data']['currentStatistics']['staleShares'])