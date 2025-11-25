

import pygame                 
from game import settings      
from game.hud import HUD
from game.player import Player      
from game.bullet import Bullet 
from game.enemy import Enemy
"""
1- velocidad vaya aumentando segun vaya psando el tiempo
2- pierdas una vida cada x enemigos que pasen x punto (hacer como una casa)
3- agregar sonido
4- agregar pantalla de inicio y de game over
5- agregar niveles

"""


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
    enemies = []

    frame_count = 0

    #game loop 
    running = True
    while running:
        frame_count += 1
        if frame_count % 60 == 0:
            enemies.append(Enemy())
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

        for enemy in enemies:
            enemy.update()

        enemies = [e for e in enemies if not e.off_screen]

        #if bullet hits enemy
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                 if bullet.rect.colliderect(enemy.rect):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 10
                    break

        #if enemy hits player
        for enemy in enemies[:]:
            if enemy.rect.colliderect(player.rect):
                enemies.remove(enemy)
                lives -= 1
                if lives <= 0:
                    running = False

       # drawing 
        screen.fill(settings.BG_COLOR)  

        player.draw(screen)

        for bullet in bullets:
            bullet.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)


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
