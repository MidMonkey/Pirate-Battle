import pygame
from math  import sin, cos, pi


class Ship(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = pygame.image.load("pirate_pack/ships/ship (1).png")
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.theta = 0
        self.velocity = 0 # in pixels per second
        self.x, self.y = [200,200] # Coordinates of the upper left corner.
        self.rect.center = [self.x, self.y]
        self.og_image = self.image
        self.screen = screen

        # needs image
        # needs rect

        # need update()
    def update(self):
        self.update_controls()
        # needs to update image and rect based off of new theta
        self.image = pygame.transform.rotate(self.og_image, self.theta)
        self.rect = self.image.get_rect()

        deg_rad = pi/180
        self.x += self.velocity * cos(self.theta * deg_rad)
        self.y -= self.velocity * sin(self.theta * deg_rad)
        # needs to calculate new x and y
        # update the rectangle

        self.rect.center = (self.x, self.y)
    def update_controls(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.theta -= 5
        elif keys[pygame.K_LEFT]:
            self.theta += 5  # may want to use a variable
        elif keys[pygame.K_UP]:
            self.velocity += 1 * .5
        elif keys[pygame.K_DOWN]:
            self.velocity -= 1 * .5
        else:
            self.theta = self.theta
            self.velocity = 0

        # need a draw()
    def draw(self, screen):
        screen.blit(self.image,self.rect)
    

