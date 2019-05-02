# Run this file to play the game

import pygame
from starter import PygameGame
from GameObject import GameObject
from Woofgang import Woofgang
from AllMonsters import *
import pitchCode 
import aubio
import pyaudio
import numpy as np
from Platform import Platform
from levels import *


class Game(PygameGame):

    def initializeNotes(self):
        self.allNotes = []
        for note in ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]:
            self.allNotes.append(pygame.mixer.Sound("monsterNotes/" + note + ".wav"))

    @staticmethod
    def initImages():
        Game.emptyBone = pygame.image.load("imgs/emptyBone.png")
        Game.filledBone = pygame.image.load("imgs/filledBone.png")


    def setWoofgang(self):
        startX = 100
        startY = 584

        Woofgang.init()
        woofgangSprite = Woofgang(startX, startY)
        self.woofgang = pygame.sprite.GroupSingle(woofgangSprite)

        #Level.addMonsters(self.monsters)
    @staticmethod
    def initializeMonsters():
        Monster.init()
        Snake.init()
        Slime.init()
        Bone.init()


    def setMonster(self):
        testMonster1 = Snake(500, 584, 2)
        testMonster2 = Snake(1200, 584, 2)
        testMonster2 = Snake(1500, 584, 2)
        self.monsters = pygame.sprite.Group()
        self.monsters.add(testMonster1)
        self.monsters.add(testMonster2)

    def setLevel(self):
        Platform.Platform.init()
        Game.initializeMonsters()
        self.platGroup = pygame.sprite.Group()
        self.monsterGroup = pygame.sprite.Group()
        if(self.level == 1):
            self.stage = Level(1)
        for row in range(len(self.stage.currMap)):
            for col in range(len(self.stage.currMap[row])):
                if(self.stage.currMap[row][col] == 1): # == 1
                    p = Platform.Platform(row, col, self.width, self.height, self.numRows, self.numCols)
                    self.platGroup.add(p)
                elif(self.stage.currMap[row][col] == "s"):
                    m = Snake(col*(self.width*4)/self.numCols, row*(self.height/self.numRows),2)
                    self.monsterGroup.add(m)
                elif(self.stage.currMap[row][col] == "o"):
                    m = Slime(col*(self.width*4)/self.numCols, row*(self.height/self.numRows), 3)
                    self.monsterGroup.add(m)

    def init(self):
        self.numRows, self.numCols = 12, 64
        self.initializeNotes()
        self.background = pygame.image.load("imgs/backgroundForest.png")
        #self.boneImage =  pygame.image.load("imgs/bone.png")
        Game.setWoofgang(self)
        #Game.setMonster(self)
        self.level = 1
        Game.setLevel(self)
        self.bone = pygame.sprite.Group()
        Game.initImages()
        self.collectBones = [self.emptyBone,self.emptyBone,self.emptyBone]
        self.worldShift = 0

    def moveWorld(self, shiftX):

        self.worldShift += shiftX

        for monster in self.monsterGroup:
            monster.x += shiftX
            monster.rect = pygame.Rect(monster.x, monster.y, monster.w, monster.h)

        for plat in self.platGroup:
            plat.x += shiftX
            plat.rect = pygame.Rect(plat.x, plat.y, plat.w, plat.h)

        for treat in self.bone:
            treat.x += shiftX
            treat.rect.x += shiftX

    def checkWoofMove(self):
        woof = self.woofgang.sprites()[0]

        if woof.x >= 500:
            diff = woof.x - 500
            woof.x = 500
            self.moveWorld(-diff)

        if woof.x <= 90:
            diff = 90 - woof.x
            woof.x = 90
            self.moveWorld(diff)

        currpos = woof.rect.x + self.worldShift
        if currpos < -4000:
            woof.x = 500

    # Keyboard Functions:
    def keyPressed(self, code, mod): pass

    def keyReleased(self, code, mod): pass

    # Mouse Functions:

    def mousePressed(self, x, y): pass

    def mouseReleased(self, x, y): pass

    def mouseMotion(self, x, y): pass

    def mouseDrag(self, x, y): pass

    # Timer Fired:

    def timerFired(self, dt): 
        woof = self.woofgang.sprites()[0]
        woof.update(self.isKeyPressed, self.width, self.height, dt, self.platGroup)
        self.checkWoofMove()
        self.monsterGroup.update(woof, self.width, self.height)
        for monster in self.monsterGroup:
            if(monster.isBattling):
                if not monster.notePlayed:
                    pitchCode.playNote(self.allNotes, monster.startingNote)
                    monster.notePlayed = True
                sungNote = pitchCode.record()
                print(monster.startingNote, sungNote)
                if(monster.checkInterval(sungNote)):
                    monster.kill()
                    self.bone.add(Bone(monster.x, monster.y+50))
                    break
                        
    def redrawAll(self, screen):
        Game.inGameRedrawAll(self, screen)

    @staticmethod
    def inGameRedrawAll(self, screen):
        screen.blit(self.background, (0, 0))
        for monster in self.monsterGroup:
            if(monster.isBattling):
                screen.blit(monster.notePic, (monster.x-20, monster.y-100))

        for i in range(3):
            tempX = 50 + 50*i
            screen.blit(self.collectBones[i], (tempX, 50))

        self.bone.draw(screen)
        self.woofgang.sprites()[0].collideBones(self.bone, self.collectBones,self.filledBone)
        self.woofgang.draw(screen)
        self.monsterGroup.draw(screen)
        self.platGroup.draw(screen)

Game(1024, 832).run()
