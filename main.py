import pygame
import sys
from ship import Ship
from effect import Effects
from cannonball import Cannonball


# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GHOST_SIZE = 10
FPS = 60
velocity = 0
theta = 0
# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pirate Battle")
clock = pygame.time.Clock()
running = True

# init classes
my_ship = Ship(screen, theta, velocity)
my_game = Effects(screen)
ball_group = pygame.sprite.Group()


# Plays the game soundtrack
my_game.music()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        theta -= 3
    elif keys[pygame.K_LEFT]:
        theta += 3  # may want to use a variable
    elif keys[pygame.K_UP]:
        velocity = 2
    elif keys[pygame.K_DOWN]:
        velocity = -2
    elif keys[pygame.K_k]:
        kill_theta = theta - 90
        ball_group.add(Cannonball(screen, my_ship.rect.x, my_ship.rect.y, kill_theta))
    elif keys[pygame.K_l]:
        kill_theta = theta + 90
        ball_group.add(Cannonball(screen, my_ship.rect.x, my_ship.rect.y, kill_theta))
    else:
        theta = theta
        velocity = 0

    my_game.background()
    my_ship.update(velocity, theta)
    my_ship.draw(screen)
    ball_group.update()
    ball_group.draw(screen)

    # Update Sprites


    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
