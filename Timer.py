"""
@author: P_k_y
"""


class Timer:
    def __init__(self):
        self._second = 0
        self._minute = 0
        self._hour = 0

    def elapse_one_second(self):
        self._second += 1
        if self._second == 60:
            self._minute += 1
            self._second = 0
        if self._minute == 60:
            self._hour += 1
            self._minute = 0
        if self._hour == 24:
            self._hour = 0

    def elapse_one_minute(self):
        self._minute += 1
        if self._minute == 60:
            self._hour += 1
            self._minute = 0
        if self._hour == 24:
            self._hour = 0

    def get_second(self):
        return self._second

    def get_minute(self):
        return self._minute

    def get_hour(self):
        return self._hour

    def set_time(self, hour, minute, second):
        self._hour = hour
        self._minute = minute
        self._second = second



