import pygame
import sys

def keep_sprite_on_screen(sprite, screen_width, screen_height):
    """
    Adjusts the sprite's position to keep it within the screen boundaries.

    Parameters:
    - sprite: A Pygame sprite object with 'rect' attribute.
    - screen_width: Width of the screen.
    - screen_height: Height of the screen.
    """
    sprite_rect = sprite.rect

    # Ensure the sprite stays within the left boundary
    if sprite_rect.left < 0:
        sprite_rect.left = 0

    # Ensure the sprite stays within the right boundary
    if sprite_rect.right > screen_width:
        sprite_rect.right = screen_width

    # Ensure the sprite stays within the top boundary
    if sprite_rect.top < 0:
        sprite_rect.top = 0

    # Ensure the sprite stays within the bottom boundary
    if sprite_rect.bottom > screen_height:
        sprite_rect.bottom = screen_height

# Define your sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Replace with your sprite image
        self.image.fill((255, 0, 0))  # Replace with your desired color
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move Sprite with Arrow Keys")

# Create a sprite
my_sprite = MySprite()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle arrow key events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        my_sprite.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        my_sprite.rect.x += 5
    if keys[pygame.K_UP]:
        my_sprite.rect.y -= 5
    if keys[pygame.K_DOWN]:
        my_sprite.rect.y += 5

    # Call the function to keep the sprite on the screen
    keep_sprite_on_screen(my_sprite, screen_width, screen_height)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the sprite on the screen
    screen.blit(my_sprite.image, my_sprite.rect.topleft)

    # Update the display
    pygame.display.flip()

    # Set the frames per second (FPS)
    pygame.time.Clock().tick(60)
