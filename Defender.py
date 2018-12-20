"""
@author: P_k_y
"""
import random
import pygame


class Defender(pygame.sprite.Sprite):

    def __init__(self, name, site, scale, color, kill_probability):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.Surface([5, 5])
        self.color = color
        self.image.fill(self.color)
        self.site = site
        self.pos = [(site.pos[0] + random.random() * 20 - 10) * scale, (site.pos[1] + random.random() * 20 - 10) * scale]
        self.kill_probability = kill_probability

    def update(self, *args):
        pass

