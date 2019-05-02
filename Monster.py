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
        self.frames = []
        self.notePic = Monster.notePicList[self.startingNote]
        self.notePlayed = False
        

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

    def update(self, player, screenWidth, screenHeight):
        self.dx = 0

        if(abs(self.x - player.x) <= screenWidth//4):
            self.isBattling = True
            self.move(player, screenWidth, screenHeight)

        elif(abs(self.x - player.x) > screenWidth//4):
            self.isBattling = False
            self.notePlayed = False
            #self.x = self.baseX
            self.dx = 0

        if pygame.sprite.collide_rect(self, player):
            player.isAttacked = True
            self.isBattling = False
            #self.x = self.baseX
            self.dx = 0
            player.getsAttacked()

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        super(Monster, self).update(screenWidth, screenHeight, self.dx, 0)

class Bone(GameObject):

    @staticmethod
    def init():
        Bone.boneImage = pygame.image.load("imgs/bone.png")

    def __init__(self, x, y):
        super(Bone, self).__init__(x, y, self.boneImage)
        self.dropped = False

