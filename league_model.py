# __author__ = 'User'
from league import League
from ability import Ability
import string


class LeagueModel(object):
    """Top model class"""
    def __init__(self, all_my_abilities=[], my_league=""):
        self._all_my_abilities = all_my_abilities
        # self._all_my_abilities = ["Hey", "Yes", "Wow"]
        self._my_league = my_league

    def export_league(self):
        return self._my_league

    def set_abilities_file(self, input):
        temp = []
        for sub_list in input:
            for attr in sub_list:
                temp.append(attr)
                # print(attr)
            new_ability = Ability(temp[0],temp[1],temp[2],temp[3])
            # print(new_ability)
            self._all_my_abilities.append(new_ability)
            temp = []

    def get_all_abilities(self):
        return self._all_my_abilities

    def add_league(self, name):
        self._my_league = League(self, name)

    def get_current_league(self):
        return self._my_league

    # File handling and reading functions:

    def read_file(self, filename):
        data = []
        file_content = open(filename, "r")
        for line in file_content:
            if line != "\n":
                # print(line)
                self.get_line_data(line, data)
        file_content.close()
        return data

    @staticmethod
    def get_line_data(line, data):
        # line = line.replace('/', ' ')
        ability_details = []
        for attr in line.split(','):
            # attr = attr.lower()
            attr = attr.strip(string.punctuation + string.whitespace)
            ability_details.append(attr)
        data.append(ability_details)



