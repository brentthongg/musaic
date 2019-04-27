import pygame
import random
from GameObject import GameObject

#startingNote = index into the list

class Monster(GameObject):
    def __init__(self, x, y, startingNote, startingInterval, startFrame):
        super(Monster, self).__init__(x, y, startFrame)
        self.x = x
        self.y = y
        self.startingNote = startingNote
        self.startingInterval = startingInterval
        self.isBattling = False
        self.frames = []
        

    def move(self, player):
        if(self.x < player.x):
            self.x += 10
        else:
            self.x -= 10

    def checkInterval(self, noteSung):
        noteList = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C"]
        if(noteList[(self.startingNote + self.startingInterval)%12] == noteList[noteSung]):
            return True
        return False

    def update(self, player, screenWidth, screenHeight):
        if collide_rect(self, player): 
            player.isAttacked = True
            self.isBattling = True
            self.x = self.baseX
            self.y = self.baseY
        elif(abs(player.x - self.x) <= screenWidth//15):
            move(self, player)
            player.isBattling = True
        else:
            player.isBattling = False
            self.x = self.baseX
            self.y = self.baseY




