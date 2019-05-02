import pygame
import random
from GameObject import GameObject
from Monster import *

class Slime(Monster):

    @staticmethod
    def init():
        image = pygame.image.load("assets/slime.png")
        cellWidth, cellHeight = image.get_size()[0]/7, image.get_size()[1]
        Slime.idleFrame = list()
        for col in range(7):
            subImage = image.subsurface((col * cellWidth, 0, cellWidth, cellHeight))
            Slime.idleFrame.append(subImage)

        image = pygame.image.load("assets/snake_walk.png")
        cellWidth, cellHeight = 34, 38
        Slime.walkFrame = list()
        for col in range(3):
            subImage = image.subsurface((col * cellWidth, 0, cellWidth, cellHeight))
            Slime.walkFrame.append(subImage)

    def __init__(self, x, y, startingInterval):
        self.baseX = x
        self.baseY = y
        startingNote = random.randint(0, 11)
        super(Slime, self).__init__(x, y, startingNote, startingInterval, Slime.idleFrame[0])


class Snake(Monster):

    @staticmethod
    def init():
        image = pygame.image.load("assets/snake_idle.png")
        cellWidth, cellHeight = 41, 39
        Snake.idleFrame = list()
        for col in range(3):
            subImage = image.subsurface((col * cellWidth, 0, cellWidth, cellHeight))
            Snake.idleFrame.append(subImage)

        image = pygame.image.load("assets/snake_walk.png")
        cellWidth, cellHeight = 34, 38
        Snake.walkFrame = list()
        for col in range(3):
            subImage = image.subsurface((col * cellWidth, 0, cellWidth, cellHeight))
            Snake.walkFrame.append(subImage)

    def __init__(self, x, y, startingInterval):
        self.baseX = x
        self.baseY = y
        startingNote = random.randint(0, 11)
        super(Snake, self).__init__(x, y, startingNote, startingInterval, Snake.idleFrame[0])


class Mushroom(Monster):

    @staticmethod
    def init():
        image = pygame.image.load("imgs/mush.png")
        cellWidth, cellHeight = image.get_size()[0]/4, image.get_size()[1]
        Mushroom.idleFrame = list()
        for col in range(4):
            subImage = image.subsurface((col * cellWidth, 0, cellWidth, cellHeight))
            Mushroom.idleFrame.append(subImage)


    def __init__(self, x, y, startingInterval):
        self.baseX = x
        self.baseY = y
        startingNote = random.randint(0, 11)
        super(Mushroom, self).__init__(x, y, startingNote, startingInterval, Mushroom.idleFrame[0])

