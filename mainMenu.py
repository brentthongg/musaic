import pygame
from GameObject import GameObject

class mainMenu():
    def mainMenu_init(self):
        self.mmbg = pygame.image.load("imgs/mainMenuBG.png")
        pygame.mixer.init()
        self.mmmusic = pygame.mixer.music.load("music/Whimsical-Popsicle.mp3")
        pygame.mixer.music.play(100,0)
        #dimensions of UI buttons
        self.startDims = (60,145,327,356) #(0:x1, 1:x2, 2:y1, 3:y2)
        self.configDims = (60,284,375,407)
        self.infoDims = (60,130,418,447)
        self.quitDims = (60,136,460,495)
        self.startPressed = False
        self.configPressed = False
        self.infoPressed = False
        self.quitPressed = False

    # Keyboard Functions:
    def mainMenu_keyPressed(self, code, mod): pass

    def mainMenu_keyReleased(self, code, mod): pass

    # Mouse Functions:

    def mainMenu_mousePressed(self, x, y):
    	(thisX,thisY) = pygame.mouse.get_pos()
    	#if user presses "start"
    	if (self.startDims[0]<=thisX <= self.startDims[1] and
    		self.startDims[2] <= thisY <= self.startDims[3]):
    		self.startPressed = True
    		#Start Game Here
    	elif (self.configDims[0]<=thisX <= self.configDims[1] and 
    		self.configDims[2] <= thisY <= self.configDims[3]):
    		#Config Screen TBM
    		self.configPressed = True
    		pass
    	elif (self.infoDims[0]<=thisX <= self.infoDims[1] and 
    		self.infoDims[2] <= thisY <= self.infoDims[3]):
    		#Info Screen TBM
    		self.infoPressed = True
    		pass
    	elif (self.quitDims[0]<=thisX <= self.quitDims[1] and 
    		self.quitDims[2] <= thisY <= self.quitDims[3]):
    		self.quitPressed = True
    	else: pass
    def getStartPressed(self):
        return self.startPressed

    def mainMenu_mouseReleased(self, x, y): pass

    def mainMenu_mouseMotion(self, x, y): pass

    def mainMenu_mouseDrag(self, x, y): pass

    # View:
    def mainMenu_redrawAll(self,screen):
        screen.blit(self.mmbg,(0,0))
        self.mmbg = pygame.transform.scale(self.mmbg, (600,600)).convert_alpha()
        if (self.startPressed):
        	pygame.draw.lines(self.mmbg,(255, 245, 228),True,[(60,327),(60,356),(145,356),(145,327)],3)
        if (self.configPressed):
        	pygame.draw.lines(self.mmbg,(255, 245, 228),True,[(60,407),(60,375),(290,375),(290,407)],3)
        if (self.infoPressed):
        	pygame.draw.lines(self.mmbg,(255, 245, 228),True,[(60,447),(60,418),(130,418),(130,447)],3)
        if (self.quitPressed):
        	pygame.draw.lines(self.mmbg,(255, 245, 228),True,[(60,460),(60,495),(136,460),(136,495)],3)
        	pygame.quit()