import pygame
import sys
from test2 import Gunboat
from test import Ball


# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GHOST_SIZE = 10
FPS = 60
theta = 0
speed = 0

# Colors
RED = (255, 0, 0)
water_color = ((134, 235, 252))

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pirate Battle")

# Load the car image

ghost_image = (pygame.Surface((GHOST_SIZE, GHOST_SIZE), pygame.SRCALPHA))
ghost = pygame.draw.rect(ghost_image, RED, (0, 0, GHOST_SIZE, GHOST_SIZE))

# Initial ghost position and speed
ghost_x = SCREEN_WIDTH // 2 - GHOST_SIZE // 2
ghost_y = SCREEN_HEIGHT // 2 - GHOST_SIZE // 2
ghost_speed = 5
ghost_angle = 0

# bringing in the ship
my_ship = pygame.image.load("pirate_pack/ships/ship (1).png")
my_ship = pygame.transform.rotate(my_ship, 180)
ship_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)  # find the center of the screen
center_pos = pygame.Vector2(my_ship.get_width() / 2,my_ship.get_height() / 2)  # find the center of the sprite
fix = ship_pos - center_pos # making the center of hte ship the same as the center of the screen
shipx, shipy = ship_pos - center_pos
# Main game loop
clock = pygame.time.Clock()
running = True

# Plays the game soundtrack
pygame.mixer_music.load("Audio/B_music.mp3")
pygame.mixer_music.play(-1)
gunboat = Gunboat(screen, theta, speed)
ball = Ball(center_pos,screen)
balls = pygame.sprite.Group()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # get list of keyboard booleans
    keys = pygame.key.get_pressed()

    # Update car position based on arrow key inputs
    if keys[pygame.K_UP]:
        speed = 5
        gunboat.update()
    if keys[pygame.K_DOWN]:
        speed = 5
        gunboat.reverse_update()
    if keys[pygame.K_LEFT]:
        speed = 5
        theta += 1
        gunboat.update()
    if keys[pygame.K_RIGHT]:
        speed = 5
        theta -= 1
        gunboat.update()
    if keys[pygame.K_SPACE]:
        balls.add(Ball)

    # Update Sprites
    balls.draw(screen)
    balls.update()
    # Clear the screen
    screen.fill(water_color)

    # Rotate the car image based on the car_angle
    rotated_ghost = pygame.transform.rotate(ghost_image, ghost_angle)

    # Draw the rotated car on the screen
    screen.blit(rotated_ghost, (ghost_x, ghost_y))
    screen.blit(my_ship, fix)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
