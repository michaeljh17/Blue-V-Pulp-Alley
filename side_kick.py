from character import Character
from edice import EDice
from character_exception import CharacterException
from edice import EDice


class SideKick(Character):
    level = 3
    size = 3
    number_abilities = 2
    base_health = EDice.d8.name

    def __init__(self, league, name, health, brawl, shoot, dodge, might,
                 finesse, cunning, **abilities):
        super().__init__(league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities)

        results = super().check_skills_input(brawl, shoot, dodge, might,
                                             finesse, cunning)

        # Check the health type
        if health != self.base_health:
            # raise an exception
            raise CharacterException("Incorrect health input")

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
