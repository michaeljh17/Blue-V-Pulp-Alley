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
print("Start of Test: Create new leader - Happy Day")
lm.get_current_league().add_character("Bruce", "Leader","d10","3d10","3d10","3d8","3d10","2d8","2d10",arg1="Mighty",arg2="Brash",arg3="Crafty")

def check_character_creation(characters_name, tests_name):
    x = lm.get_current_league().find_character(characters_name)
    if (x == None):
        print("Creation of the character " + characters_name + " in test: " + tests_name + " was unsuccessful")
    else:
        print("Creation of the character " + characters_name + " in test: " + tests_name + " was successful!")

check_character_creation("Bruce", "Create new leader - Happy Day!")
lm.get_current_league().delete_character_by_name("Bruce")
#print(lm.get_current_league())

print("\nStart of Test: Create new leader - Incorrectly set dice")
lm.get_current_league().add_character("Bruce", "Leader","d10","2d10","3d10","3d8","3d10","2d8","2d10",arg1="Mighty",arg2="Brash",arg3="Crafty")
check_character_creation("Bruce", "Create new leader - Incorrectly set dice")
lm.get_current_league().delete_character_by_name("Bruce")

print("\nStart of Test: Create new leader - Incorrectly set dice")
lm.get_current_league().add_character("Bruce", "Leader","d10","2d10","3d10","3d8","3d10","2d8","2d10",arg1="Mighty",arg2="Brash",arg3="Crafty")
check_character_creation("Bruce", "Create new leader - Incorrectly set dice")
lm.get_current_league().delete_character_by_name("Bruce")



