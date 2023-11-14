import pygame
class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, screen):
        super().__init__()
        self.screen = screen
        self.ball = pygame.image.load("pirate_pack/Ship parts/cannonBall.png")
        self.ball_rect = pygame.Surface.get_rect(self.ball)
        self.rect = self.ball.get_rect()
        self.rect.center = pos
        self.speed = 7
    def shoot(self):
        self.screen.blit(self.ball, (self.rect.center))

    def update(self):
        self.rect.x += self.speed