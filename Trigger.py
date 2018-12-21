"""
@author: P_k_y
"""


class Trigger:

    def __init__(self, timer, area_config):
        self.timer = timer
        self.area_config = area_config
        self.last_time = [timer.get_minute(), timer.get_second()]

    def second_update(self):
        for defender in self.area_config.site_list[1].defender_list:
            defender.kill_intruder(self.area_config.site_list[0].hacker_list)

    def normal_update(self, interval):
        # Reset target
        # if interval < len(self.area_config.site_list[0].hacker_list):
        #     self.area_config.site_list[0].hacker_list[interval].set_target(self.area_config.site_list[1])
        all_hacker_has_no_target = True
        for hacker in self.area_config.site_list[0].hacker_list:
            if hacker.target:
                all_hacker_has_no_target = False
        if all_hacker_has_no_target:
            for hacker in self.area_config.site_list[0].hacker_list:
                hacker.set_target(self.area_config.site_list[1])

        # update Hacker
        for hacker in self.area_config.site_list[0].hacker_list:
            hacker.update()

        # update Site
        for site in self.area_config.site_list:
            site.update()

    def update(self, interval):
        now = [self.timer.get_minute(), self.timer.get_second()]
        last_time_num = self.last_time[0] * 60 + self.last_time[1]
        now_num = now[0] * 60 + now[1]

        if now_num - last_time_num == 1:
            self.second_update()

        self.normal_update(interval)

        self.last_time = now

class SecondTrigger:

    def __init__(self, timer, area_config):
        self.timer = timer
        self.area_config = area_config

    def update(self):
        # update Defender
        for defender in self.area_config.site_list[1].defender_list:
            defender.kill_intruder(self.area_config.site_list[0].hacker_list)