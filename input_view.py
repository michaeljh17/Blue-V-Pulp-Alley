from input_exception import InputException
from edice import EDice
from character import Character
import re


class InputView(object):

    def __init__(self):
        pass

    def check_valid_name(self, input_name):
        match = re.search(r'[^\w\d]+', input_name)
        if match is None:
            pass
        else:
            raise InputException("Invalid name entry: Please use only "
                                 "alphanumeric characters for the name of a "
                                 "new character. Please try again")
        if input_name != "":
            return input
        else:
            raise InputException("The user must enter a name for this"
                                 " character. Please try again")

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
        dice_str_data = Character.obtain_dice_data(input_dice)

        # This will check the number of dice:

        if len(dice_str_data[0]) == 0:
            raise InputException("You have not entered the number of dice for"
                                 " a skill. Please try again")

        # This will check the type of dice:

        if len(dice_str_data[1]) == 0:
            raise InputException("You have not entered a valid dice type for a"
                                 " skill. Please try again")

        # Checking whether a valid dice type has been entered by the user:
        for edice in EDice:
            if dice_str_data[1] == edice.name:
                return
        raise InputException("Invalid dice type entry. Please try again")

    @staticmethod
    def check_valid_ability(input_ability, all_abilities):
        for abili in all_abilities:
            if input_ability == abili.get_name():
                return
        raise InputException("Invalid ability name entry. Please try again")

    @staticmethod
    def check_duplicate_values(collection):
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
