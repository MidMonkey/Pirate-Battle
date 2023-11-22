import pygame
from cannonball import Cannonball
from ship import Ship
from effect import Effects
class Controls():
    def __init__(self, screen, velocity, theta):
        self.theta = theta
        self.velocity = velocity
        self.shots_fired = False
        self.sshots_fired = False
        self.screen = screen
        self.velocity1 = 0
        self.theta1 = 0
        self.velocity2 = 0
        self.theta2 = 0
        self.my_ship = Ship(self.screen, self.theta1, self.velocity1)
        self.your_ship = Ship(self.screen, self.theta2, self.velocity2)
        self.my_game = Effects(screen)
        self.ball_group = pygame.sprite.Group()
        self.your_ball_group = pygame.sprite.Group()

    def player1_controls(self, keys):
        if keys[pygame.K_RIGHT]:
            self.theta -= 3
        elif keys[pygame.K_LEFT]:
            self.theta += 3
        elif keys[pygame.K_UP]:
            self.velocity = 2
        elif keys[pygame.K_DOWN]:
            self.velocity = -2
        elif keys[pygame.K_k]:
            if not self.shots_fired:
                kill_theta = self.theta - 90
                x1 = self.my_ship.rect.centerx
                y1 = self.my_ship.rect.centery
                self.ball_group.add(Cannonball(self.screen, x1, y1, kill_theta))
                self.my_game.cannon_boom()
                self.shots_fired = True
        elif keys[pygame.K_l]:
            if not self.shots_fired:
                kill_theta = self.theta + 90
                x1 = self.my_ship.rect.centerx
                y1 = self.my_ship.rect.centery
                self.ball_group.add(Cannonball(self.screen, x1, y1, kill_theta))
                self.my_game.cannon_boom()
                self.shots_fired = True
        else:
            self.theta = self.theta
            self.velocity = 0
            self.shots_fired = 0
        self.my_ship.update(self.velocity, self.theta, self.my_ship, self.your_ball_group)


    def player2_controls(self, keys):
        if keys[pygame.K_d]:
            self.theta -= 3
            print(self.theta)
        elif keys[pygame.K_a]:
            self.theta += 3
            print(self.theta)
        elif keys[pygame.K_w]:
            self.velocity = 2
            print(self.velocity)
        elif keys[pygame.K_s]:
            self.velocity = -2
            print(self.velocity)
        elif keys[pygame.K_q]:
            if not self.sshots_fired:
                kill_theta = self.theta - 90
                x2 = self.your_ship.rect.centerx
                y2 = self.your_ship.rect.centery
                self.your_ball_group.add(Cannonball(self.screen, x2, y2, kill_theta))
                self.my_game.cannon_boom()
                self.sshots_fired = True
        elif keys[pygame.K_e]:
            if not self.sshots_fired:
                kill_theta = self.theta + 90
                x2 = self.your_ship.rect.centerx
                y2 = self.your_ship.rect.centery
                self.your_ball_group.add(Cannonball(self.screen, x2, y2, kill_theta))
                self.my_game.cannon_boom()
                self.sshots_fired = True
        else:
            self.theta = self.theta
            self.velocity = 0
            self.sshots_fired = 0
        self.your_ship.update(self.velocity, self.theta, self.your_ship, self.ball_group)

