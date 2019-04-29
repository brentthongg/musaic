import pygame
import random
from GameObject import GameObject

#startingNote = index into the list

class Monster(GameObject):
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
        

    def move(self, player, screenWidth, screenHeight):
        if(self.x < player.x):
            self.dx = 2
        else:
            self.dx = -2

    def checkInterval(self, noteSung):
        noteList = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C"]
        if noteSung == None: return False
        if(noteList[(self.startingNote + self.startingInterval)%12] == noteList[noteSung]):
            return True
        return False

    def update(self, player, screenWidth, screenHeight):
        self.dx = 0

        if(abs(self.x - player.x) <= screenWidth//4):
            if(self.x < (self.baseX - screenWidth//6) or self.x > (self.baseX + screenWidth//6)):
                self.x = self.baseX
            else:
                player.isBattling = True
                self.isBattling = True
                self.move(player, screenWidth, screenHeight)

        elif(abs(self.x - player.x) > screenWidth//4):
            player.isBattling = False
            self.isBattling = False
            self.x = self.baseX

        if pygame.sprite.collide_rect(self, player):
            player.isAttacked = True
            player.isBattling = False
            self.isBattling = False
            self.x = self.baseX
            self.dx = 0
            player.getsAttacked()

        '''
        if pygame.sprite.collide_rect(self, player): 
            player.isAttacked = True
            player.isBattling = False
            self.isBattling = False
            self.x = self.baseX
            self.y = self.baseY
            self.dx = 0
            player.getsAttacked()
            
        elif(abs(self.x-player.x) <= screenWidth//5):
            #Monster.move(self, player)
            player.isBattling = True
            self.isBattling = True
        else:
            player.isBattling = False
            self.isBattling = False
            self.x = self.baseX
            self.y = self.baseY
            self.dx = 0
        '''

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        super(Monster, self).update(screenWidth, screenHeight, self.dx, 0)
