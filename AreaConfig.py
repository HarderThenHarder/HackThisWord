"""
@author: P_k_y
"""
from Country import Country


class AreaConfig:

    def __init__(self, scale):
        self.country_list = []

        countryA = Country("A", [1620 * scale, 350 * scale], scale)
        self.country_list.append(countryA)
        countryB = Country("B", [850 * scale, 900 * scale], scale)
        self.country_list.append(countryB)


