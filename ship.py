import pygame
import sys
from math  import sin, cos, pi


class Ship(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        #  init sprite variables
        self.image = pygame.image.load("pirate_pack/ships/ship (1).png")
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

        # init cannonball variables
        self.ball = pygame.image.load("pirate_pack/Ship parts/cannonBall.png")
        self.ballpos = self.rect.center
        self.ball.rect = self.ball.get_rect()
        self.ball.rect.x = self.ball.get_width()
        self.ball.rect.y = self.ball.get_height()
    def update(self):
        self.update_controls()
        self.ship_update()
        self.update_balls()
    def ship_update(self):
        self.border(self.x, self.y)
        # needs to update image and rect based off of new theta
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
        self.ballpos = self.rect.center
    def update_balls(self):
        # needs to shoot off a cannonball at a perpendicular to the ships direction.
        ballx, bally = self.ballpos
        deg_rad = pi / 180
        ball_theta = self.theta + 90
        ballx += self.velocity * cos(ball_theta * deg_rad)
        bally -= self.velocity * sin(ball_theta * deg_rad)
    def update_controls(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.theta -= 3
        elif keys[pygame.K_LEFT]:
            self.theta += 3  # may want to use a variable
        elif keys[pygame.K_UP]:
            self.velocity = 5
        elif keys[pygame.K_DOWN]:
            self.velocity = -5
        elif keys[pygame.K_k]:
            self.shoot(self.screen)
        else:
            self.theta = self.theta
            self.velocity = 0

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
    def shoot(self, screen):
        ball_group = []
        screen.blit(self.ball, self.ballpos)



