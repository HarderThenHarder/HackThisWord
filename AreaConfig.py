"""
@author: P_k_y
"""
from Site import Country


class AreaConfig:

    def __init__(self, scale):
        self.site_list = []

        siteA = Country("A", [1620 * scale, 350 * scale], scale)
        self.site_list.append(siteA)
        siteB = Country("B", [850 * scale, 900 * scale], scale)
        self.site_list.append(siteB)


