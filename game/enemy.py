import pygame
import random
from . import settings, assets

class Enemy:
    """Enemy ship: handles position, movement and drawing."""

    def __init__ (self):
        self.image =assets.load_image("enemy.png", size=(40,30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, settings.WIDTH - self.rect.width)
        self.rect.y = -self.rect.height

        self.speed = settings.ENEMY_SPEED

    def update(self):
        self.rect.y += self.speed


    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)

    @property
    def off_screen(self):
        if self.rect.top > settings.HEIGHT :
            return True
        else:
            return False