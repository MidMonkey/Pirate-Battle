import pygame
class Effects():
    def __init__(self,screen):
        self.screen = screen
        self.water = pygame.image.load('pirate_pack/Tiles/tile_73.png')
        self.x = self.water.get_width()
        self.y = self.water.get_height()
    def background(self):
        width = self.screen.get_width()
        height = self.screen.get_height()
        for i in range(1,100):
            # screen.blit(sand, (WIDTH - i * picwidth, HEIGHT - picheight))
            self.screen.blit(self.water,(width - i*self.x, height - self.y) )
