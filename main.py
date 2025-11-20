

import pygame                 
from game import settings      
from game.hud import HUD


def run(): # no devuelve nada 
    #principal function of the game
    pygame.init()

    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT)) # it gives a surface object 
    pygame.display.set_caption("Space Defender")

    clock = pygame.time.Clock() # helps with the speed of the game

    hud = HUD()
    score = 123
    lives = 3

    #game loop 
    running = True
    while running:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #if hte users clicks the x , finished
                running = False

        # logic update 
        # (por ahora no hay nada que actualizar)

       # drawing 
        screen.fill(settings.BG_COLOR)  

         # draw HUD test text
        hud.draw_centered_text(screen, "Hello HUD!", y_offset=-20, large=True)
        hud.draw_hud(screen, score, lives)
        
        # Pygame uses a double-buffer system: you draw everything on a hidden surface,
        # and flip() makes that frame visible on the screen.
        pygame.display.flip()

        # tick() adds a small delay to ensure the loop does not run faster than the
        # target FPS. If you set FPS to 60, the game will try to run at 60 frames/sec.

        clock.tick(settings.FPS)

    # game exited 
    pygame.quit()


if __name__ == "__main__":
    run()
