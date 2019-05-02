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
import random
from levelScreen import *
from story import *
from mainMenu import *


class Game(PygameGame,mainMenu,levelScreen,story):

    def initializeNotes(self):
        self.allNotes = []
        for note in ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]:
            self.allNotes.append(pygame.mixer.Sound("monsterNotes/" + note + ".wav"))

    @staticmethod
    def initImages():
        Game.emptyBone = pygame.image.load("imgs/emptyBone.png")
        Game.filledBone = pygame.image.load("imgs/filledBone.png")
        Game.emptyNote = pygame.image.load("imgs/emptyNote.png")


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
        Mushroom.init()


    def setMonster(self):
        testMonster1 = Snake(500, 584, 2)
        testMonster2 = Snake(1200, 584, 2)
        testMonster3 = Snake(1500, 584, 2)
        self.monsters = pygame.sprite.Group()
        self.monsters.add(testMonster1)
        self.monsters.add(testMonster2)

    def setLevel(self):
        Platform.Platform.init()
        Game.initializeMonsters()
        self.platGroup = pygame.sprite.Group()
        self.monsterGroup = pygame.sprite.Group()
        self.stage = Level(self.level)

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
                elif(self.stage.currMap[row][col] == "m"):
                    m = Mushroom(col*(self.width*4)/self.numCols, row*(self.height/self.numRows), 4)
                    self.monsterGroup.add(m)

    def init(self, level = 1):
        self.numRows, self.numCols = 12, 64
        self.initializeNotes()
        self.background = pygame.image.load("imgs/backgroundForest.png")
        #self.boneImage =  pygame.image.load("imgs/bone.png")
        Game.setWoofgang(self)
        #Game.setMonster(self)
        self.level = level
        Game.setLevel(self)
        self.bone = pygame.sprite.Group()
        Game.initImages()
        self.collectBones = [self.emptyBone,self.emptyBone,self.emptyBone]
        self.worldShift = 0
        self.nav = ["mainMenu","story","inGame"]
        self.navCurr = 0
        self.story = story()
        story.story_init(self)
        self.mainMenu = mainMenu()
        mainMenu.mainMenu_init(self)
        self.timer = 0
        self.sungNote = None

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
    def keyPressed(self, code, mod): 
    	currScreen = self.nav[self.navCurr]
    	if (currScreen == "story"): 
            story.story_keyPressed(self,code,mod)
            if (story.story_finished(self)): 
                self.navCurr+=1

    def keyReleased(self, code, mod): pass

    # Mouse Functions:

    def mousePressed(self, x, y):
        currScreen = self.nav[self.navCurr]
        if (currScreen == "mainMenu"): 
            mainMenu.mainMenu_mousePressed(self,x,y)
            if (mainMenu.getStartPressed): self.navCurr+=1

    def mouseReleased(self, x, y): pass

    def mouseMotion(self, x, y): pass

    def mouseDrag(self, x, y): pass

    # Timer Fired:
    def timerFired(self, dt): 
        self.sungNote = None
        self.timer += 1
        woof = self.woofgang.sprites()[0]
        woof.update(self.isKeyPressed, self.width, self.height, dt, self.platGroup)
        self.checkWoofMove()
        if self.timer % 2 == 0:
            self.monsterGroup.update(woof, self.width, self.height, dt)
        if(woof.isRecording):
            self.sungNote = pitchCode.record()
            print(self.sungNote)
        for monster in self.monsterGroup:
            if(monster.isBattling):
                if not monster.notePlayed:
                    pitchCode.playNote(self.allNotes, monster.startingNote)
                    monster.notePlayed = True
                if(monster.checkInterval(self.sungNote)):
                    monster.health -= 10
                    if monster.health <= 0:
                        monster.kill()
                        #if random.randint(1, 100) < 35:
                        self.bone.add(Bone(monster.x, monster.y+10))
                    break
        if woof.health <= 0:
            self.init(self.level)

        if woof.numBones == 3:
            self.level += 1
            self.init(self.level)
                        
    def redrawAll(self, screen):
        currScreen = self.nav[self.navCurr]
        if (currScreen == "mainMenu"): 
            mainMenu.mainMenu_redrawAll(self,screen)
        elif (currScreen == "story"): 
            story.story_redrawAll(self,screen)
        else: Game.inGameRedrawAll(self, screen)

    @staticmethod
    def inGameRedrawAll(self, screen):
        currScreen = self.nav[self.navCurr]
        if (currScreen == "inGame"):

            woof = self.woofgang.sprites()[0]
            if woof.isRecording:
                if(self.sungNote == None):
                    screen.blit(self.emptyNote, (300, 300))

            screen.blit(self.background, (0, 0))
            for monster in self.monsterGroup:
                Game.drawHealth(monster, screen)
                if(monster.isBattling):
                    screen.blit(monster.notePic, (monster.x-20, monster.y-100))

            for i in range(3):
                tempX = 50 + 50*i
                screen.blit(self.collectBones[i], (tempX, 50))

            self.bone.draw(screen)
            self.woofgang.sprites()[0].collideBones(self.bone, self.collectBones,self.filledBone)
            self.platGroup.draw(screen)
            self.monsterGroup.draw(screen)
            self.woofgang.draw(screen)
            Game.drawHealth(self.woofgang.sprites()[0], screen)

    @staticmethod
    def drawHealth(obj, screen):
        health = obj.health
        leftX = obj.x
        rightX = leftX + (health / 2)
        bottomY = obj.y
        topY = bottomY - 60

        pygame.draw.rect(screen, (255, 255, 255), (leftX, topY, 100, 10))
        pygame.draw.rect(screen, (255, 0, 0), (leftX, topY, health, 10))


Game(1024, 832).run()
