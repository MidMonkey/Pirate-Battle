import pygame
import sys
from multiplayerclass import PirateBattle
from singleplayerclass import SinglePlayer
from effect import Effects

# Initialize Pygame
print()
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Main Menu")
image_path = 'pirate_pack/Logos/logo2..png'
logo = pygame.image.load(image_path)
logo = pygame.transform.scale(logo, (300, 300))
"""image_path2 = 'pirate_pack/Logos/wheel.png'
logo2 = pygame.image.load(image_path2)
logo12 = pygame.transform.scale(logo2, (300, 300))"""


# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
dblue = (9, 19, 84)
green = (43, 179, 54)
# Set up fonts
font = pygame.font.Font(None, 36)

# Set up buttons
button_width, button_height = 200, 50
button_margin = 20

# Button 1
button1_rect = pygame.Rect((width - button_width) // 2, height // 1.15 - button_height - button_margin, button_width, button_height)

# Button 2
button2_rect = pygame.Rect((width - button_width) // 2, height // 1.15 + button_margin, button_width, button_height)

two_player = PirateBattle()
one_player = SinglePlayer()

setting = Effects(screen)
setting.music2()
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Check if buttons are clicked
                if button1_rect.collidepoint(event.pos):
                    two_player.run()
                    print("Button 1 clicked - Game 1")
                    # Add code to start Game 1 here
                elif button2_rect.collidepoint(event.pos):
                    one_player.run()
                    print("Button 2 clicked - Game 2")
                    # Add code to start Game 2 here

    # Clear the screen
    setting.background()

    # Draw title
    title_rect = logo.get_rect(center=(width // 2, height // 4+75))
    screen.blit(logo, title_rect)

    """# draw side images
    title_rect2 = logo2.get_rect(center=(width // 4+75 , height // 2))
    screen.blit(logo2, title_rect2)"""


    # Draw buttons
    pygame.draw.rect(screen, dblue, button1_rect)
    button1_text = font.render("Multiplayer", True, green)
    button1_text_rect = button1_text.get_rect(center=button1_rect.center)
    screen.blit(button1_text, button1_text_rect)

    pygame.draw.rect(screen, dblue, button2_rect)
    button2_text = font.render("Singleplayer", True, green)
    button2_text_rect = button2_text.get_rect(center=button2_rect.center)
    screen.blit(button2_text, button2_text_rect)

    # Update the display
    pygame.display.flip()
