__author__ = 'mih279'

from edice import EDice
from character_exception import CharacterException
from character import Character


class Follower(Character):
    level = 1
    size = 1
    number_abilities = 1
    base_health = EDice.d6.name
    
    def __init__(self, league, name, health, brawl, shoot, dodge, might,
                 finesse, cunning, **abilities):
        Character.__init__(self, league, name, health, brawl, shoot, dodge,
                           might, finesse, cunning, **abilities)

        results = super().check_skills_input(brawl, shoot, dodge, might,
                                             finesse, cunning)

        # Check the health type
        if health != self.base_health:
            # raise an exception
            raise CharacterException("Incorrect health input")

        number_1_dice_skills = 0
        number_d6_dice = 0

        # Check the number of dice
        for x in results[0]:
            if x == '1':
                number_1_dice_skills += 1
        # print(number_1_dice_skills)
        if number_1_dice_skills != 6:
            # raise an exception
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
            # raise an exception
            raise CharacterException("Incorrect dice type have been set for" +
                                     + name + " the " +
                                     self.__class__.__name__ + ". Please try "
                                                               "again")

        # Check the abilities which the user has entered
        super().check_abilities( name, self.__class__.__name__, self.level,
                                self.number_abilities, **abilities)

        # Check for duplicate abilities entered here? Or just leave the
        # ModelInputView to handle this?"""

    def __del__(self):
        print(self.__class__.__name__ + " object has been removed.")
