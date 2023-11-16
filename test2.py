import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Shooting Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Car properties
car_width = 50
car_height = 80
car_x = width // 2 - car_width // 2
car_y = height - car_height - 10
car_speed = 5

# Projectile properties
projectile_width = 5
projectile_height = 15
projectile_speed = 7
projectiles = []

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_x * car_speed
            elif event.key == pygame.K_RIGHT:
                car_x * -1 * car_speed
            elif event.key == pygame.K_SPACE:
                # Shoot a projectile
                projectile_x = car_x + car_width // 2 - projectile_width // 2
                projectile_y = car_y
                projectiles.append([projectile_x, projectile_y])

    # Move projectiles
    for projectile in projectiles:
        projectile[1] -= projectile_speed

    # Remove projectiles that are off-screen
    projectiles = [projectile for projectile in projectiles if projectile[1] > 0]

    # Update display
    screen.fill(white)

    # Draw car
    pygame.draw.rect(screen, black, [car_x, car_y, car_width, car_height])

    # Draw projectiles
    for projectile in projectiles:
        pygame.draw.rect(screen, red, [projectile[0], projectile[1], projectile_width, projectile_height])

    # Update display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(30)
