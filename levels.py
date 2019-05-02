import random
import Platform

class Level(object):

    def __init__(self, level):
        self.rows = 12
        self.cols = 64
        #self.currMap = []
        if(level == 1):
            self.currMap = self.readFromString(self.readFile("levels/level1"))
        elif(level == 2):
            self.currMap = self.readFromString(self.readFile("levels/level2"))
        elif(level == 3):
            self.currMap = self.readFromString(self.readFile("levels/level3"))

    def readFile(self, path):
        with open(path, "rt") as f:
            return f.read()

    def readFromString(self, board):
        board = board[1:-1]
        tempBoard = []
        for char in board:
            if(char == "["):
                tempList = []
            if(char == "0" or char == "1"):
                tempList.append(int(char))
            elif(ord(char) >= 97 and ord(char) <= 122):
                tempList.append(char)
            if(char == "]"):
                tempBoard.append(tempList)
        return tempBoard

    def createMap(self):
        tempMap = [[0] * self.cols for i in range(self.rows)]
        return tempMap

    def generateFloor(newMap):
        for i in range(1, 3):
            newMap[-1 * i] = [1] * len(newMap[0])

    #def generateLevelOne(self):
        #self.currMap = self.readFromString(self.readFile("levels/level1"))






