# Woofgang's class

import pygame
import os
from GameObject import GameObject

class Woofgang(GameObject):

    @staticmethod
    def init():
        Woofgang.frameNumber = 0

        tempList = sorted(os.listdir("assets/dog_idle"))
        Woofgang.idleFrame = list()
        for file in tempList:
            Woofgang.idleFrame.append(pygame.transform.scale(pygame.image.load("assets/dog_idle/%s" % file), (135, 120)))

        tempList = sorted(os.listdir("assets/dog_running"))
        Woofgang.runFrame = list()
        for file in tempList:
            Woofgang.runFrame.append(pygame.transform.scale(pygame.image.load("assets/dog_running/%s" % file), (135, 120)))
        
        tempList = sorted(os.listdir("assets/dog_jumping"))
        Woofgang.jumpFrame = list()
        for file in tempList:
            Woofgang.jumpFrame.append(pygame.transform.scale(pygame.image.load("assets/dog_jumping/%s" % file), (135, 120)))

        tempList = sorted(os.listdir("assets/dog_falling"))
        Woofgang.fallFrame = list()
        for file in tempList:
            Woofgang.fallFrame.append(pygame.transform.scale(pygame.image.load("assets/dog_falling/%s" % file), (135, 120)))

        tempList = sorted(os.listdir("assets/dog_dying"))
        Woofgang.dieFrame = list()
        for file in tempList:
            Woofgang.dieFrame.append(pygame.transform.scale(pygame.image.load("assets/dog_dying/%s" % file), (135, 120)))

        Woofgang.gravity = 2

    def __init__(self, x, y):
        super(Woofgang, self).__init__(x, y, Woofgang.idleFrame[0])
        self.frames = Woofgang.idleFrame
        self.goingRight = True
        self.isFlipped = False
        self.isJumping = False
        self.isRunning = False
        self.isBattling = False
        self.isAttacked = False
        self.health = 100
        self.level = 1
        self.dy = 0
        self.keysHeld = 0


    def update(self, keysDown, screenWidth, screenHeight, delta):
        dx = 0

        if (keysDown(pygame.K_RIGHT) or keysDown(pygame.K_LEFT)) and not self.isRunning:
            self.frames = Woofgang.runFrame
            Woofgang.frameNumber = 0
            self.isRunning = True

        if self.isAttacked:
            self.health -= 10
            self.frames = Woofgang.dieFrame
            Woofgang.frameNumber = 0
            self.isRunning = False
            self.isAttacked = not self.isAttacked

        if(not self.isBattling):
          if (keysDown(pygame.K_RIGHT) or keysDown(pygame.K_LEFT)) and not self.isRunning:
              self.frames = Woofgang.runFrame
              Woofgang.frameNumber = 0
              self.isRunning = True

          elif not (keysDown(pygame.K_RIGHT) or keysDown(pygame.K_LEFT)) and self.isRunning:
              self.frames = Woofgang.idleFrame
              Woofgang.frameNumber = 0
              self.isRunning = False

          if keysDown(pygame.K_RIGHT) and self.isRunning:
              Woofgang.frameNumber += 1
              dx = 15
              self.goingRight = True

          elif keysDown(pygame.K_LEFT) and self.isRunning:
              Woofgang.frameNumber += 1
              dx = -15
              self.goingRight = False

          if keysDown(pygame.K_SPACE) and not self.isJumping:
              self.isJumping = True
              self.frames = Woofgang.jumpFrame
              Woofgang.frameNumber = 0
              self.dy = 15

          elif self.isJumping and self.onGround(600 + (self.h / 2)):
              self.isJumping = False
              self.isRunning = False
              self.frames = Woofgang.idleFrame
              self.dy = 0

          elif self.isJumping:
              Woofgang.frameNumber += 1
              self.dy -= self.gravity
              if self.dy < 0:
                  self.frames = Woofgang.fallFrame
                  Woofgang.frameNumber = 0

          if not self.isRunning and not self.isJumping:
              Woofgang.frameNumber += 1

          if Woofgang.frameNumber >= len(self.frames):
              Woofgang.frameNumber = 0

        self.image = self.frames[Woofgang.frameNumber]
        if not self.goingRight:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h) 
        super(Woofgang, self).update(screenWidth, screenHeight, dx, self.dy)

    def onGround(self, groundY):
        return (self.y + (self.h / 2)) >= groundY

