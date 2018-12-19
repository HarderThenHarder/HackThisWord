"""
@author: P_k_y
"""


class Trigger:

    def __init__(self, timer, area_config):
        self.timer = timer
        self.area_config = area_config

    def update(self):
        second = self.timer.get_second()
        self.area_config.country_list[0].hacker_list[second].set_target(self.area_config.country_list[1])

