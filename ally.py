__author__ = 'User'

from character import Character


class Ally(Character):
    level = 2
    size = 2
    base_health = 6
    
    def __init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities):
        Character.__init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities)
