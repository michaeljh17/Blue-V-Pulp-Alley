from character import Character
from character_exception import CharacterException
from edice import EDice


class SideKick(Character):
    _level = 3
    _size = 3
    _number_abilities = 2
    _base_health = EDice.d8.name
    # Dice type - values: 1) Edice 2) number of these Edice
    _dice_type_1 = [EDice.d8, 3]
    _dice_type_2 = [EDice.d6, 3]
    # Dice numbers - values: 1) dice numbers 2) numbers of these dice
    _dice_numbers_1 = [3, 3]
    _dice_numbers_2 = [2, 3]

    def __init__(self, league, name, health, brawl, shoot, dodge, might,
                 finesse, cunning, **abilities):
        super().__init__(league, name, health, brawl, shoot, dodge, might,
                         finesse, cunning, **abilities)

        results = super().get_skills_input(brawl, shoot, dodge, might,
                                             finesse, cunning)

        super().check_health(health, self._base_health)

        super().check_number_dice(self, results[0])

        super().check_type_dice(self, results[1])

        """
        number_2_dice_skills = 0
        number_3_dice_skills = 0
        number_d6_dice = 0
        number_d8_dice = 0

        # Check the number of dice
        for x in results[0]:
            if x == '3':
                number_3_dice_skills += 1
            elif x == '2':
                number_2_dice_skills += 1
        # print(number_2_dice_skills)
        # print(number_3_dice_skills)
        if number_3_dice_skills != 3 or number_2_dice_skills != 3:
            # raise an exception
            raise CharacterException("Incorrect dice number setting for " +
                                     "the new character's skills. Please " +
                                     "try again")

        # Check the dice type
        for x in results[1]:
            if x == EDice.d8.name:
                number_d8_dice += 1
            elif x == EDice.d6.name:
                number_d6_dice += 1
        # print(number_d8_dice)
        # print(number_d6_dice)
        if number_d8_dice != 3 or number_d6_dice != 3:
            # raise an exception
            raise CharacterException("Incorrect dice type have been set for " +
                                     name + " the " +
                                     self.__class__.__name__ + ". Please try "
                                                               "again")
        """

        # Check the abilities which the user has entered
        super().check_abilities( name, self.__class__.__name__, self._level,
                                self._number_abilities, **abilities)

    def __del__(self):
        print(self.__class__.__name__ + " object has been removed.")

    @staticmethod
    def get_level():
        return Character.level