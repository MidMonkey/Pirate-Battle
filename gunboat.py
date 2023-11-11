import pygame.sprite
from math import pi, cos, sin, atan2, atan


class AbstractGunboat():
    image = pygame.image.load("pirate_pack/ships/ship (1).png")
    image = pygame.transform.rotate(image, 180)
    def __init__(self,screen, max_vel, rotation_vel):
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 5
        self.screen = screen
        self.x, self.y  = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
    def blit_rotate_center(self, screen, top_left, angle):
        rotated_image = pygame.transform.rotate(self.image, angle)
        """This function will rotate the image about the top left corner which is not good because it will spin the rect and distort
        the inner image"""
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=top_left).center)
        """this should fix the problem above
        by making the image rotate about its center"""
        screen.blit(rotated_image, new_rect.topleft)
    def draw(self, screen):
        self.blit_rotate_center(screen, self.x, self.y, self.angle)   # add the sprite image as the image.
    def move_forward(self,speed):
    def move_backward(self, speed):
class Gunboat(AbstractGunboat):
    def __init__(self):
        super().__init__(screen, max_vel, rotation_vel)



    def draw(self, screen, images):
        for img in images:
            screen.blit(img, self.ship_pos)
        self.image.draw()
        pygame.display.update(new_rect)

