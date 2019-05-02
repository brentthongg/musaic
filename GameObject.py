import pygame
# All game object inherit from this class.
class GameObject(pygame.sprite.Sprite): 
    
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.w, self.h = image.get_size()
        self.x, self.y, self.image = x, y, image
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def onTop(self, block):
        return self.rect.bottom <= block.rect.top

    def processBlockCollision(self, blocks):
        self.rect.x += self.dx
        hitList = pygame.sprite.spritecollide(self, blocks, False)

        for block in hitList:
            # print(block.row, block.col)
            isOnTop = self.onTop(block)
            # print(x)
            if not isOnTop:
                if self.dx > 0:
                    self.rect.right = block.rect.left
                    self.dx = 0
                elif self.dx < 0:
                    self.rect.left = block.rect.right
                    self.dx = 0

    def update(self, screenWidth, screenHeight, dx = 0, dy = 0, blocks = None):
        if blocks != None:
            self.processBlockCollision(blocks)
        self.x += self.dx
        self.y += self.dy
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.dx = 0