# Woofgang's class

import pygame
import os
from GameObject import GameObject

class Woofgang(GameObject):

    @staticmethod
    def init():
        Woofgang.frameNumber = 0
        tempList = sorted(os.listdir("assets/dog_running"))
        Woofgang.runFrame = list()
        for file in tempList:
            Woofgang.runFrame.append(pygame.transform.scale(pygame.image.load("assets/dog_running/%s" % file), (135, 120)))
        
        tempList = sorted(os.listdir("assets/dog_jumping"))
        Woofgang.jumpFrame = list()
        for file in tempList:
            Woofgang.jumpFrame.append(pygame.transform.scale(pygame.image.load("assets/dog_jumping/%s" % file), (135, 120)))

    def __init__(self, x, y):
        super(Woofgang, self).__init__(x, y, Woofgang.runFrame[0])
        self.frames = Woofgang.runFrame
        self.goingRight = True
        self.isFlipped = False

    def update(self, keysDown, screenWidth, screenHeight):
        dx = 0
        if keysDown(pygame.K_RIGHT):
            Woofgang.frameNumber += 1
            dx = 15
            self.goingRight = True

        if keysDown(pygame.K_LEFT):
            Woofgang.frameNumber += 1
            dx -= 15
            self.goingRight = False

        if Woofgang.frameNumber >= len(self.frames):
            Woofgang.frameNumber = 0

        self.image = self.frames[Woofgang.frameNumber]
        if not self.goingRight:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h) 
        super(Woofgang, self).update(screenWidth, screenHeight, dx)



