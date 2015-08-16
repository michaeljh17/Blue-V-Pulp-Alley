__author__ = 'mih279'

from character import Character
from edice import *


class SideKick(Character):
    baseHealth = EDice.d8.name
    level
    cost/size
    def __init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities):
        Character.__init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities)
        if health != self.baseHealth:
            print("you smell")
