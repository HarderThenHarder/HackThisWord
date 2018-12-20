"""
@author: P_k_y
"""
import pygame

from Defender import Defender
from Hacker import Hacker
import random


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
        self.defender_list = []
        self.red_defender_num = random.randint(0, 5)
        self.green_defender_num = random.randint(0, 5)
        self.blue_defender_num = random.randint(0, 5)
        self.create_defender_group()

    def create_hacker_group(self):
        for i in range(10):
            hacker = Hacker(self, self.scale)
            self.hacker_list.append(hacker)

    def create_defender_group(self):
        for i in range(self.red_defender_num):
            defender = Defender("RED", self, self.scale, (200, 0, 0), 0.5)
            self.defender_list.append(defender)
        for i in range(self.green_defender_num):
            defender = Defender("GREEN", self, self.scale, (0, 200, 0), 0.3)
            self.defender_list.append(defender)
        for i in range(self.blue_defender_num):
            defender = Defender("BLUE", self, self.scale, (0, 0, 200), 0.1)
            self.defender_list.append(defender)

    def update(self, *args):
        pass



