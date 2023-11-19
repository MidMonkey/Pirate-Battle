import pygame
class Effects():
    def __init__(self,screen):
        self.screen = screen
        self.water = pygame.image.load('pirate_pack/Tiles/tile_73.png')
        self.water = pygame.transform.scale(self.water, (20, 20))
        self.x = self.water.get_width()
        self.y = self.water.get_height()
    def background(self):
        WIDTH = self.screen.get_width()
        HEIGHT = self.screen.get_height()
        for x in range(0, WIDTH, self.x):
            for y in range(0, HEIGHT, self.y):
                self.screen.blit(self.water, (x,y))
    def music(self):
        self.music = pygame.mixer_music.load("Audio/B_music.mp3")
        pygame.mixer_music.play(-1)

