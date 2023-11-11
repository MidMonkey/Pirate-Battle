import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Car parameters
CAR_WIDTH = 50
CAR_HEIGHT = 100
CAR_SPEED = 5

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Race Driving Game')

clock = pygame.time.Clock()

# Load original car image
original_car_image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
pygame.draw.rect(original_car_image, RED, (0, 0, CAR_WIDTH, CAR_HEIGHT))
car_rect = original_car_image.get_rect(center=(WIDTH // 2, HEIGHT - 100))

# Original car image without rotation (used for drawing xy axis)
car_image = original_car_image.copy()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_rect.x -= CAR_SPEED
    if keys[pygame.K_RIGHT]:
        car_rect.x += CAR_SPEED
    if keys[pygame.K_UP]:
        car_rect.y -= CAR_SPEED
    if keys[pygame.K_DOWN]:
        car_rect.y += CAR_SPEED

    # Calculate the angle based on the direction vector
    angle = math.degrees(math.atan2(-car_rect.y, car_rect.x))

    # Rotate the car image based on the calculated angle
    rotated_car_image = pygame.transform.rotate(original_car_image, angle)

    # Update game logic here

    # Draw everything
    screen.fill(WHITE)

    # Draw rotated xy axis based on the car's angle
    rotated_x_axis = pygame.transform.rotate(pygame.Surface((50, 2)), angle)
    rotated_y_axis = pygame.transform.rotate(pygame.Surface((2, 50)), angle)

    screen.blit(rotated_x_axis, (car_rect.centerx, car_rect.centery))
    screen.blit(rotated_y_axis, (car_rect.centerx, car_rect.centery))

    # Draw rotated car image
    screen.blit(rotated_car_image, car_rect.topleft)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
