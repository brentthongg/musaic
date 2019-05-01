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
from Platform import Plat
import levels


class Game(PygameGame):

    def setWoofgang(self):
        startX = 100
        startY = 600

        Woofgang.init()
        woofgangSprite = Woofgang(startX, startY)
        self.woofgang = pygame.sprite.GroupSingle(woofgangSprite)

        #Level.addMonsters(self.monsters)
    def initializeMonsters():
        Monster.init()
        Snake.init()

    def setMonster(self):
        Game.initializeMonsters()
        testMonster = Snake(600, 600, 2)
        self.monsters = pygame.sprite.GroupSingle(testMonster)

    def setLevel(self):
        Plat.init()
        self.platGroup = pygame.sprite.Group()
        if(self.level ==1):
            self.stage = levels.Level(3)
        for plat in self.stage.Plats:
            self.platGroup.add(plat)


    def init(self):
        self.background = pygame.image.load("imgs/backgroundForest.png")
        Game.setWoofgang(self)
        Game.setMonster(self)
        self.level = 1
        Game.setLevel(self)

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
        self.monsters.update(woof, self.width, self.height)
        if(woof.isBattling):
            for monster in self.monsters.sprites():
                if(monster.isBattling):
                    if not monster.notePlayed:
                        pitchCode.playNote(monster.startingNote)
                        monster.notePlayed = True
                    sungNote = pitchCode.record()
                    print(monster.startingNote, sungNote)
                    if(monster.checkInterval(sungNote)):
                        monster.kill()
                        break
                        
    def redrawAll(self, screen):
        screen.blit(self.background, (0, 0))
        for monster in self.monsters:
            if(monster.isBattling):
                screen.blit(monster.notePic, (monster.x-20, monster.y-100))
        self.woofgang.draw(screen)
        self.monsters.draw(screen)
        self.platGroup.draw(screen)

Game(1024, 800).run()
