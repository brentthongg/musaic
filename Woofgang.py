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
            if(file != ".DS_Store"):
                Woofgang.idleFrame.append(pygame.transform.scale(pygame.image.load("assets/dog_idle/%s" % file).convert_alpha(), (85, 115)))

        tempList = sorted(os.listdir("assets/dog_running"))
        Woofgang.runFrame = list()
        for file in tempList:
            if(file != ".DS_Store"):
                Woofgang.runFrame.append(pygame.transform.scale(pygame.image.load("assets/dog_running/%s" % file).convert_alpha(), (85, 115)))
        
        tempList = sorted(os.listdir("assets/dog_jumping"))
        Woofgang.jumpFrame = list()
        for file in tempList:
            if(file != ".DS_Store"):
                Woofgang.jumpFrame.append(pygame.transform.scale(pygame.image.load("assets/dog_jumping/%s" % file).convert_alpha(), (85, 115)))

        tempList = sorted(os.listdir("assets/dog_falling"))
        Woofgang.fallFrame = list()
        for file in tempList:
            if(file != ".DS_Store"):
                Woofgang.fallFrame.append(pygame.transform.scale(pygame.image.load("assets/dog_falling/%s" % file).convert_alpha(), (85, 115)))

        tempList = sorted(os.listdir("assets/dog_dying"))
        Woofgang.dieFrame = list()
        for file in tempList:
            if(file != ".DS_Store"):
                Woofgang.dieFrame.append(pygame.transform.scale(pygame.image.load("assets/dog_dying/%s" % file).convert_alpha(), (153, 115)))

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
        self.isDying = False
        self.health = 100
        self.level = 1
        #self.dy = 0
        self.keysHeld = 0
        self.gravity = 1
        self.dx = 0
        self.dy = 0
        self.onPlat = False
        self.currPlat = None
        self.numBones = 0
        self.currBone = 0
        self.isRecording = False
        
    def getsAttacked(self):
        self.health -= 20

    def collideBones(self, bones, collectedBones, filledBone):
        collided = pygame.sprite.spritecollide(self, bones, False)      
        for bone in collided:
            self.numBones += 1
            bone.kill() 
            collectedBones[self.currBone] = filledBone
            self.currBone += 1

    '''

    def collidePlat(self, blocks):
        collided = pygame.sprite.spritecollide(self, blocks, False)
        for plats in collided:
            if self.dy > 0:
                self.onPlat = True
                self.y = plats.rect.top-self.h
                self.dy = 0
                self.isJumping = False
                self.isRunning = False
                self.frames = Woofgang.idleFrame
                self.currPlat = plats
        if self.onPlat and (((self.x < self.currPlat.x) or \
            (self.x+self.w)) > (self.currPlat.x + self.currPlat.w)):
            self.isJumping = True
            self.onPlat = False
    '''
    """  
    def processBlockCollision(self, blocks):
        self.rect.x += self.dx
        hitList = pygame.sprite.spritecollide(self, blocks, False)

        for block in hitList:
            if self.dx > 0:
                self.rect.right = block.rect.left
                self.dx = 0
            elif self.dx < 0:
                self.rect.left = block.rect.right
                self.dx = 0
    """

    def update(self, keysDown, screenWidth, screenHeight, delta, blocks):
        # self.dx = 0

        if (keysDown(pygame.K_RIGHT) or keysDown(pygame.K_LEFT)) and not self.isRunning:
            self.frames = Woofgang.runFrame
            Woofgang.frameNumber = 0
            self.isRunning = True

        if self.health <= 0:
            self.frames = Woofgang.dieFrame
            Woofgang.frameNumber = 0
            self.isAttacked = False
            self.isDying = True

        elif not (keysDown(pygame.K_RIGHT) or keysDown(pygame.K_LEFT)) and self.isRunning:
            self.frames = Woofgang.idleFrame
            Woofgang.frameNumber = 0
            self.isRunning = False

        if keysDown(pygame.K_RIGHT) and self.isRunning:
            Woofgang.frameNumber += 1
            self.dx = 15
            self.goingRight = True
            # self.processBlockCollision(blocks)

        elif keysDown(pygame.K_LEFT) and self.isRunning:
            Woofgang.frameNumber += 1
            self.dx = -15
            self.goingRight = False
            # self.processBlockCollision(blocks)

        if keysDown(pygame.K_SPACE) and not self.isJumping:
            self.isJumping = True
            self.frames = Woofgang.jumpFrame
            Woofgang.frameNumber = 0
            self.dy = -15

        elif self.isJumping and self.onGround(blocks):
            self.isJumping = False
            self.isRunning = False
            self.frames = Woofgang.idleFrame
            self.dy = 0


        elif self.isJumping:
            Woofgang.frameNumber += 1
            self.dy += self.gravity
            if self.dy < 0:
                self.frames = Woofgang.fallFrame
                Woofgang.frameNumber = 0

        elif not(self.onGround(blocks)):
            print('Not on ground')
            Woofgang.frameNumber += 1
            self.dy += self.gravity

        else: self.dy = 0
        
        if keysDown(pygame.K_r):
            self.isRecording = True

        elif not keysDown(pygame.K_r):
            self.isRecording = False


        if not self.isRunning and not self.isJumping:
            Woofgang.frameNumber += 1

        if Woofgang.frameNumber >= len(self.frames):
            if(self.isDying):
                self.isDying = False
                self.frames = Woofgang.idleFrame
                self.dx = -screenWidth//4
            Woofgang.frameNumber = 0

        self.image = self.frames[Woofgang.frameNumber]
        if not self.goingRight:
            self.image = pygame.transform.flip(self.image, True, False)
        # self.rect = pygame.Rect(self.x, self.y, self.w, self.h) 
        if self.y > screenHeight + 100: 
            print(self.y)
            self.health = 0
        # print(self.nextToBlock(blocks, self.dx))
        super(Woofgang, self).update(screenWidth, screenHeight, self.dx, self.dy, blocks)

    def nextToBlock(self, blocks, dx):
        tempX = self.x+dx
        tempy = self.y+self.dy
        for block in blocks:
            if (tempX > block.x) and (tempX + self.w < block.x + block.w):
                if(block.y > tempY) and (block.y + block.h < tempY+ self.h):
                    return True
        return False

    def inBlockBounds(self, platform):
        #print("right", self.x+self.w, "platform right", platform.x+platform.w, "left", self.x, "plat-left", platform.x)
        return (((self.x + self.w) > platform.x) and (self.x < platform.x+platform.w))

    def onGround(self, blocks):
        for platform in blocks:
            if self.inBlockBounds(platform):
                if (self.y + self.h >= platform.y) and (self.y < platform.y):
                    self.rect.bottom = platform.rect.top
                    return True
        return False

