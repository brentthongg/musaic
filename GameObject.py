import pygame
# All game object inherit from this class.
class GameObject(pygame.sprite.Sprite): 
    
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.w, self.h = image.get_size()
        self.x, self.y, self.image = x, y, image
        self.rect = pygame.Rect(self.x - self.w / 2, self.y - self.h / 2, self.w, self.h)

    def update(self, screenWidth, screenHeight, dx = 0, dy = 0):
        self.x += dx
        self.y -= dy

        """ WRAP AROUND FEATURE 
        if self.x - (self.w / 2) > screenWidth:
            self.x = -(self.w // 2)
        elif self.x + (self.w / 2) < 0:
            self.x = screenWidth + (self.w // 2)
        """