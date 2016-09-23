#!/usr/bin/python

import bisect

def scanTextDataToDict():
    f = open('Output.txt', 'r')
    nrOfLogEntries = int(f.readline())
    logEntries = []
    startTimes = []
    endTimes = []
    for i in range(nrOfLogEntries):
        entry = {}
        entry['endTime'], entry['duration'], entry['bitRate'] = [int(i) for i in f.readline().split()]
        if entry['duration']==0:
            continue
        entry['startTime'] = entry['endTime'] - entry['duration']
        startTimes.append(entry['startTime'])
        endTimes.append(entry['endTime'])
        logEntries.append(entry)

    nrOfQueries = int(f.readline())
    queries = []
    for i in range(nrOfQueries):
        query = {}
        query['startTime'], query['endTime'] = [int(i) for i in f.readline().split()]
        queries.append(query)
    f.close()
    return logEntries, queries, startTimes, endTimes

def scanTextDataToTuple():
    f = open('Output.txt', 'r')
    nrOfLogEntries = int(f.readline())
    logEntries = []
    startTimes = []
    endTimes = []
    for i in range(nrOfLogEntries):
        endTime, duration, bitRate = [int(i) for i in f.readline().split()]
        if duration==0:
            continue
        startTime = endTime - duration
        entry = (startTime, endTime, duration, bitRate)

        startTimes.append(entry[0])
        endTimes.append(entry[1])
        logEntries.append(entry)

    nrOfQueries = int(f.readline())
    queries = []
    for i in range(nrOfQueries):
        startTime, endTime = [int(i) for i in f.readline().split()]
        query = (startTime, endTime)
        queries.append(query)
    f.close()
    return logEntries, queries, startTimes, endTimes

def scanTextDataNewWay():
    f = open('OutputBig.txt', 'r')
    nrOfLogEntries = int(f.readline())

    allPoints = []
    for i in range(nrOfLogEntries):

        endTime, duration, bitRate = [int(i) for i in f.readline().split()]
        if duration==0:
            continue

        startTime = endTime - duration
        entry = (startTime, True, bitRate)
        allPoints.append(entry)
        entry = (endTime, False, bitRate)
        allPoints.append(entry)

    nrOfQueries = int(f.readline())
    queries = []
    for i in range(nrOfQueries):
        startTime, endTime = [int(i) for i in f.readline().split()]
        query = (startTime, endTime)
        queries.append(query)
    return allPoints, queries