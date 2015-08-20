from input_exception import InputException
from character import Character
from edice import EDice


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

    def check_valid_skill_dice(self, input_dice):
        for edice in EDice:
            if input_dice == edice.name:
                return
        raise InputException("Invalid dice type entry. Please try again")

    def check_valid_ability(self, input_ability, all_abilities):
        for abili in all_abilities:
            if input_ability == abili.get_name():
                return
        raise InputException("Invalid ability name entry. Please try again")