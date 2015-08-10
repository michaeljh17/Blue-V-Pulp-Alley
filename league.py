__author__ = 'User'

from input_exception import InputException
from leader import Leader
from side_kick import SideKick
from ally import Ally
from follower import Follower


class League(object):
    """The League class"""

    def __init__(self, name, all_my_chars=[], max_points=10):
        self._name = name
        self._all_my_characters = all_my_chars
        self._max_points = max_points

    def __str__(self):
        return self._name

    def get_all_my_characters(self):
        return self._all_my_characters

    def get_name(self):
        return self._name

    def add_character(self, name="", char_type="", health="", brawl="", shoot="", dodge="", might="", finesse="",
                      cunning="", *abilities):
        """Adds a new character to the league"""

        # First need to check that the user has not created a character with the same name as an existing character:
        if not self.check_duplicate_name(name):
            return

        # Check none of the arguments passed to the function are empty or missed out
        # Could call an exception to check this - would have to be called in the controller though ...
        # check_empty_arg() could be called for each argument. This would enable the system to identify which attributes
        # are missing, if any are missing
        if not self.check_empty_arg(name, health, brawl, shoot, dodge, might, finesse, cunning):
            return

        # Then need to check what sort of character the user wants to create (is there a better way of doing this?):
        if char_type == "Leader":
            new_character = Leader(self, name, health, brawl, shoot, dodge, might, finesse, cunning, *abilities)
        elif char_type == "Ally":
            new_character = Ally(self, name, health, brawl, shoot, dodge, might, finesse, cunning, *abilities)
        elif char_type == "Side Kick":
            new_character = SideKick(self, name, health, brawl, shoot, dodge, might, finesse, cunning, *abilities)
        elif char_type == "Follower":
            new_character = Follower(self, name, health, brawl, shoot, dodge, might, finesse, cunning, *abilities)
        else:
            try:
                raise InputException("User has tried to create a character with an unrecognised class.")
            except InputException as e:
                print(e.value)
                return

        if self.check_number_skill_dice(new_character):
            if self.check_type_skill_dice(new_character):
                print("Character creation has been successful!")
                self._all_my_characters.append(new_character)
                return new_character
            else:
                # This string should really be a constant
                return print("Character creation has been unsuccessful, please try again.")
        else:
            return print("Character creation has been unsuccessful, please try again.")

    def check_duplicate_name(self, name):
        for c in self._all_my_characters:
            if name == c.get_name():
                print("User has tried to create a character with the name of an existing character.")
                return False
        return True

    @staticmethod
    def check_empty_arg(name, health, brawl, shoot, dodge, might, finesse, cunning):
        if name == "" or health == "" or brawl == "" or shoot == "" or dodge == "" or might == "" or finesse == "" \
                or cunning == "":
            print("At least one necessary character input value is missing")
            return False
        else:
            return True

    # Need to remove the default arguments for this to work:
    def check_number_arguments(self, health="", brawl="", shoot="", dodge="", might="", finesse="", cunning=""):
        if health == "" or brawl == "" or shoot == "" or dodge == "" or might == "" or finesse == "" or cunning == "":
            print("Not enough skill arguments")
            return

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

        # In case one or more of the skills have been set with invalid values, eg "" or None
        try:
            skills_list = [new_char.get_brawl().get_number_dice(), new_char.get_cunning().get_number_dice(),
                       new_char.get_might().get_number_dice(), new_char.get_dodge().get_number_dice(),
                       new_char.get_finesse().get_number_dice(), new_char.get_shoot().get_number_dice()]
        except AttributeError as e:
            print(e)
            return False

        print("skills number dice list: " + str(skills_list))

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
        print("skills dice type list: " + str(skills_list))
        # print(isinstance(new_char.get_brawl().get_dice_type(), EDice))

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
