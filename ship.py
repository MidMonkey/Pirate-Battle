import random
import pygame
from math import sin, cos, pi

class Ship(pygame.sprite.Sprite):
    def __init__(self,screen, theta, velocity, path):
        super().__init__()
        #  init sprite variables
        self.path = path
        self.image = pygame.image.load(self.path)
        self.og_image = pygame.image.load(self.path)
        #self.og_image = pygame.transform.scale(self.image, (20, 50))
        #self.og_image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = self.image.get_width()
        self.rect.y = self.image.get_height()
        self.theta = random.randrange(0,360)
        self.velocity = 0 # in pixels per second
        self.x, self.y = [200,200] # Coordinates of the upper left corner.
        self.rect.center = [self.x, self.y]
        # init screen variables
        self.screen = screen
        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()
        # set a random postions. This is especially usefull in the multiplayer mode.
        self.x = random.randrange(0, self.screenwidth)
        self.y = random.randrange(0, self.screenheight)

        # setup health variables
        self.life = 100
        self.hit = 0




    def update(self, velocity, theta,me, enemy_cannonball_group):
        #self.update_controls()
        self.update_looks(velocity, theta)
        self.ship_update(velocity, theta)
        self.check_hits(me, enemy_cannonball_group)



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

        if self.x == max(0, min(self.x, self.screenwidth)):
            self.theta = self.theta
        if self.y == max(0, min(self.y, self.screenheight)):
            self.theta = self.theta
        # needs to calculate new x and y
        # update the rectangle

        self.rect.center = (self.x, self.y)


    def draw(self, screen):
        screen.blit(self.image,self.rect)

    # define the edges of the screen and keep the ship from going off of the screen
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
    def check_hits(self, me, enemy_cannonball_group):
        if pygame.sprite.spritecollideany(me, enemy_cannonball_group):
            self.take_damage()

    def take_damage(self):
        self.life = self.life - 5
        self.life = self.life
        print(self.life)


    def update_looks(self, velocity, theta):
        if self.path == 'pirate_pack/ships/ship (5).png':
            if 100 >= self.life > 60:
                self.image = pygame.image.load('pirate_pack/ships/ship (5).png')
            elif 60 >= self.life > 30:
                self.image = pygame.image.load('pirate_pack/ships/ship (11).png')
            elif 30 >= self.life > 1:
                self.image = pygame.image.load('pirate_pack/ships/ship (17).png')
            elif self.life <= 0:
                self.image = pygame.image.load('pirate_pack/ships/ship (23).png')
        elif self.path == 'pirate_pack/ships/ship (3).png':
            if 100 >= self.life > 50:
                self.image = pygame.image.load('pirate_pack/ships/ship (3).png')
            elif 50 >= self.life > 30:
                self.image = pygame.image.load('pirate_pack/ships/ship (9).png')
            elif 30 >= self.life > 1:
                self.image = pygame.image.load('pirate_pack/ships/ship (15).png')
            elif self.life <= 0:
                self.image = pygame.image.load('pirate_pack/ships/ship (21).png')

        # Scale and rotate the image
        self.og_image = pygame.transform.scale(self.image, (40, 80))
        self.og_image = pygame.transform.rotate(self.og_image, 90)
        # Update the ship
        self.ship_update(velocity, theta)

