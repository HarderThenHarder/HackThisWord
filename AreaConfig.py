"""
@author: P_k_y
"""
from Site import Site


class AreaConfig:

    def __init__(self, scale, timer, database):
        self.site_list = []

        siteA = Site("A", [1620 * scale, 350 * scale], scale, timer, database)
        self.site_list.append(siteA)
        siteB = Site("B", [850 * scale, 900 * scale], scale, timer, database)
        self.site_list.append(siteB)


