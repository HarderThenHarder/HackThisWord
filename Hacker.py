"""
@author: P_k_y
"""
import random
import pygame


class Hacker(pygame.sprite.Sprite):

    def __init__(self, site, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([3, 3])
        self.color = (100, 0, 0)
        self.image.fill(self.color)
        self.site = site
        self.HP = 100
        self.target = None
        self.pos = [(site.pos[0] + random.random() * 20 - 10) * scale, (site.pos[1] + random.random() * 20 - 10) * scale]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.state = "OFF"
        self.duration = "--:--"

    def set_target(self, target):
        self.target = target
        self.state = "ON "
        self.duration = "00:00"

    def update(self, *args):
        pass

