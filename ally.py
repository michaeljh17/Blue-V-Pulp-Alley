__author__ = 'User'

from character import Character
from edice import EDice
from character_exception import CharacterException


class Ally(Character):
    _level = 2
    _size = 2
    _number_abilities = 1
    _base_health = EDice.d6.name
    # Dice type - values: 1) Edice 2) number of these Edice
    _dice_type_1 = [EDice.d6, 6]
    _dice_type_2 = None
    # Dice numbers - values: 1) dice numbers 2) numbers of these dice
    _dice_numbers_1 = [2, 2]
    _dice_numbers_2 = [1, 4]
    
    def __init__(self, league, name, health, brawl, shoot, dodge, might,
                 finesse, cunning, **abilities):
        super().__init__(league, name, health, brawl, shoot, dodge, might,
                         finesse, cunning, **abilities)

        results = super().get_skills_input(brawl, shoot, dodge, might,
                                             finesse, cunning)

        super().check_health(health, self._base_health)

        number_1_dice_skills = 0
        number_2_dice_skills = 0
        number_d6_dice = 0

        # Check the number of dice
        for x in results[0]:
            if x == '2':
                number_2_dice_skills += 1
            elif x == '1':
                number_1_dice_skills += 1
        # print(number_2_dice_skills)
        # print(number_1_dice_skills)
        # If either of these are incorrect an exception should be raised
        # so use 'or':
        if number_2_dice_skills != 2 or number_1_dice_skills != 4:
            raise CharacterException("Incorrect dice numbers have been set for"
                                     + " " + name + " the " +
                                     self.__class__.__name__ + ". Please try "
                                                               "again")

        # Check the dice type
        for x in results[1]:
            if x == EDice.d6.name:
                number_d6_dice += 1
        # print(number_d6_dice)
        if number_d6_dice != 6:
            raise CharacterException("Incorrect dice type have been set for "
                                     + name + " the " +
                                     self.__class__.__name__ + ". Please try "
                                                               "again")

        # Check the abilities which the user has entered
        super().check_abilities(name, self.__class__.__name__, self._level,
                                self._number_abilities, **abilities)

    def __del__(self):
        print(self.__class__.__name__ + " object has been removed.")

    @staticmethod
    def get_level():
        return Character.level