import sys
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if path not in sys.path:
    sys.path.insert(1, path)
del path
from league import *
from character import *
from league_model import *
from FilerModule.FilerModule import *
from ViewModel.ViewModel import *


lm = LeagueModel()
lm.add_league("Test League")
fm = FilerModule()
lm.set_abilities_file(fm.read_file("..\Abilities.txt"))
vm = ViewModel()

lm.get_current_league().add_character("Bruce", char_type="Leader",
                                      health="d10", brawl="3d10",
                                      shoot="2d10", dodge="3d8",
                                      might="3d10",
                                      finesse="2d10",
                                      cunning="3d8",
                                      arg1="Mighty", arg2="Brash",
                                      arg3="Crafty")
print(lm.get_current_league().find_character("Bruce"))

result = vm.build_character_table(
    lm.export_character("Bruce"))
vm.display(result)
