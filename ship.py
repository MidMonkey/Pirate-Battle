import pygame
from math import sin, cos, pi
from cannonball import Cannonball


class Ship(pygame.sprite.Sprite):
    def __init__(self,screen, theta, velocity):
        super().__init__()
        #  init sprite variables
        self.image = pygame.image.load("pirate_pack/ships/ship (5).png")
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = self.image.get_width()
        self.rect.y = self.image.get_height()
        self.theta = 0
        self.velocity = 0 # in pixels per second
        self.x, self.y = [200,200] # Coordinates of the upper left corner.
        self.rect.center = [self.x, self.y]
        self.og_image = self.image

        # init screen variables
        self.screen = screen
        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()

        # cannonballs
        self.ball = Cannonball(self.screen, self.x, self.y, self.theta)

        self.cannonball_group = pygame.sprite.Group()


    def update(self, velocity, theta):
        #self.update_controls()
        self.ship_update(velocity, theta)


    def ship_update(self, velocity, theta):
        self.border(self.x, self.y)
        # needs to update image and rect based off of new theta
        self.velocity = velocity
        self.theta = theta
        self.image = pygame.transform.rotate(self.og_image, self.theta)
        self.rect = self.image.get_rect()

        deg_rad = pi/180
        self.x += self.velocity * cos(self.theta * deg_rad)
        self.y -= self.velocity * sin(self.theta * deg_rad)

        self.x = max(0, min(self.x, self.screenwidth))
        self.y = max(0, min(self.y, self.screenheight))
        # needs to calculate new x and y
        # update the rectangle

        self.rect.center = (self.x, self.y)

    """def update_controls(self):
        self.ball = Cannonball(self.screen, self.x, self.y, self.theta)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.theta -= 3
        elif keys[pygame.K_LEFT]:
            self.theta += 3  # may want to use a variable
        elif keys[pygame.K_UP]:
            self.velocity = 2
        elif keys[pygame.K_DOWN]:
            self.velocity = -2
        elif keys[pygame.K_k]:
            self.cannonball_group.add(self.ball)
            print(self.cannonball_group)
        else:
            self.theta = self.theta
            self.velocity = 0"""


        # need a draw()
    def draw(self, screen):
        screen.blit(self.image,self.rect)
    def border(self, x, y):
        if x < 0:
            x = 0
        elif x > self.screenwidth - self.rect.x:
            x = self.screenwidth - self.rect.x
        elif y < 0:
            y=0
        elif y > self.screenheight - self.rect.y:
            y = self.screenheight - self.rect.y
    def location(self):
        return(self.x, self.y)
    def shoot(self):
        return Cannonball(self.screen, self.x, self.y, self.theta)




