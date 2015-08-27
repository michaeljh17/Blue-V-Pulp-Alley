import unittest
import os
import sys
from league_model import *
from league import *
from character import *
from FilerModule.FilerModule import *
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if path not in sys.path:
    sys.path.insert(1, path)
del path


class MainTests(unittest.TestCase):

    def setUp(self):
        self.lm = LeagueModel()
        self.lm.add_league("Test League")
        self.cl = self.lm.get_current_league()
        self.fm = FilerModule()
        self.lm.set_abilities_file(self.fm.read_file("..\Abilities.txt"))

    def test_01(self):
        print("Test 01 - Add Leader with incorrect health")
        self.cl.add_character("Bruce", char_type="Leader", health="d8",
                              brawl="3d10", shoot="2d10", dodge="3d8",
                              might="3d10", finesse="2d10", cunning="3d8",
                              arg1="Mighty", arg2="Brash", arg3="Crafty")

        self.assertTrue(self.cl.find_character("Bruce") == None)

    def test_02(self):
        print("Test 02 - Add Leader with - incorrect dice type")
        self.cl.add_character("Bruce", char_type="Leader", health="d10",
                              brawl="3d8", shoot="2d10", dodge="3d8",
                              might="3d10", finesse="2d10", cunning="3d8",
                              arg1="Mighty", arg2="Brash", arg3="Crafty")

        self.assertTrue(self.cl.find_character("Bruce") == None)


if __name__ == "__main__":
    unittest.main()
