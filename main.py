

import pygame                 
from game import settings      
from game.hud import HUD
from game.player import Player      
from game.bullet import Bullet 


def run(): # no devuelve nada 
    #principal function of the game
    pygame.init()

    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT)) # it gives a surface object 
    pygame.display.set_caption("Space Defender")

    clock = pygame.time.Clock() # helps with the speed of the game

    hud = HUD()
    score = 123
    lives = 3

    player = Player()
    bullets= []


    #game loop 
    running = True
    while running:
        keys = pygame.key.get_pressed()
        player.handle_input(keys)
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #if hte users clicks the x , finished
                running = False
            
            if event.type == pygame.KEYDOWN and event.key ==pygame.K_SPACE:
                bullets.append(Bullet(player.rect.centerx, player.rect.top))

        # logic update 
        player.update()

        for bullet in bullets :
            bullet.update()
            
        bullets = [b for b in bullets if not b.off_screen]

        

       # drawing 
        screen.fill(settings.BG_COLOR)  

        player.draw(screen)

        for bullet in bullets:
            bullet.draw(screen)

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
