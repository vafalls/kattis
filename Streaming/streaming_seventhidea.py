#!/usr/bin/python

import mylib
import bisect
import time
from pprint import pprint

MAX_ENDTIME = 1326000000000
MIN_STARTTIME = 1325000000000

def scanData():
    nrOfLogEntries = input()
    startTimes = []
    endTimes = []
    logEntries = []
    for i in range(nrOfLogEntries):

        endTime, duration, bitRate = [int(i) for i in raw_input().split()]

        if duration==0:
            continue
        startTime = endTime - duration
        entry = (startTime, endTime, duration, bitRate)

        startTimes.append(entry[0])
        endTimes.append(entry[1])
        logEntries.append(entry)

    nrOfQueries = input()
    queries = []
    for i in range(nrOfQueries):
        startTime, endTime = [int(i) for i in raw_input().split()]
        query = (startTime, endTime)
        queries.append(query)
    return logEntries, queries, startTimes, endTimes


def calc(query, valuesToBeCalculated):

    intervalTime = 0
    for val in valuesToBeCalculated:
        if val[0] > query[0]:
            startTime = val[0]
        else:
            startTime = query[0]

        if val[1] < query[1]:
            stopTime = val[1]
        else:
            stopTime = query[1]

        # if startTimes < stopTime:
        intervalTime += val[3] * (stopTime-startTime)

    return intervalTime * 0.001


if __name__ == "__main__":
    logEntries, queries, startTimes, endTimes = scanData()
    # logEntries, queries, startTimes, endTimes = mylib.scanTextDataToTuple()

    # pprint(logEntries)

    timeA = time.time()

    startTimes.sort()
    endTimes.sort()
    logEntriesSortedByEnd = sorted(logEntries, key=lambda k: k[1])
    logEntriesSortedByStart = sorted(logEntries, key=lambda k: (k[0],k[1]))
    pprint(logEntriesSortedByStart)

    for query in queries:

        #---------------------------------------------------
        #           XXX|                                    |
        #---------------------------------------------------
        # if MAX_ENDTIME-query[1] > query[0]-MIN_STARTTIME:
        cutoffA = bisect.bisect_left(startTimes,query[1])
        print "cutoffA",cutoffA

        #---------------------------------------------------
        #                                    |XXX           |
        #---------------------------------------------------
        # else:
        cutoffB = bisect.bisect_right(endTimes,query[0])
        print "cutoffB",cutoffB

        if len(startTimes)-cutoffA > cutoffB:
            valuesToBeCalculated = logEntriesSortedByStart[:cutoffA]
            valuesToBeCalculated = sorted(valuesToBeCalculated, key=lambda k: k[1], reverse=True)
        else:
            valuesToBeCalculated = logEntriesSortedByEnd[cutoffB:]

        valuesToBeCalculated = logEntriesSortedByStart[cutoffB:cutoffA]
        pprint(valuesToBeCalculated)

        # valuesToBeCalculated = list(set(valuesToBeCalculatedA) & set(valuesToBeCalculatedB)) #this is why i should use tuples instead of dicts
        result = calc(query, valuesToBeCalculated)

        print("%.3f"% (result))



    print time.time()-timeA
