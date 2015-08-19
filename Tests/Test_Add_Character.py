import sys
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
    sys.path.insert(1, path)
del path
from league import *
from character import *
from league_model import *

class Test_Add_Character(object):
    
    def __init__(self):
        self.lm = LeagueModel()
        self.lm.add_league("Test League")
        self.lm.set_abilities_file(self.lm.read_file("..\Abilities.txt"))


    def check_character_creation(self, characters_name):
        x = self.lm.get_current_league().find_character(characters_name)
        if (x == None):
            return False
        else:
            return True
        
    def add_bruce(self):
        self.lm.get_current_league().add_character("L", char_type="Leader", health="d10",
                                      brawl="3d10", shoot="2d10", dodge="3d8",
                                      might="3d10", finesse="2d10",
                                      cunning="3d8", arg1="Mighty",
                                      arg2="Brash", arg3="Crafty")
        
    def check_character_creation_methods(self, tests_name, expectation, name, char_type, health, brawl,
                      shoot, dodge, might, finesse,
                      cunning, *abilities):
        print("Beginning Test: " + tests_name)
        self.lm.get_current_league().add_character(name, char_type, health, brawl,
                      shoot, dodge, might, finesse,
                      cunning, arg1 = abilities[0], arg2 = abilities[1], arg3 = abilities[2])
        if self.check_character_creation(name) == expectation:
            print("End of Test: " + tests_name + " Result - Passed")
        else:
            print("End of Test: " + tests_name + " Result - Failed")
        self.lm.get_current_league().delete_character_by_name(name)
        print(" ")