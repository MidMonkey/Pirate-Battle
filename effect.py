import pygame
class Effects():
    def __init__(self,screen):
        self.screen = screen
        self.water = pygame.image.load('pirate_pack/Tiles/tile_73.png')
        self.water = pygame.transform.scale(self.water, (20, 20))
        self.x = self.water.get_width()
        self.y = self.water.get_height()
        self.guntime = 0
    def background(self):
        WIDTH = self.screen.get_width()
        HEIGHT = self.screen.get_height()
        for x in range(0, WIDTH, self.x):
            for y in range(0, HEIGHT, self.y):
                self.screen.blit(self.water, (x,y))
    def music(self):
        self.music = pygame.mixer_music.load("Audio/B_music.mp3")
        pygame.mixer_music.play(-1)
    def music2(self):
        self.music = pygame.mixer_music.load("Audio/ship_ambience.wav")
        pygame.mixer_music.play(-1)

    def cannon_boom(self):
        esound = pygame.mixer.Sound('Audio/cannonball-89596.mp3')
        esound.play()
        """I had a bug where adding sound effects caused my background music to restart. Jay Barreto showed me that
        there were different ways to initialized the music so that this would not happer"""

    def display_score1(self, screen, score):
        # Set up the font
        font = pygame.font.Font(None, 36)

        # Render the text
        text = font.render(f"Score: {score}", True, (255, 255, 255))

        # Get the text rect and set its position to the top left corner
        text_rect = text.get_rect()
        text_rect.topleft = (50, 10)

        # Draw the text on the screen
        screen.blit(text, text_rect)

        # Update the display
        pygame.display.flip()
    def display_score2(self, screen, score1, score2):
        # Set up the font
        font = pygame.font.Font(None, 36)

        # Render the text
        text = font.render(f"Blue: {score1} | Red {score2}", True, (255, 255, 255))

        # Get the text rect and set its position to the top left corner
        text_rect = text.get_rect()
        text_rect.topleft = (50, 10)

        # Draw the text on the screen
        screen.blit(text, text_rect)

        # Update the display
        pygame.display.flip()




