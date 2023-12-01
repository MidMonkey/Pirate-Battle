import pygame
import sys
from ship import Ship
from effect import Effects
from cannonball import Cannonball
from npc import Npc
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
my_ship = Ship(screen, theta1, velocity1,'pirate_pack/ships/ship (5).png')
npcs = Npc(screen, 'pirate_pack/ships/ship (4).png', my_ship)
my_game = Effects(screen)
ball_group = pygame.sprite.Group()
npc_ball_group = pygame.sprite.Group()


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
    # attack playercontroled ship if it is within a certain radius.
    npcs.attack(npcs, my_ship, npc_ball_group)
    # tile background
    my_game.background()
    # update both cannonball groups before updating ships.
    # update first ball group
    ball_group.update()
    ball_group.draw(screen)
    # update second ball group
    npc_ball_group.update()
    npc_ball_group.draw(screen)
    # update first sprite
    my_ship.update(velocity1, theta1, my_ship, npc_ball_group)
    my_ship.draw(screen)
    npcs.npc_update(npcs, ball_group)
    npcs.draw(screen)

    # kill cannonball sprites after first contact.
    collisions = pygame.sprite.spritecollide(my_ship, npc_ball_group, True)
    for i in collisions:
        i.kill()
    collisions2 = pygame.sprite.spritecollide(npcs, ball_group, True)
    for i in collisions2:
        i.kill()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
