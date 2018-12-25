"""
@author: P_k_y
"""


class DataBase:

    def __init__(self):
        self.defender_coefficient = [0, 0, 0]

    def update_coefficient(self, defender_num_list, duration_time):
        if duration_time == [-1, -1]:
            duration_time_num = 0
        else:
            duration_time_num = duration_time[0] * 60 + duration_time[1]

        for i in range(len(self.defender_coefficient)):
            self.defender_coefficient[i] += (duration_time_num * defender_num_list[i] / sum(defender_num_list))
        # normalized coefficient
        total_num = sum(self.defender_coefficient)
        if total_num:
            for i in range(len(self.defender_coefficient)):
                self.defender_coefficient[i] /= total_num


if __name__ == "__main__":
    data_base = DataBase()
    data_base.update_coefficient([3, 2, 7], 18)
    data_base.update_coefficient([3, 16, 2], 38)

    print(data_base.defender_coefficient)
