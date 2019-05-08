import pygame
import random
from GameObject import GameObject
import pitchCode

#startingNote = index into the list

class Monster(GameObject):

    @staticmethod
    def init():
        image = pygame.image.load("imgs/notes.png")
        rows, cols = 3, 4
        width, height = image.get_size()
        cellWidth, cellHeight = width / cols, height / rows
        Monster.notePicList = []
        for row in range(rows):
            for col in range(cols):
                subImage = image.subsurface(
                    (col * cellWidth, row * cellHeight, cellWidth, cellHeight))
                Monster.notePicList.append(subImage)
        Monster.boneImage = pygame.image.load("imgs/bone.png")

    def __init__(self, x, y, startingNote, startingInterval, startFrame):
        super(Monster, self).__init__(x, y, startFrame)
        self.x = x
        self.y = y
        self.dx, self.dy = 0, 0
        self.baseX = x
        self.baseY = y
        self.startingNote = startingNote
        self.startingInterval = startingInterval
        self.isBattling = False
        self.frames = self.idleFrame
        self.frameNumber = 0
        self.notePic = Monster.notePicList[self.startingNote]
        self.notePlayed = False
        self.health = 100
        self.timer = 0
        self.coolDown = 0

    def move(self, player, screenWidth, screenHeight):
        if(self.x < player.x):
            self.dx = 2
        else:
            self.dx = -2

    def checkInterval(self, noteSung):
        noteList = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C"]
        if noteSung == None: return False
        elif pitchCode.checkInterval(self.startingInterval, self.startingNote, noteSung):
            return True
        return False

    def update(self, player, screenWidth, screenHeight, dt, blocks):
        self.coolDown -= dt
        self.dx = 0

        if(abs(self.x - player.x) <= screenWidth//4):
            self.isBattling = True
            self.move(player, screenWidth, screenHeight)

        elif(abs(self.x - player.x) > screenWidth//4):
            self.isBattling = False
            self.notePlayed = False
            self.dx = 0

        hitList = pygame.sprite.spritecollide(self, blocks, False)

        for plat in hitList:
            isOnTop = onTop(self, plat)
            if not(isOnTop):
                if self.dx > 0:
                    self.rect.right = plat.rect.left
                    self.dx = 0
                elif self.dx < 0:
                    self.rect.left = plat.rect.right
                    self.dx = 0
            elif(isOnTop):
                if(self.rect.left < plat.rect.left) or (self.rect.right > plat.rect.right):
                    self.dx = 0



        if pygame.sprite.collide_rect(self, player) and self.coolDown < 0:
            player.isAttacked = True
            self.isBattling = False
            self.dx = 0
            self.coolDown = 2000
            player.getsAttacked()
        self.frameNumber += 1
        self.image = self.frames[self.frameNumber % len(self.frames)]
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        super(Monster, self).update(screenWidth, screenHeight, self.dx, 0, blocks)

def onTop(self, block):
    return self.rect.bottom <= block.rect.top

def onGround(self):
    return self.rect.bottom == 600

class Bone(GameObject):

    @staticmethod
    def init():
        Bone.boneImage = pygame.image.load("imgs/bone.png")

    def __init__(self, x, y):
        super(Bone, self).__init__(x, y, self.boneImage)
        self.dropped = False

