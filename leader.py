__author__ = 'mih279'

from character import Character


class Leader(Character):
    level = 4
    size = 0
    base_health = 10
    
    def __init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities):
        Character.__init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities)
