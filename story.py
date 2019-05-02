import pygame

class story():
    def story_init(self):
        self.storybg = pygame.image.load("slides/scene1.png")
        self.scenes = ["slides/scene1.png","slides/scene2.png","slides/scene3.png",
        "slides/scene4.png","slides/scene5.png","slides/scene6.png","slides/scene7.png",
        "slides/scene8.png"]
        self.currScene = 1
        self.currMusic = 0
        self.events = pygame.event.get()
        self.storyFinished = False
        pygame.mixer.init()
        self.musicTitles = ["music/fantasyForestBattle","music/clockMaker","music/crusaders",
        "music/parisLoop","music/8bit"]
        self.storymusic = pygame.mixer.music.load(self.musicTitles[self.currMusic]+".mp3")
        pygame.mixer.music.play(100,3)

    def story_keyPressed(self, code, mod):
        if code == pygame.K_UP or code == pygame.K_RIGHT: 
            if (self.currScene >= 8): 
                self.storyFinished = True
            else:
                self.currScene += 1
                if self.currScene in [3,5,6,8]:
                    self.currMusic += 1
                    pygame.mixer.music.load(self.musicTitles[self.currMusic]+".mp3")
                    pygame.mixer.music.play(100,0)
        if code == pygame.K_DOWN or code == pygame.K_LEFT: 
            if (self.currScene!= 1): 
                self.currScene -= 1
                if self.currScene in [3,5,6,8]:
                    self.currMusic -= 1
                    pygame.mixer.music.load(self.musicTitles[self.currMusic]+".mp3")
                    pygame.mixer.music.play(100,0)

    def story_finished(self):
        return self.storyFinished

    def story_keyReleased(self, code, mod): pass

    def story_mousePressed(self, x, y): pass

    def story_mouseReleased(self, x, y): pass

    def story_mouseMotion(self, x, y): pass

    def story_mouseDrag(self, x, y): pass

    def story_redrawAll(self,screen):
        screen.blit(self.storybg,(0,0))
        self.storybg = pygame.transform.scale(self.storybg, (600,600)).convert_alpha()
        if (self.currScene <= 8):
            self.storybg = pygame.image.load(self.scenes[self.currScene-1])
        