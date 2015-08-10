__author__ = 'User'

from edice import EDice
from input_exception import InputException
from leader import Leader
from side_kick import SideKick
from ally import Ally
from follower import Follower


class League(object):
    """The League class"""
    def __init__(self, name, all_my_chars=0, max_points=10):
        self._name = name
        self._all_my_characters = all_my_chars
        self._max_points = max_points

    def add_character(self, name, char_type, *skills_dict, **abilities):
        """Adds a new character to the league"""
        # First need to check what sort of character the user wants to create:
        if char_type == "Leader":
            new_character = Leader(name, *skills_dict, **abilities)
        elif char_type == "Ally":
            new_character = Ally(name, *skills_dict, **abilities)
        elif char_type == "Side Kick":
            new_character = SideKick(name, *skills_dict, **abilities)
        elif char_type == "Follower":
            new_character = Follower(name, *skills_dict, **abilities)
        else:
            try:
                raise InputException("User has tried to create an unrecognised class.")
            except InputException as e:
                print(e.value)

        # if new_character:
        #    print(new_character.get_name() + " the " + new_character.get_char_type() + " has been created.")
        # else:
        #    print("Character creation has been unsuccessful, please try again.")

        if new_character.get_brawl() is not None:
            if self.check_number_skill_dice(new_character):
                if self.check_type_skill_dice(new_character):
                    # Look at the output format which should be followed here:
                    print("Character creation has been successful!")
                    return new_character
                else:
                    # This string should really be a constant
                    return print("Character creation has been unsuccessful, please try again.")
            else:
                return print("Character creation has been unsuccessful, please try again.")
        else:
            return print("Character creation has been unsuccessful, please try again.")

    @staticmethod
    def check_number_skill_dice(new_char):
        """
        This function checks the number of dice assigned to the skills has been done correctly
        according to the class of the character to be created
        :param new_char: an instance of a subclass of the Character class
        """
        number_3_dice_skills = 0
        number_2_dice_skills = 0
        number_1_dice_skills = 0
        skills_list = [new_char.get_brawl().get_number_dice(), new_char.get_cunning().get_number_dice(),
                       new_char.get_might().get_number_dice(), new_char.get_dodge().get_number_dice(),
                       new_char.get_finesse().get_number_dice(), new_char.get_shoot().get_number_dice()]
        print("skills list: " + str(skills_list))

        if new_char.__class__.__name__ == "Leader":
            for x in skills_list:
                if x == '3':
                    number_3_dice_skills += 1
                elif x == '2':
                    number_2_dice_skills += 1
            print(number_2_dice_skills)
            print(number_3_dice_skills)
            if number_3_dice_skills != 4 or number_2_dice_skills != 2:
                try:
                    raise InputException("Incorrect dice number setting for the new character's skills. Please try "
                                         "again")
                except InputException as e:
                    print(e.value)
            else:
                return True

        if new_char.__class__.__name__ == "SideKick":
            for x in skills_list:
                if x == '3':
                    number_3_dice_skills += 1
                elif x == '2':
                    number_2_dice_skills += 1
            print(number_2_dice_skills)
            print(number_3_dice_skills)
            if number_3_dice_skills != 3 or number_2_dice_skills != 3:
                try:
                    raise InputException("Incorrect dice number setting for the new character's skills. Please try "
                                         "again")
                except InputException as e:
                    print(e.value)
            else:
                return True

        if new_char.__class__.__name__ == "Ally":
            for x in skills_list:
                if x == '2':
                    number_2_dice_skills += 1
                elif x == '1':
                    number_1_dice_skills += 1
            print(number_2_dice_skills)
            print(number_1_dice_skills)
            # If either of these are incorrect, so use 'or'
            if number_2_dice_skills != 2 or number_1_dice_skills != 4:
                try:
                    raise InputException("Incorrect dice number setting for the new character's skills. Please try "
                                         "again")
                except InputException as e:
                    print(e.value)
            else:
                return True

        if new_char.__class__.__name__ == "Follower":
            for x in skills_list:
                if x == '1':
                    number_1_dice_skills += 1
            print(number_1_dice_skills)
            if number_1_dice_skills != 6:
                try:
                    raise InputException("Incorrect dice number setting for the new character's skills. Please try "
                                         "again")
                except InputException as e:
                    print(e.value)
            else:
                return True

    @staticmethod
    def check_type_skill_dice(new_char):
        """
        This function checks the type of dice assigned to the skills has been done correctly
        according to the class of the character to be created
        :param new_char: an instance of a subclass of the Character class
        """
        number_d6_dice = 0
        number_d8_dice = 0
        number_d10_dice = 0
        skills_list = [new_char.get_brawl().get_dice_type().name, new_char.get_cunning().get_dice_type().name,
                       new_char.get_might().get_dice_type().name, new_char.get_dodge().get_dice_type().name,
                       new_char.get_finesse().get_dice_type().name, new_char.get_shoot().get_dice_type().name]
        print("skills list: " + str(skills_list))
        print(isinstance(new_char.get_brawl().get_dice_type(), EDice))

        if new_char.__class__.__name__ == "Leader":
            for x in skills_list:
                if x == 'd10':
                    number_d10_dice += 1
                elif x == 'd8':
                    number_d8_dice += 1
            print(number_d10_dice)
            print(number_d8_dice)
            if number_d10_dice != 4 or number_d8_dice != 2:
                try:
                    raise InputException("Incorrect dice number setting for the new character's skills. Please try "
                                         "again")
                except InputException as e:
                    print(e.value)
            else:
                return True

        if new_char.__class__.__name__ == "SideKick":
            for x in skills_list:
                if x == 'd8':
                    number_d8_dice += 1
                elif x == 'd6':
                    number_d6_dice += 1
            print(number_d8_dice)
            print(number_d6_dice)
            if number_d8_dice != 3 or number_d6_dice != 3:
                try:
                    raise InputException("Incorrect dice number setting for the new character's skills. Please try "
                                         "again")
                except InputException as e:
                    print(e.value)
            else:
                return True

        if new_char.__class__.__name__ == "Ally":
            for x in skills_list:
                if x == 'd6':
                    number_d6_dice += 1
            print(number_d6_dice)
            # If either of these are incorrect, so use 'or'
            if number_d6_dice != 6:
                try:
                    raise InputException("Incorrect dice number setting for the new character's skills. Please try "
                                         "again")
                except InputException as e:
                    print(e.value)
            else:
                return True

        if new_char.__class__.__name__ == "Follower":
            for x in skills_list:
                if x == 'd6':
                    number_d6_dice += 1
            print(number_d6_dice)
            if number_d6_dice != 6:
                try:
                    raise InputException("Incorrect dice type setting for the new character's skills. Please try "
                                         "again")
                except InputException as e:
                    print(e.value)
            else:
                return True