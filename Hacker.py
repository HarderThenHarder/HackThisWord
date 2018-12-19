"""
@author: P_k_y
"""
import random
import pygame


class Hacker(pygame.sprite.Sprite):

    def __init__(self, country, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([3, 3])
        self.color = (100, 0, 0)
        self.image.fill(self.color)
        self.country = country
        self.HP = 100
        self.target = None
        self.pos = [(country.pos[0] + random.random() * 20 - 10) * scale, (country.pos[1] + random.random() * 20 - 10) * scale]

    def set_target(self, target):
        self.target = target

    def update(self, *args):
        pass

