import pygame
import random
from GameObject import GameObject

class Plat(GameObject):

    @staticmethod
    def init():
    	Plat.platImage = pygame.image.load("imgs/plat.png")

    def __init__(self):
    	self.x, self.y = random.randint(300, 1000), random.randint(570, 600)
    	super(Plat, self).__init__(self.x, self.y, self.platImage)
    	self.len = random.randint(0, 3)

