import random
import pygame
from ship import Ship
from math import sin, cos, pi
class Npc(Ship):
    def __init__(self, screen, path):
        # Set default values for velocity and theta
        # Call the constructor of the parent class (Ship)
        self.path = path
        self.image = pygame.image.load(self.path)
        self.og_image = self.image
        self.velocity = 2
        self.theta = random.randrange(0, 360)
        super().__init__(screen, self.theta, self.velocity, self.path)
        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()
        self.kill_radius = 150
    def npc_update(self):
        self.npc_ship_update()

    def npc_ship_update(self):
        self.border(self.x, self.y)

        # If the ship hits the border, adjust its course to a random angle
        if self.x == 0 or self.x == self.screenwidth or self.y == 0 or self.y == self.screenheight:
            self.theta = random.randrange(0, 360)

        self.image = pygame.transform.rotate(self.og_image, self.theta)
        self.rect = self.image.get_rect()

        deg_rad = pi/180
        self.x += 2 * cos((self.theta-90) * deg_rad)
        self.y -= 2 * sin((self.theta-90) * deg_rad)

        self.x = max(0, min(self.x, self.screenwidth))
        self.y = max(0, min(self.y, self.screenheight))

        self.rect.center = (self.x, self.y)
