# Run this file to play the game

import pygame
from starter import PygameGame
from GameObject import GameObject
from Woofgang import Woofgang
import pitchCode 

class Game(PygameGame):

    def setWoofgang(self):
        startX = 600
        startY = 600

        Woofgang.init()
        woofgangSprite = Woofgang(startX, startY)
        self.woofgang = pygame.sprite.GroupSingle(woofgangSprite)

        self.monsters = pygame.sprite.Group()

        Level.addMonsters(self.monsters)

    def init(self):
        self.background = pygame.image.load("imgs/backgroundForest.png")
        Game.setWoofgang(self)

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
        if(woof.isBattling):
            sungNote = pitchCode.record()
            for monster in self.monsters.sprites():
                if monster.isBattling:
                    monster.check(sungNote)
    # View:

    def redrawAll(self, screen):
        screen.blit(self.background, (0, 0))
        self.woofgang.draw(screen)
        self.monsters.draw(screen)

Game(1024, 800).run()
