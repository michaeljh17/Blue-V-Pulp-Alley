from Test_Add_Character import *

test = Test_Add_Character()


""" Test leader Creation """
test.lm.get_current_league().add_character("L", char_type="Leader", health="d10",
                                      brawl="3d10", shoot="2d10", dodge="3d8",
                                      might="3d10", finesse="2d10",
                                      cunning="3d8", arg1="Mighty",
                                      arg2="Brash", arg3="Crafty")
#test.check_character_creation_methods("Create a Leader, Happy Day", True,"Bruce","Leader","d10","3d10","3d10","3d8","3d10","2d8","2d10", "Mighty", "Brash", "Crafty")
"""
test.check_character_creation_methods("Create a Leader, Incorrectly Set Skill",
                                False,"Bruce", "Leader","d10","2d10","3d10",
                                "3d8","3d10","2d8","2d10","Mighty","Brash",
                                "Crafty")

test.check_character_creation_methods("Create a Leader, Incorrectly Set Health",
                                False,"Bruce", "Leader","d8","3d10","3d10",
                                "3d8","3d10","2d8","2d10","Mighty","Brash",
                                "Crafty")

test.lm.get_current_league().add_character("Bruce", "Leader","d10","3d10","3d10",
                                     "3d8","3d10","2d8","2d10",arg1="Mighty",
                                     arg2="Brash", arg3="Crafty")

test.check_character_creation_methods("Create a Leader, When there is already a leader",
                                False,"Danny", "Leader","d10","3d10","3d10",
                                "3d8","3d10","2d8","2d10","Mighty","Brash",
                                "Crafty")

test.lm.get_current_league().add_character("Bruce", "Leader","d10","3d10","3d10",
                                     "3d8","3d10","2d8","2d10",arg1="Mighty",
                                   arg2="Brash", arg3="Crafty")

test.check_character_creation_methods("Create a Leader, When there is already a leader with the same name", 
                                False,"Bruce", "Leader","d10","3d10","3d10","3d8","3d10","2d8",
                                "2d10","Mighty","Brash","Crafty")
"""