__author__ = 'User'

from character import Character


class Ally(Character):
    def __init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, *abilities):
        Character.__init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, abilities)
