__author__ = 'mih279'

from character import Character
from edice import *


class SideKick(Character):
    level = 3
    size = 3
    base_health = 8
    
    def __init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities):
        Character.__init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities)
        if health != self.baseHealth:
            print("you smell")
