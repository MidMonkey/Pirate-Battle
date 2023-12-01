import random
import pygame
from ship import Ship
from math import sin, cos, pi, sqrt, atan2
from cannonball import Cannonball
from effect import Effects
class Npc(Ship):
    def __init__(self, screen, path, enemy_ship):
        # Set default values for velocity and theta
        # Call the constructor of the parent class (Ship)
        self.path = path
        self.image = pygame.image.load(self.path)
        self.og_image = self.image
        self.velocity = 2
        self.theta = random.randrange(0, 360)
        self.attack_cooldown = 200
        self.last_attack_time = 0
        self.enemy_ship = enemy_ship
        super().__init__(screen, self.theta, self.velocity, self.path)
        self.screenwidth = self.screen.get_width()
        self.screenheight = self.screen.get_height()
        self.kill_radius = 200
        self.life = 100
        self.my_game = Effects(self.screen)
        self.npc_ball_group = pygame.sprite.Group()
        self.gun_timer = 0
    def npc_update(self, me, enemy_cannonball_group):
        self.npc_ship_update()
        self.npc_ball_group.update()
        self.check_hits(me, enemy_cannonball_group)
        self.npc_update_looks(2,self.theta)

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
    def attack(self,sprite1, sprite2, ball_group):
            coord1 = sprite1.rect.center
            x1, y1 = coord1
            coord2 = sprite2.rect.center
            x2, y2 = coord2
            distance = sqrt((x2-x1)**2+(y2-y1)**2)
            angle_radians = atan2(y2 - y1, x2 - x1)
            print(angle_radians)
            kill_theta = self.theta - 49
            kill_theta1 = kill_theta - 90
            kill_theta2 = kill_theta + 90
            x3 = self.rect.centerx
            y3 = self.rect.centery
            self.gun_timer = pygame.time.get_ticks()
            # if pygame.time.get_ticks() - self.gun_timer >= 100:
            current_time = pygame.time.get_ticks()
            print()
            if current_time - self.last_attack_time >= self.attack_cooldown:
                if distance <= self.kill_radius:
                    print('attack')
                    ball_group.add(Cannonball(self.screen, x3, y3, kill_theta2))
                    ball_group.add(Cannonball(self.screen, x3, y3, kill_theta1))
                    self.my_game.cannon_boom()
                    self.last_attack_time = current_time
                    self.npc_ball_group.draw(self.screen)

    def npc_update_looks(self, velocity, theta):
        if 100 >= self.life > 60:
            self.image = pygame.image.load('pirate_pack/ships/ship (4).png')
        elif 60 >= self.life > 30:
            self.image = pygame.image.load('pirate_pack/ships/ship (10).png')
        elif 30 >= self.life > 1:
            self.image = pygame.image.load('pirate_pack/ships/ship (16).png')
        elif self.life <= 0:
            self.image = pygame.image.load('pirate_pack/ships/ship (22).png')

        # Scale and rotate the image
        self.og_image = pygame.transform.scale(self.image, (40, 80))
        self.og_image = pygame.transform.rotate(self.og_image, 40)
        # Update the ship
        self.ship_update(2, self.theta)
