#Heads-Up Display

import pygame
from . import assets

class HUD:
    """Heads-Up Display: handles drawing score, lives and generic text."""


    def __init__(self) -> None:
        # pre-load two fonts: one small, one large
        self.font_small = assets.get_font(24)
        self.font_large = assets.get_font(48)
    

    def draw_hud(self, screen: pygame.Surface, score: int, lives: int) -> None:
        """Draw score and lives in the top-left corner."""
        # render the text into surfaces
        score_surf = self.font_small.render(f"Score: {score}", True, (255, 255, 255))
        lives_surf = self.font_small.render(f"Lives: {lives}", True, (255, 255, 255))

        # blit them onto the screen
        screen.blit(score_surf, (10, 10))
        screen.blit(lives_surf, (10, 40))


    def draw_centered_text(
        self,
        screen: pygame.Surface,
        text: str,
        y_offset: int = 0,
        large: bool = True,
    ) -> None:
        """
        Draw text centered on the screen.
        y_offset moves it up or down from the vertical center.
        """
        # choose font size
        font = self.font_large if large else self.font_small

        # create the text surface
        surf = font.render(text, True, (255, 255, 255))

        # center it on the screen
        rect = surf.get_rect(
            center=(screen.get_width() // 2, screen.get_height() // 2 + y_offset)
        )

        # draw it
        screen.blit(surf, rect)
