"""
@author: P_k_y
"""
import random
import pygame


class Hacker(pygame.sprite.Sprite):

    def __init__(self, site, scale, timer):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([3, 3])
        self.site = site
        self.timer = timer
        self.HP = 100
        self.target = None
        self.pos = [(site.pos[0] + random.random() * 20 - 10) * scale, (site.pos[1] + random.random() * 20 - 10) * scale]
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.state = "OFF"
        self.duration = [-1, -1]
        self.start_time = []

    def set_target(self, target):
        self.target = target
        # !!!!!!!!!!!!!! is "ON " ———— with SPACE after !!!!!!!!!!!!!! #
        self.state = "ON "
        self.duration = [0, 0]
        self.start_time = [self.timer.get_minute(), self.timer.get_second()]
        if self.site not in target.who_is_attacking_me:
            target.who_is_attacking_me.append(self.site)

    def be_killed(self):
        self.target = None
        self.state = "OFF"
        self.duration = [-1, -1]

    def retreat(self):
        """
        retreat because target change the defender, so this result don't used for learning
        """
        self.target = None
        self.state = "OFF"
        self.duration = [-1, -1]

    def update(self, *args):
        # !!!!!!!!!!!!!! is "ON " ———— with SPACE after !!!!!!!!!!!!!! #
        if self.state == "ON ":
            now = [self.timer.get_minute(), self.timer.get_second()]
            self.duration = [now[0] - self.start_time[0], now[1] - self.start_time[1]]

