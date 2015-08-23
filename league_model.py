#?# __author__ = 'User'
from league import League
from ability import Ability
import string


class LeagueModel(object):
    """Top model class"""
    def __init__(self, all_my_abilities=[], my_league=""):
        self._all_my_abilities = all_my_abilities
        self._my_league = my_league

    def set_abilities_file(self, input):
        temp = []
        global ability_list
        ability_list = []
        for sub_list in input:
            for attr in sub_list:
                temp.append(attr)
                # print(attr)
            new_ability = Ability(temp[0],temp[1],temp[2],temp[3])
            # print(new_ability)
            self._all_my_abilities.append(new_ability)
            temp = []
            ability_list.append(new_ability)
        # return ability_list

    def get_all_abilities(self):
        return self._all_my_abilities

    def add_league(self, name):
        self._my_league = League(self, name)

    def get_current_league(self):
        return self._my_league

    # League Export functions

    def export_league(self):
        return self._my_league.export_league()
