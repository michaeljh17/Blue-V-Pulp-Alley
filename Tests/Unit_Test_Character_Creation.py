import unittest
import os
import sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if path not in sys.path:
    sys.path.insert(1, path)
del path
from league_model import *
from league import *
from character import *


class MainTests(unittest.TestCase):

    def setUp(self):
        self.lm = LeagueModel()
        self.lm.add_league("Test League")
        self.lm.set_abilities_file(self.lm.read_file("..\Abilities.txt"))

    def test_01(self):
        print("Test 01 - With all slots full can a new character be created")
        self.lm.get_current_league().add_character("Bruce", char_type="Leader",
                                                   health="d10", brawl="3d10",
                                                   shoot="2d10", dodge="3d8",
                                                   might="3d10",
                                                   finesse="2d10",
                                                   cunning="3d8",
                                                   arg1="Mighty", arg2="Brash",
                                                   arg3="Crafty")

        self.lm.get_current_league().add_character("SideKick01", char_type="SideKick", health="d8",
                                                   brawl="2d6", shoot="3d6", dodge="2d6",
                                                   might="3d8", finesse="2d8",
                                                   cunning="3d8", arg1="Mighty",
                                                   arg2="Brash", arg3="")

        self.lm.get_current_league().add_character("Ally01", char_type="Ally", health="d6",
                                                   brawl="2d6", shoot="2d6", dodge="1d6",
                                                   might="1d6", finesse="1d6", cunning="1d6",
                                                   arg1="Mighty", arg2="",
                                                   arg3="")

        self.lm.get_current_league().add_character("Ally02", char_type="Ally", health="d6",
                                                   brawl="2d6", shoot="2d6", dodge="1d6",
                                                   might="1d6", finesse="1d6", cunning="1d6",
                                                   arg1="Mighty", arg2="",
                                                   arg3="")

        self.lm.get_current_league().add_character("Ally03", char_type="Ally", health="d6",
                                                   brawl="2d6", shoot="2d6", dodge="1d6",
                                                   might="1d6", finesse="1d6", cunning="1d6",
                                                   arg1="Mighty", arg2="",
                                                   arg3="")

if __name__ == "__main__":
    unittest.main()
