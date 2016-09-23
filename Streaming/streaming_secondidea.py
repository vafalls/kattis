#!/usr/bin/python

# Original idea to sort by start time and end time
# and then use searchalgorithm to find cutoff values.
# After that take all values that can be
# found in both lists and calculate them

import sys
from pprint import pprint
from datetime import datetime
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

        if startTime < stopTime:
            intervalTime += float(float(val['bitRate']) / float(1000) * float(stopTime-startTime))
    return intervalTime


def removeEndValues(logEntriesSortedByStart, queryLastEnd):
    for i, entry in reversed(list(enumerate(logEntriesSortedByStart))):
        if entry['startTime'] < queryLastEnd['endTime']:
            return logEntriesSortedByStart[:i+1]
    return logEntriesSortedByStart


def removeFirstValues(logEntriesSortedByEnd, queryFirstStart):
    for i, entry in enumerate(logEntriesSortedByEnd):
        if entry['endTime'] > queryFirstStart:
            return logEntriesSortedByEnd[i:]
    return logEntriesSortedByEnd


if __name__ == "__main__":
    # logEntries, queries = scanData()
    logEntries, queries = mylib.scanTextDataToDict()

    timeA = datetime.now()
    queryFirstStart = min(queries, key=lambda x:x['startTime'])
    queryLastEnd = max(queries, key=lambda x:x['endTime'])

    logEntriesSortedByEnd = sorted(logEntries, key=lambda k: k['endTime'])
    logEntriesSortedByEnd = removeFirstValues(logEntriesSortedByEnd, queryFirstStart)
    logEntriesSortedByStart = sorted(logEntriesSortedByEnd, key=lambda k: k['startTime'])
    logEntries = removeEndValues(logEntriesSortedByStart, queryLastEnd)


    for query in queries:

        valuesToBeCalculated = [x for x in logEntries if not x['endTime'] <= query['startTime'] and not x['startTime'] >= query['endTime'] and not x['duration'] == 0]
        result = calc(query, valuesToBeCalculated)




        # print("%.3f %d"% (result,totTime.microseconds))
        # print("{:<20} {:<30}".format(result,firstTime.microseconds+secondTime.microseconds))

    timeB = datetime.now()
    totTime = timeB-timeA
print totTime.seconds
