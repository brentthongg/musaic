# Run this file to play the game

import pygame
from starter import PygameGame
from GameObject import GameObject
from Woofgang import Woofgang

class Game(PygameGame):

    def setWoofgang(self):
        startX = 600
        startY = 600

        Woofgang.init()
        woofgangSprite = Woofgang(startX, startY)
        self.woofgang = pygame.sprite.GroupSingle(woofgangSprite)

    def init(self):
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
        woof.update(self.isKeyPressed, self.width, self.height)

    # View:

    def redrawAll(self, screen):
        self.woofgang.draw(screen)

Game(1200, 800).run()
