import pygame
from GameObject import GameObject

class Platform(GameObject):

    @staticmethod
    def init():
        pass

    def __init__(self, x, y):
        super(Platform, self).__init__(x, y, Platform.image)

    def update():
        pass