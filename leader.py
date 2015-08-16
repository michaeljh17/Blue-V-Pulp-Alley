#__author__ = 'mih279'

from character import Character
from character_exception import CharacterException
from edice import EDice


class Leader(Character):
    level = 4
    size = 0
    number_abilities = 3
    base_health = EDice.d10.name
    
    def __init__(self, league, name, health, brawl, shoot, dodge, might,
                 finesse, cunning, **abilities):
        Character.__init__(self, league, name, health, brawl, shoot, dodge,
                           might, finesse, cunning, **abilities)

        results = super().check_skills_input(brawl, shoot, dodge, might,
                                             finesse, cunning)

        # Check the health type
        if health != self.base_health:
            # raise an exception
            return

        number_2_dice_skills = 0
        number_3_dice_skills = 0
        number_d8_dice = 0
        number_d10_dice = 0

        # Check the number of dice
        for x in results[0]:
            if x == '3':
                number_3_dice_skills += 1
            elif x == '2':
                number_2_dice_skills += 1
        # print(number_2_dice_skills)
        # print(number_3_dice_skills)
        if number_3_dice_skills != 4 or number_2_dice_skills != 2:
            try:
                raise CharacterException("Incorrect dice number setting for " +
                                         " the new character's skills. Please "
                                         + "try again")
            except CharacterException as e:
                print(e.value)
                return

        # Check the dice type
        for x in results[1]:
            if x == EDice.d10.name:
                number_d10_dice += 1
            elif x == EDice.d8.name:
                number_d8_dice += 1
        # print(number_d10_dice)
        # print(number_d8_dice)
        if number_d10_dice != 4 or number_d8_dice != 2:
            try:
                raise CharacterException("Incorrect dice type for at least " +
                                         " one of the new character's skills."
                                         + " Please try again")
            except CharacterException as e:
                print(e.value)
                return

        # Check the number of abilities which are entered
        # new_abilities will be a list
        super().check_abilities(self.__class__.__name__, self.level,
                                self.number_abilities, **abilities)

