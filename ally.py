__author__ = 'User'

from character import Character
from edice import EDice
from character_exception import CharacterException


class Ally(Character):
    level = 2
    size = 2
    number_abilities = 1
    base_health = EDice.d6.name
    
    def __init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities):
        super().__init__(league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities)

        results = super().check_skills_input(brawl, shoot, dodge, might,
                                             finesse, cunning)

        # Check the health type
        if health != self.base_health:
            # raise an exception
            return

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
        # If either of these are incorrect an exception shold be raised,
        # so use 'or':
        if number_2_dice_skills != 2 or number_1_dice_skills != 4:
            try:
                raise CharacterException("Incorrect dice number setting for " +
                                     "the new character's skills. Please " +
                                     "try again")
            except CharacterException as e:
                print(e.value)
                return

        # Check the dice type
        for x in results[1]:
            if x == EDice.d6.name:
                number_d6_dice += 1
        # print(number_d6_dice)
        # If either of these are incorrect, so use 'or'
        if number_d6_dice != 6:
            try:
                raise CharacterException("Incorrect dice type for at least one" +
                                     " of the new character's skills. " +
                                     "Please try again")
            except CharacterException as e:
                print(e.value)
                return

        # Check the number of abilities which are entered
        # new_abilities will be a list
        # super().check_abilities(self.__class__.__name__, self.level,
        #                        self.number_abilities, **abilities)

        """if len(new_abilities) != 1:
            # Raise an exception
            print("The ally does not have the correct number of abilities: 1")

        if len(new_abilities) > 1:
            # Raise an exception
            print("The ally cannot have more than one ability.")

        # Check the level of the abilities which the user has entered
        for abili in new_abilities:
            if abili.get_level() > self.level:
                # raise an exception
                print("The ally cannot have an ability with a level " +
                      "higher than " + str(self.level))

        # Check for duplicate abilities entered here? Or just leave the View or
        # the ModelInputView to handle this?"""
