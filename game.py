# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
HEIGHT = 650
WIDTH = 800
water_color = ((134, 235, 252))
my_ship = pygame.image.load("pirate_pack/ships/ship (1).png")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

ship_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(water_color)

    screen.blit(my_ship, ship_pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ship_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        ship_pos.y += 300 * dt
    if keys[pygame.K_a]:
        ship_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        ship_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()