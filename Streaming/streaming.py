#!/usr/bin/python

import bisect

MAX_ENDTIME = 1326000000000
MIN_STARTTIME = 1325000000000

def scanData():
    nrOfLogEntries = input()

    allPoints = []
    for i in range(nrOfLogEntries):

        endTime, duration, bitRate = [int(i) for i in raw_input().split()]
        if duration==0:
            continue

        startTime = endTime - duration
        entry = (startTime, True, bitRate)
        allPoints.append(entry)
        entry = (endTime, False, bitRate)
        allPoints.append(entry)

    nrOfQueries = input()
    queries = []
    for i in range(nrOfQueries):
        startTime, endTime = [int(i) for i in raw_input().split()]
        query = (startTime, endTime)
        queries.append(query)
    return allPoints, queries


def calc(query, valuesToBeCalculated):
    time = 0
    i = 1
    length = len(valuesToBeCalculated)

    while i < length:
        bitRate = valuesToBeCalculated[i-1][1]

        startTime = query[0] if query[0] > valuesToBeCalculated[i-1][0] else valuesToBeCalculated[i-1][0]
        stopTime = query[1] if query[1] < valuesToBeCalculated[i][0] else valuesToBeCalculated[i][0]

        time += bitRate * (stopTime-startTime)
        i += 1

    return time * 0.001

def createBetterList(allPoints):
    currentBitRate = 0
    rates = []
    for point in allPoints:

        if point[1]:
            currentBitRate += point[2]
        else:
            currentBitRate -= point[2]

        ratePoint = (point[0], currentBitRate)
        rates.append(ratePoint)
    return rates

if __name__ == "__main__":
    allPoints, queries = scanData()

    allPointsSorted = sorted(allPoints, key=lambda k: k[0])
    betterList = createBetterList(allPointsSorted)

    for query in queries:
        startInd = bisect.bisect_left(betterList,query)-1
        startInd = startInd if startInd > 0 else 0
        endInd = bisect.bisect_right(betterList,(query[1],query[0]))+1

        result = calc(query, betterList[startInd:endInd])
        print("%.3f"% (result))
