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
        self.width = 10
        self.height = 10
        self.image = pygame.Surface([int(self.width * scale), int(self.height * scale)])
        self.pos = pos
        self.center = [int(self.pos[0] + self.width / 2 * scale), int(self.pos[1] + self.height / 2 * scale)]
        self.color = (100, 0, 0)
        self.image.fill(self.color)
        self.hacker_list = []
        self.create_hacker_group()

    def create_hacker_group(self):
        for i in range(20):
            hacker = Hacker(self, self.scale)
            self.hacker_list.append(hacker)

    def update(self, *args):
        pass



