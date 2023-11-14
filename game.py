import pygame
from math  import sin, cos, pi


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pirate_pack/Ships/ship (1).png")
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.theta = 0
        self.velocity = 2 # in pixels per second
        self.x, self.y = [0,0] # Coordinates of the upper left corner.
        self.rect.center = [self.x, self.y]
        self.og_image = self.image
        # needs image
        # needs rect

        # need update()
        def update():
            # needs to update image and rect based off of new theta
            self.image = pygame.transform.rotate(self.og_image, self.theta)
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)

            deg_rad = pi/180
            self.x += self.velocity * cos(self.theta * deg_rad)
            self.y -= self.velocity * sin(self.theta * deg_rad)
            # needs to calculate new x and y
            pass
        # need a draw()
        def draw(self, screen):
            screen.blit(self.image, self.rect)
            print(self.rect)
        def controls(self):
            keys = pygame.key.get_pressed
            if keys[pygame.K_RIGHT]:
                my_ship.theta -= 5
            if keys[pygame.K_LEFT]:
                my_ship.theta += 5  # may want to use a variable
            if keys[pygame.K_UP]:
                my_ship.velocity += 1
            if keys[pygame.K_DOWN]:
                my_ship.velocity -= 1
        def check_collision(self, screen):
            if self.x > self.screen.get_width

        """ In game 
        # make a car class 
        my_ship = Car()
        # in the loop
        my_car.update()
        my_ship.blit(screen)"""

        """using keys 
        keys = pygame.key.get_pressed
        if keys[pygame.k_RIGHT]:
            my_ship.theta -=5 
        if keys[pygame.k_LEFT]:
            my_ship.theta +=5 # may want to use a variable 
        if event.key == pygame.k_UP:
            my_ship.velocity += 1 
        if event.key == pygame.k_DOWN:
            my_ship.velocity -= 1
            """

