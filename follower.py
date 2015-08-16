__author__ = 'mih279'

from character import Character


class Follower(Character):
    level = 1
    size = 1
    base_health = 6
    
    def __init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities):
        Character.__init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities)
