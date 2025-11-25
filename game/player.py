import pygame
from . import settings, assets

class Player:
    """Player ship: handles position, movement and drawing."""

    def __init__(self) -> None:
        # Load the player image (or a placeholder if missing)
        self.image = assets.load_image("player.png", size=(50, 40))

        # Rect stores position and size of the player
        self.rect = self.image.get_rect()

        # Start centered at the bottom of the screen
        self.rect.centerx = settings.WIDTH // 2
        self.rect.bottom = settings.HEIGHT - 20

        # Movement speed in pixels per frame
        self.speed = settings.PLAYER_SPEED

    def handle_input(self, keys: pygame.key.ScancodeWrapper) -> None:
        """
        Move the player based on pressed keys.
        """
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep the player inside the screen boundaries
        self.rect.clamp_ip(pygame.Rect(0, 0, settings.WIDTH, settings.HEIGHT))

    def update(self) -> None:
        """
        Placeholder for future logic 
        """
        pass

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the player image at its current position."""
        screen.blit(self.image, self.rect)