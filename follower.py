__author__ = 'mih279'

from edice import EDice
from character_exception import CharacterException
from character import Character


class Follower(Character):
    level = 1
    size = 1
    abilities_allowed = 1
    base_health = EDice.d6.name
    
    def __init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities):
        Character.__init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities)

        results = super().check_skills_input(brawl, shoot, dodge, might, finesse, cunning)

        # Check the health type
        if health != self.base_health:
            # raise an exception
            return

        number_1_dice_skills = 0
        number_d6_dice = 0

        # Check the number of dice
        for x in results[0]:
            if x == '1':
                number_1_dice_skills += 1
        # print(number_1_dice_skills)
        if number_1_dice_skills != 6:
            # raise an exception
            try:
                raise CharacterException("Incorrect dice number setting for "
                                     "the new character's skills. Please "
                                     "try again")
            except CharacterException as e:
                print(e.value)
                return

        # Check the dice type
        for x in results[1]:
            if x == EDice.d6.name:
                number_d6_dice += 1
        # print(number_d6_dice)
        if number_d6_dice != 6:
            # raise an exception
            try:
                raise CharacterException("Incorrect dice type for at least one"
                + " of the new character's skills. Please try again")
            except CharacterException as e:
                print(e.value)
                return

        # Check the number of abilities which are entered
        # new_abilities will be a list
        if not super().check_abilities(self.__class__.__name__, self.level,
                                self.abilities_allowed, **abilities):
            return

        """if len(new_abilities) != 1:
            # Raise an exception
            print("The follower does not have the correct number of abilities:"
                  + " 1")

        if len(new_abilities) > 1:
            # Raise an exception
            print("The follower cannot have more than one ability.")

        # Check the level of the abilities which the user has entered
        for abili in new_abilities:
            if abili.get_level() != self.level:
                # raise an exception
                print("The follower cannot have an ability with a level " +
                      "higher than " + str(self.level))

        # Check for duplicate abilities entered here? Or just leave the View or
        # the ModelInputView to handle this?"""
