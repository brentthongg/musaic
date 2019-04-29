# Run this file to play the game

import pygame
from starter import PygameGame
from GameObject import GameObject
from Woofgang import Woofgang
from AllMonsters import *
import pitchCode 

class Game(PygameGame):

    def setWoofgang(self):
        startX = 100
        startY = 600

        Woofgang.init()
        woofgangSprite = Woofgang(startX, startY)
        self.woofgang = pygame.sprite.GroupSingle(woofgangSprite)

        #Level.addMonsters(self.monsters)
    def initializeMonsters():
        Snake.init()

    def setMonster(self):
        Game.initializeMonsters()
        testMonster = Snake(600, 600, 2)
        self.monsters = pygame.sprite.GroupSingle(testMonster)
        pass

    def init(self):
        self.background = pygame.image.load("imgs/backgroundForest.png")
        Game.setWoofgang(self)
        Game.setMonster(self)

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
        woof.update(self.isKeyPressed, self.width, self.height, dt)
        self.monsters.update(woof, self.width, self.height)
        #print("Woof Loc:", woof.x, woof.y)
        if(woof.isBattling):
            sungNote = pitchCode.record()
            #print(sungNote)
            for monster in self.monsters.sprites():
                #print("Monster Loc:", monster.x, monster.y)
                if monster.isBattling:
                    pitchCode.playNote(monster.startingNote)
                    if monster.checkInterval(sungNote):
                      monster.kill()
    # View:

    def redrawAll(self, screen):
        screen.blit(self.background, (0, 0))
        self.woofgang.draw(screen)
        self.monsters.draw(screen)

Game(1024, 800).run()
