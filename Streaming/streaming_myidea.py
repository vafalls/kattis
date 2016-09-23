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

def removeLaterPart(entriesByStart, endTime):
    low, mid = 0, 0
    high = len(entriesByStart) - 1

    if entriesByStart[high]['startTime'] < endTime:
        return entriesByStart
    elif entriesByStart[low]['startTime'] >= endTime:
        print "0.000"
        sys.exit()

    while high-low > 1:
        mid = low + (high-low)/2

        if high-low == 1 or high-low == 2:
            if entriesByStart[mid]['startTime'] >= endTime and entriesByStart[mid+1]['startTime'] > endTime:
                return entriesByStart[0 : mid - 1]

            if entriesByStart[mid+1]['startTime'] >= endTime and mid+2 < len(entriesByStart)-1 and entriesByStart[mid+2]['startTime'] > endTime:
                return entriesByStart[0:mid]

        if endTime < entriesByStart[mid]['startTime']:
            high = mid
        elif endTime > entriesByStart[mid]['startTime']:
            low = mid
        else:
            high = high - 1
    return entriesByStart

def removeEarlierPart(entriesByEnd, startTime):
    low, mid = 0, 0
    high = len(entriesByEnd) - 1

    if entriesByEnd[low]['endTime'] > startTime:
        return entriesByEnd
    elif entriesByEnd[high]['endTime'] <= startTime:
        print "0.000"
        sys.exit()

    while high-low > 1:
        mid = low + (high-low)/2

        if high-low == 1 or high-low == 2:
            if entriesByEnd[mid]['endTime'] <= startTime and entriesByEnd[mid+1]['endTime'] > startTime:
                return entriesByEnd[mid+1:]

            if entriesByEnd[mid+1]['endTime'] <= startTime and mid+2 < len(entriesByEnd)-1 and entriesByEnd[mid+2]['endTime'] > startTime:
                return entriesByEnd[mid+2:]

        if startTime < entriesByEnd[mid]['endTime']:
            high = mid
        elif startTime > entriesByEnd[mid]['endTime']:
            low = mid
        else:
            high = high - 1
    return entriesByEnd


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





if __name__ == "__main__":
    # logEntries, queries = scanData()
    logEntries, queries = mylib.scanTextDataToDict()

    timeA = datetime.now()
    logEntriesSortedByEnd = sorted(logEntries, key=lambda k: k['endTime'])
    logEntriesSortedByStart = sorted(logEntries, key=lambda k: k['startTime'])

    for query in queries:
        logEntriesEarlier = removeLaterPart(logEntriesSortedByStart, query['endTime'])
        logEntriesLater = removeEarlierPart(logEntriesSortedByEnd, query['startTime'])
        valuesToBeCalculated = [x for x in logEntriesEarlier if x in logEntriesLater]
        result = calc(query, valuesToBeCalculated)

        # print("%.3f %d"% (result,totTime.microseconds))
        # print("{:<20} {:<30}".format(result,firstTime.microseconds+secondTime.microseconds))

    timeB = datetime.now()
    totTime = timeB-timeA
    print totTime.seconds
