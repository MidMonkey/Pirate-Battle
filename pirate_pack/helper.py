import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Score Example")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up font
font = pygame.font.Font(None, 36)

# Initial score
score = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update score (this could be based on game logic)
    score += 1

    # Clear the screen
    screen.fill(black)

    # Render the score text
    score_text = font.render("Score: {}".format(score), True, white)

    # Draw the score text in the upper left corner
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate (optional)
    pygame.time.Clock().tick(60)
