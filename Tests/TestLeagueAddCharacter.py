import sys
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
    sys.path.insert(1, path)
del path
from league import *
from character import *
from league_model import *

lm = LeagueModel()
lm.set_abilities_file(lm.read_file("..\Abilities.txt"))
lm.add_league("Legion")

def check_character_creation(characters_name):
    x = lm.get_current_league().find_character(characters_name)
    if (x == None):
        return False
    else:
        return True
    
def test_character_creation_methods(tests_name, expectation,
                                    ch_name, ch_type, ch_health,
                                    ch_skill_01, ch_skill_02,
                                    ch_skill_03, ch_skill_04,
                                    ch_skill_05, ch_skill_06,
                                    ch_ability_01, ch_ability_02,
                                    ch_ability_03):
    print("Beginning Test: " + tests_name)
    lm.get_current_league().add_character(ch_name, ch_type,
                                          ch_health, ch_skill_01,
                                          ch_skill_02, ch_skill_03,
                                          ch_skill_04, ch_skill_05,
                                          ch_skill_06,
                                          arg1= ch_ability_01,
                                          arg2= ch_ability_02,
                                          arg3= ch_ability_03)
    if check_character_creation(ch_name) == expectation:
        print("End of Test: " + tests_name + " Result - Passed")
    else:
        print("End of Test: " + tests_name + " Result - Failed")
    lm.get_current_league().delete_character_by_name(ch_name)
    print(" ")
        

#print(lm.get_current_league())

test_character_creation_methods("Create a Leader, Happy Day", True,"Bruce",
                                "Leader","d10","3d10","3d10","3d8","3d10",
                                "2d8","2d10","Mighty","Brash","Crafty")

test_character_creation_methods("Create a Leader, Incorrectly Set Skill",
                                False,"Bruce", "Leader","d10","2d10","3d10",
                                "3d8","3d10","2d8","2d10","Mighty","Brash",
                                "Crafty")

test_character_creation_methods("Create a Leader, Incorrectly Set Health",
                                False,"Bruce", "Leader","d8","3d10","3d10",
                                "3d8","3d10","2d8","2d10","Mighty","Brash",
                                "Crafty")


