import pygame
class Effects():
    def __init__(self,screen):
        self.screen = screen
        self.water = pygame.image.load('pirate_pack/Tiles/tile_73.png')
        self.x = self.water.get_width()
        self.y = self.water.get_height()
    def background(self):
        WIDTH = self.screen.get_width()
        HEIGHT = self.screen.get_height()
        for i in range(1,100):
            self.screen.blit(self.water,(WIDTH - i * self.x, HEIGHT - self.y))

