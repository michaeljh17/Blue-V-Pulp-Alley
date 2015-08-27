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
        self.cl.add_character("Bruce", "Leader", "d10", "3d10", "3d10", "3d8",
                              "3d10", "2d8", "2d10", arg1="Mighty",
                              arg2="Brash", arg3="Crafty")
        self.cl.add_character("TestFollower", char_type="Follower",
                              health="d6",
                              brawl="1d6", shoot="1d6", dodge="1d6",
                              might="1d6", finesse="1d6", cunning="1d6",
                              arg1="Mighty", arg2="", arg3="")

    def test_01(self):
        print('Test 01 - Delete a character')
        theCharacter = self.cl.find_character("TestFollower")
        self.cl.remove_character(theCharacter)
        self.assertTrue(self.cl.find_character("TestFollower") == None)


if __name__ == "__main__":
    unittest.main()
