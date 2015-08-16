#__author__ = 'mih279'

from character import Character
from edice import EDice
from character_exception import CharacterException
from edice import EDice


class SideKick(Character):
    level = 3
    size = 3
    number_abilities = 2
    base_health = EDice.d8.name
    
    def __init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities):
        Character.__init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities)

        results = super().check_skills_input(brawl, shoot, dodge, might,
                                             finesse, cunning)

        # Check the health type
        if health != self.base_health:
            # raise an exception
            try:
                raise CharacterException("Incorrect health input")
            except CharacterException as e:
                print(e.value)
                return

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
            # raise an exception (use these exceptions if you want or change them):
            try:
                raise CharacterException("Incorrect dice number setting for "
                                     "the new character's skills. Please "
                                     "try again")
            except CharacterException as e:
                print(e.value)
                return

        # Check the dice type
        for x in results[1]:
            if x == EDice.d8.name:
                number_d8_dice += 1
            elif x == EDice.d6.name:
                number_d6_dice += 1
        # print(number_d8_dice)
        # print(number_d6_dice)
        if number_d8_dice != 3 or number_d6_dice != 3:
            try:
                raise CharacterException("Incorrect dice type for at least " +
                                         "one of the new character's skills. "
                                         + "Please try again")
            except CharacterException as e:
                print(e.value)
                return

        # Check the number of abilities which are entered
        # new_abilities will be a list
        if not super().check_abilities(self.__class__.__name__, self.level,
                                self.number_abilities, **abilities):
            return

        """if len(new_abilities) != 2:
            # Raise an exception
            print("The side kick does not have the correct number of abilities:"
                  + " 2")

        if len(new_abilities) > 2:
            # Raise an exception
            print("The side kick cannot have more than two abilities.")

        # Check the level of the abilities which the user has entered
        for abili in new_abilities:
            if abili.get_level() > self.level:
                print("The side kick cannot have an ability with a level " +
                      "higher than " + str(self.level))"""
