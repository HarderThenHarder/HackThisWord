"""
@author: P_k_y
"""
import random



class Trigger:

    def __init__(self, timer, area_config, database):
        self.timer = timer
        self.area_config = area_config
        self.database = database
        self.last_time = [timer.get_minute(), timer.get_second()]
        self.counter = 0

    def choose_target(self):
        max_score = self.area_config.site_list[1].red_defender_num * self.database.defender_coefficient[0] + \
                    self.area_config.site_list[1].green_defender_num * self.database.defender_coefficient[1] + \
                    self.area_config.site_list[1].blue_defender_num * self.database.defender_coefficient[2]
        next_target = self.area_config.site_list[1]

        for target in self.area_config.site_list:
            tmp_score = target.red_defender_num * self.database.defender_coefficient[0] + \
                        target.green_defender_num * self.database.defender_coefficient[1] + \
                        target.blue_defender_num * self.database.defender_coefficient[2]
            if max_score < tmp_score:
                max_score = tmp_score
                next_target = target

        return next_target

    def random_choose_target(self):
        rand = random.randint(0, len(self.area_config.site_list) - 1)
        return self.area_config.site_list[rand]

    def second_update(self):
        for site in self.area_config.site_list:
            if site.who_is_attacking_me:
                for defender in site.defender_list:
                    defender.kill_intruder(site.who_is_attacking_me)

    def normal_update(self, interval):
        # Reset target
        # if interval < len(self.area_config.site_list[0].hacker_list):
        #     self.area_config.site_list[0].hacker_list[interval].set_target(self.area_config.site_list[1])

        # if all hacker has no target, launch a new attack
        for site in self.area_config.site_list:
            all_hacker_has_no_target = True
            for hacker in site.hacker_list:
                if hacker.target:
                    all_hacker_has_no_target = False
            if all_hacker_has_no_target:
                for hacker in site.hacker_list:
                    if random.random() > 0.1:
                        hacker.set_target(self.choose_target())
                    else:
                        hacker.set_target(self.random_choose_target())

        # update Hacker
        for site in self.area_config.site_list:
            for hacker in site.hacker_list:
                hacker.update()

        # update Site
        for site in self.area_config.site_list:
            site.update()

    def update(self, interval):
        now = [self.timer.get_minute(), self.timer.get_second()]
        last_time_num = self.last_time[0] * 60 + self.last_time[1]
        now_num = now[0] * 60 + now[1]

        # per second update
        if now_num - last_time_num == 1:
            self.second_update()
            self.counter += 1

        # 20 seconds is an iteration
        if self.counter == 20:
            self.area_config.site_list[1].reset_defender_group()
            # kill all hackers
            for hacker in self.area_config.site_list[0].hacker_list:
                hacker.retreat()
            self.counter = 0

        self.normal_update(interval)
        self.last_time = now
