import pygame
def update_looks(self, velocity, theta, path):
    self.path = path
    if self.path == 'pirate_pack/ships/ship (5).png':
        if 100 >= self.life > 60:
            self.image = pygame.image.load('pirate_pack/ships/ship (5).png')
            self.og_image = pygame.image.load('pirate_pack/ships/ship (5).png')
            self.og_image = pygame.transform.scale(self.image, (20, 50))
            self.og_image = pygame.transform.rotate(self.image, 90)
            # self.rect.center = (self.x, self.y)
            self.ship_update(velocity, theta)
        elif 60 >= self.life > 30:
            self.image = pygame.image.load('pirate_pack/ships/ship (11).png')
            self.og_image = pygame.image.load('pirate_pack/ships/ship (11).png')
            self.og_image = pygame.transform.scale(self.image, (20, 50))
            self.og_image = pygame.transform.rotate(self.image, 90)
            # self.rect.center = (self.x, self.y)
            self.ship_update(velocity, theta)
        elif 30 >= self.life > 1:
            self.image = pygame.image.load('pirate_pack/ships/ship (17).png')
            self.og_image = pygame.image.load('pirate_pack/ships/ship (17).png')
            self.og_image = pygame.transform.scale(self.image, (20, 50))
            self.og_image = pygame.transform.rotate(self.image, 90)
            # self.rect.center = (self.x, self.y)
            self.ship_update(velocity, theta)
        elif self.life <= 0:
            self.image = pygame.image.load('pirate_pack/ships/ship (23).png')
            self.og_image = pygame.image.load('pirate_pack/ships/ship (23).png')
            self.og_image = pygame.transform.scale(self.image, (20, 50))
            self.og_image = pygame.transform.rotate(self.image, 90)
            # self.rect.center = (self.x, self.y)
        # setup for second ship.
        if self.path == 'pirate_pack/ships/ship (3).png':
            if 100 >= self.life > 60:
                self.image = pygame.image.load('pirate_pack/ships/ship (3).png')
                self.og_image = pygame.image.load('pirate_pack/ships/ship (3).png')
                self.og_image = pygame.transform.scale(self.image, (20, 50))
                self.og_image = pygame.transform.rotate(self.image, 90)
                # self.rect.center = (self.x, self.y)
                self.ship_update(velocity, theta)
            elif 60 >= self.life > 30:
                self.image = pygame.image.load('pirate_pack/ships/ship (9).png')
                self.og_image = pygame.image.load('pirate_pack/ships/ship (9).png')
                self.og_image = pygame.transform.scale(self.image, (20, 50))
                self.og_image = pygame.transform.rotate(self.image, 90)
                # self.rect.center = (self.x, self.y)
                self.ship_update(velocity, theta)
            elif 30 >= self.life > 1:
                self.image = pygame.image.load('pirate_pack/ships/ship (15).png')
                self.og_image = pygame.image.load('pirate_pack/ships/ship (15).png')
                self.og_image = pygame.transform.scale(self.image, (20, 50))
                self.og_image = pygame.transform.rotate(self.image, 90)
                # self.rect.center = (self.x, self.y)
                self.ship_update(velocity, theta)
            elif self.life <= 0:
                self.image = pygame.image.load('pirate_pack/ships/ship (21).png')
                self.og_image = pygame.image.load('pirate_pack/ships/ship (21).png')
                self.og_image = pygame.transform.scale(self.image, (20, 50))
                self.og_image = pygame.transform.rotate(self.image, 90)
                # self.rect.center = (self.x, self.y)
