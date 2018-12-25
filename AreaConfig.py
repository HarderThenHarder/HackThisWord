"""
@author: P_k_y
"""
from Site import Site


class AreaConfig:

    def __init__(self, scale, timer, database):
        self.site_list = []

        siteA = Site("A", [1300 * scale, 500 * scale], scale, timer, database)
        self.site_list.append(siteA)
        siteB = Site("B", [850 * scale, 900 * scale], scale, timer, database)
        self.site_list.append(siteB)
        siteC = Site("C", [2020 * scale, 1050 * scale], scale, timer, database)
        self.site_list.append(siteC)
        siteD = Site("D", [1800 * scale, 600 * scale], scale, timer, database)
        self.site_list.append(siteD)
        siteE = Site("E", [2000 * scale, 400 * scale], scale, timer, database)
        self.site_list.append(siteE)
        siteF = Site("F", [950 * scale, 250 * scale], scale, timer, database)
        self.site_list.append(siteF)
        siteG = Site("G", [450 * scale, 600 * scale], scale, timer, database)
        self.site_list.append(siteG)

