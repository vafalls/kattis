#!/usr/bin/python

movementDirection = dict(horizontal=True, vertical=True)

class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printTown():
    for index,a in enumerate(town):
        if a['printcolor']:
            print BColors.HEADER + str(a['val']) + BColors.ENDC,
        else:
            print a['val'],
        if (index+1) % size[0] == 0:
            print


def printresults(ultimateLocationList):
    for index, value in enumerate(ultimateLocationList):
        print value,
        if (index+1) % size[0] == 0:
            print


def brute_force_it():
    ultimateLocationList = []
    for restaurantLocation in town:
        dist = 0
        for customerLocation in town:
            if customerLocation.get('val') != 0:
                verticalDiff = customerLocation.get('y') - restaurantLocation.get('y')
                horizontalDiff = customerLocation.get('x') - restaurantLocation.get('x')
                dist += customerLocation.get('val') * (abs(horizontalDiff) + abs(verticalDiff))

        ultimateLocationList.append(dist)
    printresults(ultimateLocationList)


def get_position_value(restaurantLocation):
    dist = 0
    for customerLocation in town:
        if customerLocation.get('val') != 0:
            verticalDiff = customerLocation.get('y') - restaurantLocation.get('y')
            horizontalDiff = customerLocation.get('x') - restaurantLocation.get('x')
            dist += customerLocation.get('val') * (abs(horizontalDiff) + abs(verticalDiff))
    return dist


def check_and_step(stepsToTake, dimension, parallelWithAxis):
    global currentPosition
    if 0 <= currentPosition.get('indexInTown')+stepsToTake < len(town)\
            and\
                    town[currentPosition.get('indexInTown')+stepsToTake].get(parallelWithAxis) ==\
                    town[currentPosition.get('indexInTown')].get(parallelWithAxis):

        nextValue = get_position_value(town[currentPosition.get('indexInTown')+stepsToTake])

        if nextValue < currentPosition.get('currentDistance'):
            currentPosition['indexInTown'] += stepsToTake
            currentPosition['currentDistance'] = nextValue
            town[currentPosition['indexInTown']]['printcolor'] = True
            movementDirection[dimension] = False
            return False
        else:
            return True

    else:
        return True

def printIndexes():
    for a,b in enumerate(town):
        print a,
        if (a+1) % size[0] == 0:
            print

if __name__ == "__main__":
    nrOfTestCases = input()

    for i in range(nrOfTestCases):
        size = map(int, raw_input().split())
        town = []
        for a in range(size[1]):
            row = map(int, raw_input().split())
            for ind, val in enumerate(row):
                oneValue = dict(val=val, y=a, x=ind, printcolor=False)
                town.append(oneValue)

        if size[1] % 2 == 0:
            startIndex = len(town)/2 + size[0]/2
            # print "Startindex: " + str(startIndex)
        else:
            startIndex = len(town)/2
            # print "startindex: " + str(startIndex)
        currentPosition = dict(indexInTown=startIndex, currentDistance=get_position_value(town[startIndex]))
        town[currentPosition['indexInTown']]['printcolor'] = True

        triedHorizontal, triedVertical = False, False

        while not triedHorizontal:
            triedHorizontal = check_and_step(-1, 'horizontal', 'y')
        if movementDirection.get('horizontal'):
            while not check_and_step(1, 'horizontal', 'y'):
                pass

        while not triedVertical:
            triedVertical = check_and_step(-size[0], 'vertical', 'x')
        if movementDirection.get('vertical'):
            while not check_and_step(size[0], 'vertical', 'x'):
                pass

        print str(get_position_value(town[currentPosition.get('indexInTown')])) + " blocks"
        # printTown()
        # brute_force_it()
        # printIndexes()








