"""
@author: P_k_y
"""
import pygame
from Hacker import Hacker


class Country(pygame.sprite.Sprite):

    def __init__(self, name, pos, scale):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.name = name
        self.pos = pos
        self.image = pygame.Surface([int(10 * scale), int(10 * scale)])
        self.color = (0, 131, 114)
        self.image.fill(self.color)
        self.hacker_list = []
        self.create_hacker_group()

    def create_hacker_group(self):
        for i in range(20):
            hacker = Hacker(self, self.scale)
            self.hacker_list.append(hacker)

    def update(self, *args):
        pass



