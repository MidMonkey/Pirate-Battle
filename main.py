import pygame
import sys
from ship import Ship
from test2 import Effects


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
my_ship = Ship(screen)
my_game = Effects(screen)

# Plays the game soundtrack
my_game.music()
# init cannonballs
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    my_game.background()
    my_ship.draw(screen)

    # Update Sprites
    my_ship.update()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
