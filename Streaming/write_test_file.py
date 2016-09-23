#!/usr/bin/python
from random import randint
import sys

MAX_ENDTIME   = 1326000000000
MIN_STARTTIME = 1325000000000
MAX_DURATION =  30000000
NR_ENTRIES = 100000
NR_QUERIES = 1000

if __name__ == "__main__":
    text_file = open("OutputBig.txt", "w")

    text_file.write("%d\n" % NR_ENTRIES)
    for i in range(NR_ENTRIES):
        endTime = randint(MIN_STARTTIME,MAX_ENDTIME)


        duration = randint(0,endTime-MIN_STARTTIME)

        bitRate = randint(64,320)

        text_file.write("%d " % endTime)
        text_file.write("%d " % duration)
        text_file.write("%d\n" % bitRate)

    text_file.write("%d\n" % NR_QUERIES)
    for i in range(NR_QUERIES):
        endTime = randint(MIN_STARTTIME,MAX_ENDTIME)

        startTime = randint(MIN_STARTTIME,endTime)

        text_file.write("%d " % startTime)
        text_file.write("%d\n" % endTime)

    text_file.close()
