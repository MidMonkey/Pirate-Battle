import pygame
from math import sin, cos, pi


class Cannonball(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, theta):
        super().__init__()
        self.image = pygame.image.load("pirate_pack/Ship parts/cannonBall.png")
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.rect.center = [self.x, self.y]

        # init Screen
        self.screen = screen
        # self.screenwidth = self.screen.get_width()
        # self.screenheight = self.screen.get_height()

        # init data
        self.theta = theta
        self.velocity = 15

    def update(self):
        # needs to update image and rect based off of new theta
        self.rect = self.image.get_rect()

        deg_rad = pi / 180
        self.x += self.velocity * cos(self.theta * deg_rad)
        self.y -= self.velocity * sin(self.theta * deg_rad)
        self.rect.center = (int(self.x), int(self.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect.center)
