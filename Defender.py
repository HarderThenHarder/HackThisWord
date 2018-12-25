"""
@author: P_k_y
"""
import random
import pygame


class Defender(pygame.sprite.Sprite):

    def __init__(self, name, site, scale, color, kill_probability, database):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.Surface([5, 5])
        self.color = color
        self.image.fill(self.color)
        self.image.set_alpha(0.5*255)
        self.site = site
        self.scale = scale
        self.pos = []
        self.set_pos()
        self.kill_probability = kill_probability
        self.database = database

    def set_pos(self):
        x_offset = random.random() * 40 - 20
        y_offset = random.random() * 40 - 20
        self.pos = [int((self.site.pos[0] + x_offset) * self.scale), int((self.site.pos[1] + y_offset) * self.scale)]

    def kill_intruder(self, hacker_list):
        for hacker in hacker_list:
            rand = random.random()
            if rand < self.kill_probability:
                self.database.update_coefficient([self.site.red_defender_num, self.site.green_defender_num, self.site.blue_defender_num], hacker.duration)
                hacker.be_killed()
                print(self.database.defender_coefficient)

    def update(self, *args):
        pass
