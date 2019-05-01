import pygame
import math

def calculateCoordinates(givenObject, scrollX):
    return (givenObject.x - scrollX)

def isOffScreen(givenObject, scrollX, screenWidth):
    return (((givenObject.x - (givenObject.width / 2)) - scrollX) < 0 or 
            ((givenObject.x + (givenObject.width / 2)) - scrollX) > screenWidth)

def getColFromX(givenObject, gridWidth, screenWidth):
    pass