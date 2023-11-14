import pygame
from math import cos, sin, pi, atan2
class Gunboat(pygame.sprite.Sprite):
    def __init__(self, screen, theta = 0,speed = 0):
        super().__init__()
        self.screen = screen
        self.my_ship = pygame.image.load("pirate_pack/ships/ship (1).png")
        self.my_ship = pygame.transform.rotate(self.my_ship, 180)
        self.ship_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)  # find the center of the screen
        self.center_pos = pygame.Vector2(self.my_ship.get_width() / 2, self.my_ship.get_height() / 2)  # find the center of the sprite
        self.x, self.y = self.ship_pos - self.center_pos  # making the center of hte ship the same as the center of the screen
        self.theta = theta
        self.speed = speed

    def update(self):

        # move the ship with it's speed
        self.x = self.x + self.speed * cos(self.theta)
        self.y = self.y + self.speed * sin(self.theta)

        # update the rectangle
        # self.rect.x = self.x
        # self.rect.y = self.y
    def reverse_update(self):

        # move the ship with it's speed
        self.x = self.x - self.speed * cos(self.theta)
        self.y = self.y - self.speed * sin(self.theta)

        # update the rectangle
        # self.rect.x = self.x
        # self.rect.y = self.y
    def move_ship(self):
        new_ship = pygame.transform.rotate(self.my_ship, self.theta)





