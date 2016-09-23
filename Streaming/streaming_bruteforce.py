#!/usr/bin/python

import sys
import pprint
import time
import mylib

def scanData():
    nrOfLogEntries = input()
    logEntries = []
    for i in range(nrOfLogEntries):
        entry = {}
        entry['endTime'], entry['duration'], entry['bitRate'] = [int(i) for i in raw_input().split()]
        entry['startTime'] = entry['endTime'] - entry['duration']
        logEntries.append(entry)

    nrOfQueries = input()
    queries = []
    for i in range(nrOfQueries):
        query = {}
        query['startTime'], query['endTime'] = [int(i) for i in raw_input().split()]
        queries.append(query)
    return logEntries, queries

def calc(query, valuesToBeCalculated):
    intervalTime = 0
    for val in valuesToBeCalculated:
        if val['duration'] == 0:
            continue
        if val['startTime'] >= query['startTime']:
            startTime = val['startTime']
        else:
            startTime = query['startTime']

        if val['endTime'] <= query['endTime']:
            stopTime = val['endTime']
        else:
            stopTime = query['endTime']

            # intervalTime += float(float(val['bitRate']) / float(1000) * float(stopTime-startTime))
        intervalTime += val['bitRate'] * (stopTime-startTime)
    return intervalTime * 0.001


if __name__ == "__main__":
    # logEntries, queries = scanData()
    logEntries, queries, _, _ = mylib.scanTextDataToDict()

    timeA = time.time()

    for query in queries:

        valuesToBeCalculated2 = [x for x in logEntries if not x['endTime'] <= query['startTime'] and not x['startTime'] >= query['endTime'] and not x['duration'] == 0]
        result = calc(query, valuesToBeCalculated2)

        # print("%.3f"% (result))

    print time.time()-timeA
