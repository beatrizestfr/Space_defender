import pygame
from . import settings, assets

class Bullet:

    def __init__(self, x, y):
        self.image = assets.load_image("bullet.png", size=(5, 10))
        self.rect = self.image.get_rect(center =(x,y))
        self.speed = settings.BULLET_SPEED

        # colocarla donde se disparo 

    def update(self):
        self.rect.y-= self.speed

    def draw(self, screen:pygame.Surface):
        screen.blit(self.image, self.rect)


    @property
    def off_screen(self):
        if self.rect.bottom < 0 or self.rect.top > settings.HEIGHT:
            return True
        else:
            return False
