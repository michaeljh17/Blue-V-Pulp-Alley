__author__ = 'mih279'

from character import Character

class Follower(Character):
    def __init__(self, name, health="", brawl="", shoot="", dodge="", might="", finesse="", cunning=""):
        Character.__init__(self, name, health, brawl, shoot, dodge, might, finesse, cunning)