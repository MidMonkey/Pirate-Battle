import pygame
from ship import Ship
import random

class Npc(Ship):
    def __init__(self):
        super().__init__()
        self.theta = random.randrange(0,360)
    def bounce(self):
        pass
