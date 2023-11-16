import pygame
import sys
from ship import Ship

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GHOST_SIZE = 10
FPS = 60
velocity = 0
theta = 0


# Colors

water_color = ((134, 235, 252))

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pirate Battle")
# Load the car image


# Initial ghost position and speed
# Main game loop
clock = pygame.time.Clock()
running = True

# Plays the game soundtrack
pygame.mixer_music.load("Audio/B_music.mp3")
pygame.mixer_music.play(-1)

my_ship = Ship(screen)

# init cannonballs
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(water_color)
    my_ship.draw(screen)




    # Update Sprites
    my_ship.update()



    # Clear the screen




    # Draw the rotated car on the screen

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
