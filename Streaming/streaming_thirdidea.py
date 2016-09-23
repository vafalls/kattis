#!/usr/bin/python

# Original idea to sort by start time and end time
# and then use searchalgorithm to find cutoff values.
# After that take all values that can be
# found in both lists and calculate them

import sys
from pprint import pprint
from datetime import datetime
import mylib
import bisect

MAX_ENDTIME = 1326000000000
MIN_STARTTIME = 1325000000000

def scanData():
    nrOfLogEntries = input()
    startTimes = []
    endTimes = []
    logEntries = []
    for i in range(nrOfLogEntries):
        entry = {}
        entry['endTime'], entry['duration'], entry['bitRate'] = [int(i) for i in raw_input().split()]
        if entry['duration']==0:
            continue
        entry['startTime'] = entry['endTime'] - entry['duration']
        startTimes.append(entry['startTime'])
        endTimes.append(entry['endTime'])
        logEntries.append(entry)

    nrOfQueries = input()
    queries = []
    for i in range(nrOfQueries):
        query = {}
        query['startTime'], query['endTime'] = [int(i) for i in raw_input().split()]
        queries.append(query)
    return logEntries, queries,startTimes,endTimes


def calc(query, valuesToBeCalculated):
    intervalTime = 0
    for val in valuesToBeCalculated:
        if val['startTime'] >= query['startTime']:
            startTime = val['startTime']
        else:
            startTime = query['startTime']

        if val['endTime'] <= query['endTime']:
            stopTime = val['endTime']
        else:
            stopTime = query['endTime']

        if startTime < stopTime:
            intervalTime += float(float(val['bitRate']) * float(0.001) * float(stopTime-startTime))
    return intervalTime


def removeEndValues(startTimes, endTime):
    print startTimes, endTime
    print bisect.bisect(startTimes,endTime)
    # for i, entry in enumerate(logEntriesSortedByStart):
    #     if entry['startTime'] > endTime:
    #         return logEntriesSortedByStart[:i]
    # return logEntriesSortedByStart


def removeFirstValues(logEntriesSortedByEnd, startTime):
    for i, entry in reversed(list(enumerate(logEntriesSortedByEnd))):
        if entry['endTime'] < startTime:
            return logEntriesSortedByEnd[i:]
    return logEntriesSortedByEnd




if __name__ == "__main__":
    # logEntries, queries, startTimes, endTimes = scanData()
    logEntries, queries, startTimes, endTimes = mylib.scanTextDataToDict()

    timeA = datetime.now()

    startTimes.sort()
    endTimes.sort(reverse=True)
    logEntriesSortedByEnd = sorted(logEntries, key=lambda k: k['endTime'])
    logEntriesSortedByStart = sorted(logEntries, key=lambda k: k['startTime'])

    for query in queries:

        #---------------------------------------------------
        #          |XXX|                                    |
        #---------------------------------------------------
        if MAX_ENDTIME-query['endTime'] > query['startTime']-MIN_STARTTIME:
            valuesToBeCalculated = logEntriesSortedByStart[0:bisect.bisect_left(startTimes,query['endTime'])]

        #---------------------------------------------------
        #                                    |XXX|          |
        #---------------------------------------------------
        else :
            valuesToBeCalculated = logEntriesSortedByEnd[bisect.bisect_right(endTimes,query['startTime']):]

        result = calc(query, valuesToBeCalculated)

        # print("%.3f"% (result))

    timeB = datetime.now()
    totTime = timeB-timeA
    print totTime.seconds
