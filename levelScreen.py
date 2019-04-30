import pygame
from starter import PygameGame
from GameObject import GameObject

class levelScreen(PygameGame):
	def init(self):
		self.levelScreenCalled = False
		self.background = pygame.image.load("lvlImgs/1.png")
		pygame.mixer.init()
		self.music = pygame.mixer.music.load("music/Whimsical-Popsicle.mp3")
		pygame.mixer.music.play(100,0)
		self.level1Dims = (106,244,185,216) #(0:x1, 1:x2, 2:y1, 3:y2)
		self.level1Pressed = False


	# Keyboard Functions:
	def keyPressed(self, code, mod): pass

	def keyReleased(self, code, mod): pass

	# Mouse Functions:

	def mousePressed(self, x, y):
		(thisX,thisY) = pygame.mouse.get_pos()
		print(thisX,thisY)
		if (self.level1Dims[0]<=thisX <= self.level1Dims[1] and 
			self.level1Dims[2] <= thisY <= self.level1Dims[3]):
			self.level1Pressed = True

	def mouseReleased(self, x, y): pass

	def mouseMotion(self, x, y): pass

	def mouseDrag(self, x, y): pass

	# View:
	def redrawAll(self,screen):
		screen.blit(self.background,(0,0))
		self.background = pygame.transform.scale(self.background, (600,600)).convert_alpha()





levelScreen(600, 600).run()
