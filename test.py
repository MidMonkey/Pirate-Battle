import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Car parameters
CAR_WIDTH = 50
CAR_HEIGHT = 100
CAR_SPEED = 3

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Race Driving Game')

clock = pygame.time.Clock()

# Load car image
car_image = pygame.image.load("pirate_pack/ships/ship (1).png")
pygame.draw.rect(car_image, RED, (0, 0, CAR_WIDTH, CAR_HEIGHT))
car_rect = car_image.get_rect(center=(WIDTH // 2, HEIGHT - 100))

# Initial direction vector (x, y)
direction = pygame.math.Vector2(0, -1)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction.rotate_ip(3)  # Rotate left
    if keys[pygame.K_RIGHT]:
        direction.rotate_ip(-3)  # Rotate right
    if keys[pygame.K_UP]:
        car_rect.x += direction.x * CAR_SPEED
        car_rect.y += direction.y * CAR_SPEED  # used to be CAR_SPEED
    if keys[pygame.K_DOWN]:
        car_rect.x += direction.x * -CAR_SPEED
        car_rect.y += direction.y * -CAR_SPEED

        # Update car position based on direction

    # Wrap the car around the screen edges
    car_rect.x %= WIDTH
    car_rect.y %= HEIGHT

    # Update game logic here

    # Draw everything
    screen.fill(WHITE)
    rotated_car = pygame.transform.rotate(car_image, -direction.angle_to(pygame.math.Vector2(0, -1)))
    screen.blit(rotated_car, car_rect.topleft)

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
