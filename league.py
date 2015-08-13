__author__ = 'User'

from input_exception import InputException
from leader import Leader
from side_kick import SideKick
from ally import Ally
from follower import Follower


class League(object):
    """The League class"""

    def __init__(self, league_model, name, all_my_chars=[], max_points=10):
        self._name = name
        self._all_my_characters = all_my_chars
        self._max_points = max_points
        self._my_league_model = league_model

    def __str__(self):
        return self._name

    def get_all_my_characters(self):
        return self._all_my_characters

    def get_name(self):
        return self._name

    def get_my_league_model(self):
        return self._my_league_model

    def find_character(self, char_name):
        for ch in self._all_my_characters:
            if ch.get_name() == char_name:
                return ch
        return None

    def add_character(self, name="", char_type="", health="", brawl="", shoot="", dodge="", might="", finesse="",
                      cunning="", **abilities):
        # def add_character(self, name="", char_type="", **skills_abilities):
        """Adds a new character to the league"""

        # First need to check that the user has not created a character with the same name as an existing character:
        if not self.check_duplicate_name(name):
            return

        # Check none of the arguments passed to the function are empty or missed out
        # Could call an exception to check this - would have to be called in the controller though ...
        # check_empty_arg() could be called for each argument. This would enable the system to identify which attributes
        # are missing, if any are missing
        if not self.check_empty_arg(name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities):
            return

        # Then need to check what sort of character the user wants to create (is there a better way of doing this?):
        # Now checking char_type against the the class of the Character child-classes:
        if char_type == Leader.__name__:
            new_character = Leader(self, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities)
        elif char_type == Ally.__name__:
            new_character = Ally(self, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities)
        elif char_type == SideKick.__name__:
            new_character = SideKick(self, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities)
        elif char_type == Follower.__name__:
            new_character = Follower(self, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities)
        else:
            try:
                raise InputException("User has tried to create a character with an unrecognised class.")
            except InputException as e:
                print(e.value)
                return

        if self.check_number_skill_dice(new_character):

            if self.check_type_skill_dice(new_character):

                if self.check_number_abilities(new_character):

                    for ability in new_character.get_abilities():
                        # The level value of each ability object needs to be converted into a int - because the
                        # instances of Ability have been obtained from file Strings
                        if self.check_level_ability(new_character, int(ability.get_level())):

                            # If none of the character's abilities are duplicates then the character is okay
                            if not self.check_duplicate_values(new_character.get_abilities()):
                                print("Character creation has been successful!")
                                self._all_my_characters.append(new_character)
                                return new_character
                            else:
                                print("User has tried to give the character a duplicate ability")
                                return print("Character creation has been unsuccessful, please try again.")
                        else:
                            return print("Character creation has been unsuccessful, please try again.")
                    else:
                        # This string should really be made into a constant
                        return print("Character creation has been unsuccessful, please try again.")
                else:
                    return print("Character creation has been unsuccessful, please try again.")
            else:
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
    def check_duplicate_values(collection):
        a_dict = dict()

        for a in collection:
            if a not in a_dict:
                a_dict[a] = 1
            else:
                a_dict[a] += 1

        for b in a_dict:
            if a_dict[b] > 1:
                return True
        return False

        #for a in collection:
        #    for b in collection:
        #       if b == a and a_dict[a] is None:
        #           a_dict[a] = 1
        #       elif b == a and a_dict[a] > 0:
        #           a_dict[a] += 1

        #   if a_dict[a] > 1:
               # This means there are duplicate items in the dictionary
        #       return True
        # This means there are no duplicate items in the collection
        # return False


    @staticmethod
    def check_empty_arg(name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities):
        if name == "" or health == "" or brawl == "" or shoot == "" or dodge == "" or might == "" or finesse == "" \
                or cunning == "" or len(abilities) == 0:
            print("At least one necessary character input value is missing")
            return False
        else:
            return True

    # Need to remove the default arguments for this to work:
    @staticmethod
    def check_number_arguments(health="", brawl="", shoot="", dodge="", might="", finesse="", cunning=""):
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
                    raise InputException("Incorrect dice type for at least one of the new character's skills. Please try "
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
                    raise InputException("Incorrect dice type for at least one of the new character's skills. Please try "
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
                    raise InputException("Incorrect dice type for at least one of the new character's skills. Please try "
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
                    raise InputException("Incorrect dice type for at least one of the new character's skills. Please try "
                                         "again")
                except InputException as e:
                    print(e.value)
            else:
                return True

    @staticmethod
    def check_number_abilities(character):
        """
        This is a function to set the abilities of the new character
        :param new_char: an instance of a subclass of the Character class
        :return:
        """
        abilities_list = character.get_abilities()

        if character.__class__.__name__ == "Leader":
            if len(abilities_list) == 3:
                return True
            elif len(abilities_list) < 3:
                print("The leader does not have the maximum number of abilities")
                return False
            elif len(abilities_list) > 3:
                print("The leader has been given too many abilities")
                return False

        if character.__class__.__name__ == "SideKick":
            if len(abilities_list) == 2:
                return True
            elif len(abilities_list) < 2:
                print("The side kick does not have the maximum number of abilities")
                return False
            elif len(abilities_list) > 2:
                print("The side kick has been given too many abilities")
                return False

        if character.__class__.__name__ == "Ally":
            if len(abilities_list) == 1:
                return True
            elif len(abilities_list) < 1:
                print("The ally does not have the maximum number of abilities")
                return False
            elif len(abilities_list) > 1:
                print("The ally has been given too many abilities")
                return False

        if character.__class__.__name__ == "Follower":
            if len(abilities_list) == 1:
                return True
            elif len(abilities_list) < 1:
                print("The follower does not have the maximum number of abilities")
                return False
            elif len(abilities_list) > 1:
                print("The follower has been given too many abilities")
                return False

    @staticmethod
    def check_level_ability(character, input_level):
        """
        This method checks the level(s) of the ability or abilities which the user has been given are legal according
        to the character creation rules
        :param new_char: an instance of a subclass of the Character class
        :param ability: an ability the character has
        :return: A boolean value which indicates whether the character be given an ability of a certain level
        """

        if character.__class__.__name__ == "Leader":
            # Leaders are allowed to choose an ability of any level
            # Just in case an ability has a level less than 1:
            if input_level > 0:
                return True
            else:
                print("The leader cannot be given an ability with this level number")
                return False

        elif character.__class__.__name__ == "SideKick":
            if input_level > 0 or input_level <= 3:
                return True
            else:
                print("The side kick cannot be given an ability with this level number")
                return False

        elif character.__class__.__name__ == "Ally":
            if input_level > 0 or input_level <= 2:
                return True
            else:
                print("The ally cannot be given an ability with this level number")
                return False

        elif character.__class__.__name__ == "Follower":
            if input_level > 0 or input_level <= 1:
                return True
            else:
                print("cannot be given an ability with this level number")
                return False

    def char_remove_ability(self, ability_name, char_name):
        """
        This function will check that a character exists in the league. If so, then the method attempt to remove an
        ability from the character's abilities list
        :param ability_name: the String name of an ability the user would like to remove
        :param char: the String name of a char
        :return: A boolean value to indicate whether the removal has been successful or not
        """
        for ch in self._all_my_characters:
            if ch.get_name() == char_name:
                bool_result = False
                for abili in ch.get_abilities():
                    if abili.get_name() == ability_name:
                        bool_result = True
                if bool_result:
                        if ch.remove_ability(ability_name):
                            print("The character's " + ability_name + " ability has been removed")
                            return True
                        else:
                            print(char_name + " does have an ability called " + ability_name + ", but it has not been "
                                                                                               "removed.")
                # Instead of the else statement, an exception could be raised.
                else:
                    print(char_name + " does not have an ability called " + ability_name + ", so it cannot be "
                                                                                           "removed.")
                    return False
            else:
                print("A character called " + char_name + " does not exist in the " + self._name + " league")
                return False

    @staticmethod
    def check_add_ability(character):
        """
        This is a function to set the abilities of the new character
        :param new_char: an instance of a subclass of the Character class
        :return:
        """
        # Perhaps the error message printed here should be called from the method which calls this method
        abilities_list = character.get_abilities()

        if character.__class__.__name__ == "Leader":
            if len(abilities_list) < 3:
                return True
            else:
                print("The leader cannot add anymore abilities")
                return False

        if character.__class__.__name__ == "SideKick":
            if len(abilities_list) < 2:
                return True
            else:
                print("The side kick cannot add anymore abilities")
                return False

        if character.__class__.__name__ == "Ally":
            if len(abilities_list) == 1:
                return True
            else:
                print("The ally cannot add anymore abilities")
                return False

        if character.__class__.__name__ == "Follower":
            if len(abilities_list) == 1:
                return True
            else:
                print("The follower cannot add anymore abilities")
                return False

    @staticmethod
    def check_add_ability_level(character):
        """
        This method checks the level(s) of the ability or abilities which the user has been given are legal according
        to the character creation rules
        :param new_char: an instance of a subclass of the Character class
        :return:
        """
        abilities_list = character.get_abilities()

        if character.__class__.__name__ == "Leader":
            # Leaders are allowed to choose an ability of any level
            # Just in case an ability has a level less than 1:
            for ab in abilities_list:
                if abilities_list[ab].get_level() > 0:
                    return True
                else:
                    print("The leader cannot add an ability with an invalid level number")
                    return False

        elif character.__class__.__name__ == "SideKick":
            for ab in abilities_list:
                if abilities_list[ab].get_level() > 0 or abilities_list[ab].get_level() <= 3:
                    return True
                else:
                    print("The side kick has been given an ability with an invalid level number")
                    return False

        elif character.__class__.__name__ == "Ally":
            for ab in abilities_list:
                if abilities_list[ab].get_level() > 0 or abilities_list[ab].get_level() <= 2:
                    return True
                else:
                    print("The ally has been given an ability with an invalid level number")
                    return False

        elif character.__class__.__name__ == "Follower":
            for ab in abilities_list:
                if abilities_list[ab].get_level() > 0 or abilities_list[ab].get_level() <= 1:
                    return True
                else:
                    print("The follower has been given an ability with an invalid level number")
                    return False

    def char_add_ability(self, ability_name, char_name):
        """
        This function will first check that a character exists in the league. If so, then the method attempt to add an ability
        to the character's abilities list
        :param ability_name: the String name of an ability the user would like to remove
        :return: A boolean value to indicate whether the removal has been successful or not
        """
        # Instead of the else statements, exceptions could be raised.

        for ch in self._all_my_characters:
            if ch.get_name() == char_name:
                # Check whether the ability entered is a valid ability
                for abili in self._my_league_model.get_all_abilities():
                    if abili.get_name() == ability_name:
                        # Check whether the character is allowed to add a new ability (ie does not have a max number of
                        # abilities)
                        if self.check_add_ability(ch):
                            # Check whether the character can add this level of ability
                            if self.check_level_ability(ch, int(abili.get_level())):
                                # Check whether the character already has this particular ability
                                for ab in ch.get_abilities():
                                    if ab.get_name() == ability_name:
                                        print("The character already has the ability you would like to add. " +
                                              ability_name + " has not been added.")
                                        return False

                                ch.add_ability(abili)
                                print("The character has had this ability added: " + ability_name)
                                return True
                            else:
                                return False
                        else:
                            print("The character cannot add another ability")
                            return False

            print("Attempting to add an unrecognised ability")
            return False
        # Or could raise an exception here:
        else:
            print("A character called " + char_name + " does not exist in the " + self._name + " league")
            return False
