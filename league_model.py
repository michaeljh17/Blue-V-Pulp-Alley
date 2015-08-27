# __author__ = 'User'
from league import League
from ability import Ability


class LeagueModel(object):
    """Top model class"""

    def __init__(self, all_my_abilities=[], my_league=""):
        self._all_my_abilities = all_my_abilities
        self._my_league = my_league

    def set_abilities_file(self, input):
        temp = []
        # global ability_list
        ability_list = []
        for sub_list in input:
            for attr in sub_list:
                temp.append(attr)
                # print(attr)
            new_ability = Ability(temp[0], temp[1], temp[2], temp[3])
            # print(new_ability)
            self._all_my_abilities.append(new_ability)
            temp = []
            ability_list.append(new_ability)
        # return ability_list

    def get_ability_by_name(self, name):
        for ability in self._all_my_abilities:
            if ability.get_name() == name:
                return ability

    def get_all_abilities(self):
        return self._all_my_abilities

    def add_league(self, name):
        self._my_league = League(self, name)

    def set_league(self, league_object):
        self._my_league = league_object

    def get_current_league(self):
        return self._my_league

    def delete_league(self):
        del self._my_league
        self._my_league = ""

    # League Export functions

    def export_league(self):
        return self._my_league.export_league()

    def export_character(self, character_name):
        #  -MS-
        the_data = self._my_league.export_character(character_name)
        # print("Data given to lm " + str(the_data))
        abilities = the_data[5]
        # print(str(the_data))
        # print(str(the_data[5]))
        # print(str(abilities))
        del the_data[5]
        new_row = ["Abilities"]
        the_data.append(new_row)
        new_row = ["Name", "Level", "Effect"]
        the_data.append(new_row)
        for ability in abilities:
            if ability is not "":
                the_ability = self.get_ability_by_name(ability)
                new_row = []
                new_row.append(ability)
                new_row.append(str(the_ability.get_level()))
                new_row.append("Adds " + str(the_ability.get_modifier()) +
                               " to " + the_ability.get_effected_skill())
                the_data.append(new_row)
        # print("Result from LeagueModel " + str(the_data))
        return the_data

    def export_league_binary(self):
        return self._my_league
