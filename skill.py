__author__ = 'User'

from edice import EDice
from reveal_access import RevealAccess

from edice import EDice
from input_exception import InputException


class Skill(object):
    """The Ally class"""
    def __init__(self, skill_name, dice_type, number_dice=1):
        # self.skill_name = RevealAccess(skill_name)
        self._skill_name = skill_name
        self._number_dice = number_dice
        self._dice_type = dice_type

    # def __get__(self, instance, owner):
    #   print ('Retrieving this skill: ', self.name)
    #   result = [self.name, self.number_dice, self.dice_type]
    #   return result

    def __str__(self):
        return self._skill_name.name + ' skill. Dice: ' + str(self._number_dice) + ' ' + self._dice_type

    def set_number_dice(self, number_dice):
        self._number_dice = number_dice

    def get_number_dice(self):
        return self._number_dice

    def set_dice_type(self, dice_type):
        """
        input needs to be validated as being an enum
        Am using an assert to do this:
        """
        # assert isinstance(dice_type, EDice), print("%r is not an EDice type" % dice_type)
        # assert type(dice_type) is EDice, print("%r is not an EDice type" % dice_type)
        try:
            if not isinstance(dice_type, EDice):
                raise InputException("Incorrect user input: The dice type for a skill is not an EDice type")
            else:
                self._dice_type = dice_type
        except InputException as e:
            print(e.value)


    def get_dice_type(self):
        return self._dice_type

    def set_skill_name(self, skill_name):
        self._skill_name = skill_name

    def get_skill_name(self):
        return self._skill_name.name

