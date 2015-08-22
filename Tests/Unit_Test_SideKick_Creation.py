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
        self.cl = self.lm.get_current_league()
        self.lm.set_abilities_file(self.lm.read_file("..\Abilities.txt"))

    def test_01(self):
        print("Test 01 - Add Sidekick with incorrect health")
        self.cl.add_character("Kicky", char_type="SideKick", health="d10",
                              brawl="2d6", shoot="3d6", dodge="2d6",
                              might="3d8", finesse="2d8",
                              cunning="3d8", arg1="Mighty",
                              arg2="Brash", arg3="")

        self.assertTrue(self.cl.find_character("Kicky") == None)

    def test_02(self):
        print("Test 02 - Add Sidekick with - incorrect dice type")
        self.cl.add_character("Kicky", char_type="SideKick", health="d8",
                              brawl="2d6", shoot="3d10", dodge="2d6",
                              might="3d8", finesse="2d8",
                              cunning="3d8", arg1="Mighty",
                              arg2="Brash", arg3="")

        self.assertTrue(self.cl.find_character("Kicky") == None)

    def test_03(self):
        print("Test 03 - Add SideKick - Happy day")
        self.cl.add_character("Kicky", char_type="SideKick", health="d8",
                              brawl="2d6", shoot="3d6", dodge="2d6",
                              might="3d8", finesse="2d8",
                              cunning="3d8", arg1="Mighty",
                              arg2="Brash", arg3="")

        self.assertTrue(str(self.cl.find_character("Kicky")) == "Kicky")
        self.cl.delete_character_by_name("Kicky")

    def test_04(self):
        print("Test 04 - Add SideKick - Incorrectly Set Skill")
        self.cl.add_character("Kicky", char_type="SideKick", health="d8",
                              brawl="3d6", shoot="3d6", dodge="2d6",
                              might="3d8", finesse="2d8",
                              cunning="3d8", arg1="Mighty",
                              arg2="Brash", arg3="")

        self.assertTrue(self.cl.find_character("Kicky") == None)

    def test_05(self):
        print("Test 05 - Add SideKick - When there is already a sideKick")
        self.cl.add_character("Kicky", char_type="SideKick", health="d8",
                              brawl="2d6", shoot="3d6", dodge="2d6",
                              might="3d8", finesse="2d8",
                              cunning="3d8", arg1="Mighty",
                              arg2="Brash", arg3="")

        self.cl.add_character("Kicky02", char_type="SideKick", health="d8",
                              brawl="2d6", shoot="3d6", dodge="2d6",
                              might="3d8", finesse="2d8",
                              cunning="3d8", arg1="Mighty",
                              arg2="Brash", arg3="")

        self.assertTrue(self.cl.find_character("Kicky02") == None)
        self.cl.delete_character_by_name("Kicky")
        self.cl.delete_character_by_name("Kicky02")

    def test_06(self):
        print("Test 06 - Add SideKick - when there is a character with "
              + "the same name in the league")
        self.cl.add_character("Kicky", "Leader", "d10", "3d10", "3d10", "3d8",
                              "3d10", "2d8", "2d10", arg1="Mighty",
                              arg2="Brash", arg3="Crafty")
        self.cl.add_character("Kicky", char_type="SideKick", health="d8",
                              brawl="2d6", shoot="3d6", dodge="2d6",
                              might="3d8", finesse="2d8",
                              cunning="3d8", arg1="Mighty",
                              arg2="Brash", arg3="")
        self.cl.delete_character_by_name("Kicky")
        self.assertTrue(self.cl.find_character("Kicky") == None)


if __name__ == "__main__":
    unittest.main()
