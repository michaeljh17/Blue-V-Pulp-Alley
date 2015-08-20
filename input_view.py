from input_exception import InputException
from character import Character
from edice import EDice
import string


class InputView(object):

    def __init__(self):
        pass

    def check_valid_name(self, input_name):
        if input_name != "":
            return input
        else:
            print("The user must enter a name for this character. Please try"
                  " again")
            raise InputException("Invalid name entry. Please try again")

    def check_valid_class(self, input_class):
        for charac in Character.__subclasses__():
            if input_class == charac.__name__:
                return
        raise InputException("Invalid class name entry. Please try again")

    @staticmethod
    def check_valid_skill_dice(input_dice):
        """
        Checks whether the string passed to this method is a valid dice type
        :param input_dice: string
        :return: returns None if successful
        """
        number_dice, type_dice = Character.obtain_dice_data(input_dice)

        for edice in EDice:
            if type_dice == edice.name:
                return
        raise InputException("Invalid dice type entry. Please try again")

    @staticmethod
    def check_valid_ability(input_ability, all_abilities):
        for abili in all_abilities:
            if input_ability == abili.get_name():
                return
        raise InputException("Invalid ability name entry. Please try again")

    @staticmethod
    def check_duplicate_values(*collection):
        a_dict = dict()

        for a in collection:
            if a not in a_dict:
                a_dict[a] = 1
            else:
                a_dict[a] += 1

        for b in a_dict:
            if a_dict[b] > 1:
                raise InputException("Invalid entry: duplicate ability names "
                                     "detected. Please try again")