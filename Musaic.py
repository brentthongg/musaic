# Run this file to play the game

import pygame
from starter import PygameGame

class Game(PygameGame):

    def init(self): pass

    # Keyboard Functions:
    def keyPressed(self, code, mod): pass

    def keyReleased(self, code, mod): pass

    # Mouse Functions:

    def mousePressed(self, x, y): pass

    def mouseReleased(self, x, y): pass

    def mouseMotion(self, x, y): pass

    def mouseDrag(self, x, y): pass

    # Timer Fired:

    def timerFired(self, dt): pass

    # View:

    def redrawAll(self, screen): pass

Game(1200, 800).run()
