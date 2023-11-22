import pygame
import sys
from ship import Ship
from effect import Effects
from cannonball import Cannonball
from control import Controls

class PirateBattle:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Constants
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.FPS = 60

        # Create the screen
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Pirate Battle")

        # Other member variables
        self.velocity1 = 0
        self.theta1 = 0
        self.velocity2 = 0
        self.theta2 = 0
        self.shots_fired = 0
        self.sshots_fired = 0

        # init classes
        self.your_ship = Ship(self.screen, self.theta2, self.velocity2, 'pirate_pack/ships/ship (3).png')
        self.my_ship = Ship(self.screen, self.theta1, self.velocity1, 'pirate_pack/ships/ship (5).png')
        self.my_game = Effects(self.screen)
        self.ball_group = pygame.sprite.Group()
        self.your_ball_group = pygame.sprite.Group()

    def run(self):
        # Plays the game soundtrack
        self.my_game.music()

        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            self.handle_controls(keys)
            self.update_sprites()
            self.check_collisions()

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            clock.tick(self.FPS)

        # Quit Pygame
        pygame.quit()
        sys.exit()

    def handle_controls(self, keys):
        # Handle controls for player 1
        if keys[pygame.K_RIGHT]:
            self.theta1 -= 3
        elif keys[pygame.K_LEFT]:
            self.theta1 += 3
        elif keys[pygame.K_UP]:
            self.velocity1 = 2
        elif keys[pygame.K_DOWN]:
            self.velocity1 = -2
        elif keys[pygame.K_k]:
            if not self.shots_fired:
                self.fire_cannon(90)
        elif keys[pygame.K_l]:
            if not self.shots_fired:
                self.fire_cannon(-90)
        else:
            self.theta1 = self.theta1
            self.velocity1 = 0
            self.shots_fired = 0

        # Handle controls for player 2
        if keys[pygame.K_d]:
            self.theta2 -= 3
        elif keys[pygame.K_a]:
            self.theta2 += 3
        elif keys[pygame.K_w]:
            self.velocity2 = 2
        elif keys[pygame.K_s]:
            self.velocity2 = -2
        elif keys[pygame.K_h]:
            if not self.sshots_fired:
                self.fire_enemy_cannon(90)
        elif keys[pygame.K_g]:
            if not self.sshots_fired:
                self.fire_enemy_cannon(-90)
        else:
            self.theta2 = self.theta2
            self.velocity2 = 0
            self.sshots_fired = 0

    def update_sprites(self):
        # Tile background
        self.my_game.background()

        # Update both cannonball groups before updating ships.
        # Update first ball group
        self.ball_group.update()
        self.ball_group.draw(self.screen)

        # Update second ball group
        self.your_ball_group.update()
        self.your_ball_group.draw(self.screen)

        # Update first sprite
        self.my_ship.update(self.velocity1, self.theta1, self.my_ship, self.your_ball_group)
        self.my_ship.draw(self.screen)

        # Update second sprite
        self.your_ship.update(self.velocity2, self.theta2, self.your_ship, self.ball_group)
        self.your_ship.draw(self.screen)

    def check_collisions(self):
        # Kill cannonball sprites after first contact.
        collisions = pygame.sprite.spritecollide(self.my_ship, self.your_ball_group, True)
        for i in collisions:
            i.kill()

        collisions2 = pygame.sprite.spritecollide(self.your_ship, self.ball_group, True)
        for i in collisions2:
            i.kill()

    def fire_cannon(self, angle):
        kill_theta = self.theta1 + angle
        x1 = self.my_ship.rect.centerx
        y1 = self.my_ship.rect.centery
        self.ball_group.add(Cannonball(self.screen, x1, y1, kill_theta))
        self.my_game.cannon_boom()
        self.shots_fired = True

    def fire_enemy_cannon(self, angle):
        kill_theta2 = self.theta2 + angle
        x2 = self.your_ship.rect.centerx
        y2 = self.your_ship.rect.centery
        self.your_ball_group.add(Cannonball(self.screen, x2, y2, kill_theta2))
        self.my_game.cannon_boom()
        self.sshots_fired = True

if __name__ == "__main__":
    game = PirateBattle()
    game.run()
