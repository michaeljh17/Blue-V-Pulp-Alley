__author__ = 'User'

from character import Character


class Ally(Character):
    def __init__(self, name, health="", brawl="", shoot="", dodge="", might="", finesse="", cunning=""):
        Character.__init__(self, name, health, brawl, shoot, dodge, might, finesse, cunning)
