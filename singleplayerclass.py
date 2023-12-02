import pygame
import sys
from ship import Ship
from effect import Effects
from cannonball import Cannonball
from npc import Npc

class SinglePlayer:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Constants
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.FPS = 60
        self.velocity1 = 0
        self.theta1 = 0
        self.velocity2 = 0
        self.theta2 = 0
        self.shots_fired = 0
        self.sshots_fired = 0
        self.score = 0

        # Create the screen
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Pirate Battle")
        self.clock = pygame.time.Clock()
        self.running = True

        # Init classes
        self.my_ship = Ship(self.screen, self.theta1, self.velocity1, 'pirate_pack/ships/ship (5).png')
        self.npcs = Npc(self.screen, 'pirate_pack/ships/ship (4).png', self.my_ship)
        self.my_game = Effects(self.screen)
        self.ball_group = pygame.sprite.Group()
        self.npc_ball_group = pygame.sprite.Group()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.theta1 -= 3
        elif keys[pygame.K_LEFT]:
            self.theta1 += 3
        elif keys[pygame.K_UP]:
            self.velocity1 = 1.5
        elif keys[pygame.K_DOWN]:
            self.velocity1 = -1.5
        elif keys[pygame.K_k]:
            if not self.shots_fired:
                kill_theta = self.theta1 - 90
                x1 = self.my_ship.rect.centerx
                y1 = self.my_ship.rect.centery
                self.ball_group.add(Cannonball(self.screen, x1, y1, kill_theta))
                self.my_game.cannon_boom()
                self.shots_fired = True
        elif keys[pygame.K_l]:
            if not self.shots_fired:
                kill_theta = self.theta1 + 90
                x1 = self.my_ship.rect.centerx
                y1 = self.my_ship.rect.centery
                self.ball_group.add(Cannonball(self.screen, x1, y1, kill_theta))
                self.my_game.cannon_boom()
                self.shots_fired = True
        else:
            self.theta1 = self.theta1
            self.velocity1 = 0
            self.shots_fired = 0


    def update_game(self):
        # Attack player-controlled ship if it is within a certain radius.
        self.npcs.attack(self.npcs, self.my_ship, self.npc_ball_group)


        # Tile background
        self.my_game.background()

        # Update both cannonball groups before updating ships.
        # Update first ball group
        self.ball_group.update()
        self.ball_group.draw(self.screen)

        # Update second ball group
        self.npc_ball_group.update()
        self.npc_ball_group.draw(self.screen)

        # Update first sprite
        self.my_ship.update(self.velocity1, self.theta1, self.my_ship, self.npc_ball_group)
        self.my_ship.draw(self.screen)

        self.npcs.npc_update(self.npcs, self.ball_group)
        self.npcs.draw(self.screen)

        # Kill cannonball sprites after first contact.
        collisions = pygame.sprite.spritecollide(self.my_ship, self.npc_ball_group, True)
        for i in collisions:
            i.kill()
            self.score -=3
        collisions2 = pygame.sprite.spritecollide(self.npcs, self.ball_group, True)
        for i in collisions2:
            i.kill()
            self.score += 3

        # displays game score
        self.my_game.display_score1(self.screen, self.score)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        self.clock.tick(self.FPS)

    def run(self):
        self.my_game.music()
        while self.running:
            self.handle_events()
            self.handle_input()
            self.update_game()

        # Quit Pygame
        pygame.quit()
        sys.exit()


