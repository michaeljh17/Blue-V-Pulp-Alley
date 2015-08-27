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

    def test_01(self):
        print("Test 01 - Add Follower with incorrect health")
        self.cl.add_character("Bounder", char_type="Follower", health="d10",
                              brawl="1d6", shoot="1d6", dodge="1d6",
                              might="1d6", finesse="1d6", cunning="1d6",
                              arg1="Mighty", arg2="", arg3="")

        self.assertTrue(self.cl.find_character("Bounder") == None)

    def test_02(self):
        print("Test 02 - Add Follower with - incorrect dice type")
        self.cl.add_character("Bounder", char_type="Follower", health="d6",
                              brawl="1d6", shoot="1d6", dodge="1d6",
                              might="1d8", finesse="1d6", cunning="1d6",
                              arg1="Mighty", arg2="", arg3="")

        self.assertTrue(self.cl.find_character("Bounder") == None)

    def test_03(self):
        print("Test 03 - Add Follower - Happy day")
        self.cl.add_character("Bounder", char_type="Follower", health="d6",
                              brawl="1d6", shoot="1d6", dodge="1d6",
                              might="1d6", finesse="1d6", cunning="1d6",
                              arg1="Mighty", arg2="", arg3="")

        the_character = self.cl.find_character("Bounder")
        self.assertTrue(str(the_character) == "Bounder")
        if the_character is not None:
            self.cl.remove_character(the_character)

    def test_04(self):
        print("Test 04 - Add Follower - Incorrectly Set Skill")
        self.cl.add_character("Bounder", char_type="Follower", health="d6",
                              brawl="2d6", shoot="1d6", dodge="1d6",
                              might="1d6", finesse="1d6", cunning="1d6",
                              arg1="Mighty", arg2="", arg3="")

        self.assertTrue(self.cl.find_character("Bounder") == None)

    def test_05(self):
        print("Test 05 - Add Follower - When there is already a Follower")
        self.cl.add_character("Bounder", char_type="Follower", health="d6",
                              brawl="1d6", shoot="1d6", dodge="1d6",
                              might="1d6", finesse="1d6", cunning="1d6",
                              arg1="Mighty", arg2="", arg3="")

        self.cl.add_character("Bounder02", char_type="Follower", health="d6",
                              brawl="1d6", shoot="1d6", dodge="1d6",
                              might="1d6", finesse="1d6", cunning="1d6",
                              arg1="Mighty", arg2="", arg3="")

        self.assertTrue(
            str(self.cl.find_character("Bounder02")) == "Bounder02")
        self.cl.delete_character_by_name("Bounder")
        self.cl.delete_character_by_name("Bounder02")

    def test_06(self):
        print("Test 06 - Add Follower - when there is a character with " +
              "the same name in the league")
        self.cl.add_character("Bounder", "Leader", "d10", "3d10", "3d10",
                              "3d8", "3d10", "2d8", "2d10", arg1="Mighty",
                              arg2="Brash", arg3="Crafty")
        self.cl.add_character("Bounder", char_type="Follower", health="d8",
                              brawl="2d6", shoot="3d6", dodge="2d6",
                              might="3d8", finesse="2d8",
                              cunning="3d8", arg1="Mighty",
                              arg2="Brash", arg3="")
        self.cl.delete_character_by_name("Bounder")
        self.assertTrue(self.cl.find_character("Bounder") == None)


if __name__ == "__main__":
    unittest.main()
