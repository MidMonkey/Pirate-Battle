import pygame
import sys
from ship import Ship
from effect import Effects
from cannonball import Cannonball
from control import Controls


# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GHOST_SIZE = 10
FPS = 60
velocity1 = 0
theta1 = 0
velocity2 = 0
theta2 = 0
shots_fired = 0
sshots_fired = 0
# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pirate Battle")
clock = pygame.time.Clock()
running = True

# init classes

your_ship = Ship(screen, theta2, velocity2, 'pirate_pack/ships/ship (3).png')
my_ship = Ship(screen, theta1, velocity1,'pirate_pack/ships/ship (5).png')
"""my_ship_controls = Controls(screen,velocity1, theta1)
your_ship_controls = Controls(screen, velocity2, theta2)"""
my_game = Effects(screen)
ball_group = pygame.sprite.Group()
your_ball_group = pygame.sprite.Group()
#  my_ship_group = pygame.sprite.Group()
#  your_ship_group = pygame.sprite.Group()


# Plays the game soundtrack
my_game.music()


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    #my_ship_controls.player1_controls(keys)
    #your_ship_controls.player2_controls(keys)
    #controls for player 1
    if keys[pygame.K_RIGHT]:
        theta1 -= 3
    elif keys[pygame.K_LEFT]:
        theta1 += 3  # may want to use a variable
    elif keys[pygame.K_UP]:
        velocity1 = 2
    elif keys[pygame.K_DOWN]:
        velocity1 = -2
    elif keys[pygame.K_k]:
        if not shots_fired:
            kill_theta = theta1 - 90
            x1 = my_ship.rect.centerx
            y1 = my_ship.rect.centery
            ball_group.add(Cannonball(screen, x1, y1, kill_theta))
            my_game.cannon_boom()
            shots_fired = True


    elif keys[pygame.K_l]:
        if not shots_fired:
            kill_theta = theta1 + 90
            x1 = my_ship.rect.centerx
            y1 = my_ship.rect.centery
            ball_group.add(Cannonball(screen, x1, y1, kill_theta))
            my_game.cannon_boom()
            shots_fired = True

    else:
        theta1 = theta1
        velocity1 = 0
        shots_fired = 0
    # controls for player 2
    if keys[pygame.K_d]:
        theta2 -= 3
    elif keys[pygame.K_a]:
        theta2 += 3  # may want to use a variable
    elif keys[pygame.K_w]:
        velocity2 = 2
    elif keys[pygame.K_s]:
        velocity2 = -2
    elif keys[pygame.K_h]:
        if not sshots_fired:
            kill_theta2 = theta2 - 90
            x2 = your_ship.rect.centerx
            y2 = your_ship.rect.centery
            your_ball_group.add(Cannonball(screen, x2, y2, kill_theta2))
            my_game.cannon_boom()
            sshots_fired = True
    elif keys[pygame.K_g]:
        if not sshots_fired:
            kill_theta2 = theta2 + 90
            x2 = your_ship.rect.centerx
            y2 = your_ship.rect.centery
            your_ball_group.add(Cannonball(screen, x2, y2, kill_theta2))
            my_game.cannon_boom()
            sshots_fired = True
    else:
        theta2 = theta2
        velocity2 = 0
        sshots_fired = 0





    # tile background
    my_game.background()
    # update both cannonball groups before updating ships.
    # update first ball group
    ball_group.update()
    ball_group.draw(screen)
    # update second ball group
    your_ball_group.update()
    your_ball_group.draw(screen)
    # update first sprite
    my_ship.update(velocity1, theta1, my_ship, your_ball_group)
    my_ship.draw(screen)
    # update second sprite
    your_ship.update(velocity2, theta2, your_ship, ball_group)
    your_ship.draw(screen)

    # kill cannonball sprites after first contact.
    collisions = pygame.sprite.spritecollide(my_ship, your_ball_group, True)
    for i in collisions:
        i.kill()
    collisions2 = pygame.sprite.spritecollide(your_ship, ball_group, True)
    for i in collisions2:
        i.kill()



    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
