import random
import Platform

class Level(object):

    def __init__(self, level):
	    self.rows = 12
	    self.cols = 64
	    if level == 1:
	        self.generateLevelOne()
	    else:
	        self.generateLevelOne()

    def createMap(self):
        tempMap = [[0] * self.cols for i in range(self.rows)]
        return tempMap

    def generateFloor(newMap):
        for i in range(1, 3):
            newMap[-1 * i] = [1] * len(newMap[0])

    def generateLevelOne(self):
        #Create empty map and floor
        self.currMap = self.createMap()
        Level.generateFloor(self.currMap)
        self.currMap[9][12:17] = [1, 1, 1, 1, 1]