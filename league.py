# __author__ = 'User'
from input_exception import InputException
from leader import Leader
from side_kick import SideKick
from ally import Ally
from follower import Follower
from edice import EDice


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

    def add_character(self, name="", char_type="", health="", brawl="",
                      shoot="", dodge="", might="", finesse="",
                      cunning="", **abilities):
        """Adds a new character to the league"""

        # First need to check that the user has not created a character with
        # the same name as an existing character: These 'if not' statements
        # are saying if the result is False then ...
        if not self.check_duplicate_name(name):
            # This is the same as returning None
            return

        # Check none of the arguments passed to the function are empty or
        #  missed out
        # Could call an exception to check this - would have to be called in
        # the controller - ?
        # check_empty_arg() could be called for each argument. This would
        # enable the system to identify which attributes
        # are missing, if any are missing
        """if not self.check_empty_arg(name, health, brawl, shoot, dodge, might,
                                    finesse, cunning, **abilities):
            return"""

        # Checking the abilities which the user may have attempted to add to
        # the character actually are abilities which
        # are recognised by the system
        # This functionality could be replaced by an exception ...
        # if not self.check_abilities(abilities):
        #    print("Character creation of " + name + " has been unsuccessful, "
        #                                            "please try again.")
        #    return None

        # Check that the character class string the user has entered matches a
        # valid character class
        if not self.check_valid_character(char_type):
            return

        # There needs to be a check that only one Leader and one Side-Kick can
        # be in the league

        # Check that the user has entered valid values for the new character's
        # health
        # if not self.check_health_input(char_type, health):
        #    return

        # Check that the details for the skills which the user has inputted are
        # valid
        # if not self.check_skills_input(char_type, brawl, shoot, dodge, might,
        #                               finesse, cunning):
        #    return

        # There could be a check here that the character is being given a
        # ability with a permitted level, instead of
        # being done after the character creation block

        # If no errors have been found then the characters can be created
        if char_type == Leader.__name__:
            new_character = Leader(self, name, health, brawl, shoot, dodge,
                                   might, finesse, cunning, **abilities)
        elif char_type == Ally.__name__:
            new_character = Ally(self, name, health, brawl, shoot, dodge,
                                 might, finesse, cunning, **abilities)
        elif char_type == SideKick.__name__:
            new_character = SideKick(self, name, health, brawl, shoot, dodge,
                                     might, finesse, cunning, **abilities)
        elif char_type == Follower.__name__:
            new_character = Follower(self, name, health, brawl, shoot, dodge,
                                     might, finesse, cunning, **abilities)
        else:
            try:
                raise InputException("User has tried to create a character "
                                     "with an unrecognised class.")
            except InputException as e:
                print(e.value)
                return

        # print("New char: " + str(new_character))

        if new_character is not None:
            print("Character creation of " + name + " the " + char_type +
                  " has been successful!")
            self._all_my_characters.append(new_character)
            return new_character

        # These commented out checks are now performed before the character
        # creation:
        # if not self.check_number_skill_dice(new_character):
        #    return print("Character creation of " + name + " the " + char_type
        #  + " has been unsuccessful, please try
        # again.")

        # if not self.check_type_skill_dice(new_character):
        #    return print("Character creation of " + name + " the " + char_type
        #  + " has been unsuccessful, please try
        # again.")

        """if not self.check_number_abilities(new_character):
            print("Character creation of " + name + " the " + char_type +
                  " has been unsuccessful, please try again.")
            return

        errors_level = False
        errors_dupl = False

        for ability in new_character.get_abilities():
            print("Ability to be added: " + ability.get_name())
            print("Ability level: " + ability.get_level())

            # The level value of each ability object needs to be converted into
            #  a int - because the
            # instances of Ability have been obtained from file Strings
            if not self.check_level_abili(new_character,
                                          int(ability.get_level())):
                errors_level = True

            # If none of the character's abilities are duplicates then the
            # character is okay
            if self.check_duplicate_values(new_character.get_abilities()):
                errors_dupl = True

        if errors_level:
            print("Character creation of " + name + " the " + char_type +
                  " has been unsuccessful, please try again.")
            return

        if errors_dupl:
            print("User has tried to give the character a duplicate ability")
            print("Character creation has been unsuccessful, please try "
                  "again.")
            return

        print("Character creation of " + name + " the " + char_type +
              " has been successful!")
        self._all_my_characters.append(new_character)
        return new_character"""

    @staticmethod
    def check_valid_character(char_type):
        if char_type == Leader.__name__ or char_type == Ally.__name__ or \
                        char_type == SideKick.__name__ or char_type \
                == Follower.__name__:
            return True
        else:
            return False

    def check_health_input(self, char_type, health):
        results = self.get_skill_values(health)
        # print("Number: " + results[0])
        # print("Type: " + results[1])
        check = False
        if results[0] == "":
            # check that the dice type is valid
            if self.check_health_dice_type(char_type, results[1]):
                check = True
        else:
            print("The health skill should not be prefixed by any numbers. "
                  "Please try again.")
        return check

    @staticmethod
    def check_health_dice_type(char_type, health_dice_type):

        if char_type == Leader.__name__ \
                and health_dice_type == str(EDice.d10.name):
            return True
        elif char_type == SideKick.__name__ \
                and health_dice_type == str(EDice.d8.name):
            return True
        elif char_type == Ally.__name__ \
                and health_dice_type == str(EDice.d6.name):
            return True
        elif char_type == Follower.__name__ \
                and health_dice_type == str(EDice.d6.name):
            return True
        else:
            print("Incorrect input for the new character's health. Please try "
                  "again")
            return False

    def check_skills_input(self, char_type, brawl, shoot, dodge, might,
                           finesse, cunning):
        number_dice_list = []
        dice_type_list = []

        number_dice_list.append(self.get_skill_values(brawl)[0])
        dice_type_list.append(self.get_skill_values(brawl)[1])

        number_dice_list.append(self.get_skill_values(shoot)[0])
        dice_type_list.append(self.get_skill_values(shoot)[1])

        number_dice_list.append(self.get_skill_values(dodge)[0])
        dice_type_list.append(self.get_skill_values(dodge)[1])

        number_dice_list.append(self.get_skill_values(might)[0])
        dice_type_list.append(self.get_skill_values(might)[1])

        number_dice_list.append(self.get_skill_values(finesse)[0])
        dice_type_list.append(self.get_skill_values(finesse)[1])

        number_dice_list.append(self.get_skill_values(cunning)[0])
        dice_type_list.append(self.get_skill_values(cunning)[1])

        if self.check_number_dice(char_type, number_dice_list) and \
                self.check_dice_type(char_type, dice_type_list):
            return True
        else:
            return False

    def check_number_dice(self, char_type, number_dice_list):
        """
        This function checks the number of dice which the user would like the
        skills to have has been done correctly according to the class of the
        character to be created
        :param char_type: A string representing the class of the character to
        be created
        :param number_dice_list: A 1-D list containing the numbers of dice the
        user has assigned for each skill
        :return: will return True if the conditional tests determine that the
        user's input to set the character's skills
        is correct
        >>>check_number_dice("Leader", [3, 3, 3, 3, 2, 2])
        True
        """
        number_3_dice_skills = 0
        number_2_dice_skills = 0
        number_1_dice_skills = 0

        if char_type == Leader.__name__:
            for x in number_dice_list:
                if x == '3':
                    number_3_dice_skills += 1
                elif x == '2':
                    number_2_dice_skills += 1
            # print(number_2_dice_skills)
            # print(number_3_dice_skills)
            if number_3_dice_skills != 4 or number_2_dice_skills != 2:
                try:
                    raise InputException("Incorrect dice number setting for "
                                         "the new character's skills. Please "
                                         "try again")
                except InputException as e:
                    print(e.value)
            else:
                return True

        if char_type == SideKick.__name__:
            for x in number_dice_list:
                if x == '3':
                    number_3_dice_skills += 1
                elif x == '2':
                    number_2_dice_skills += 1
            # print(number_2_dice_skills)
            # print(number_3_dice_skills)
            if number_3_dice_skills != 3 or number_2_dice_skills != 3:
                try:
                    raise InputException("Incorrect dice number setting for "
                                         "the new character's skills. Please "
                                         "try again")
                except InputException as e:
                    print(e.value)
            else:
                return True

        if char_type == Ally.__name__:
            for x in number_dice_list:
                if x == '2':
                    number_2_dice_skills += 1
                elif x == '1':
                    number_1_dice_skills += 1
            # print(number_2_dice_skills)
            # print(number_1_dice_skills)
            # If either of these are incorrect, so use 'or'
            if number_2_dice_skills != 2 or number_1_dice_skills != 4:
                try:
                    raise InputException("Incorrect dice number setting for "
                                         "the new character's skills. Please "
                                         "try again")
                except InputException as e:
                    print(e.value)
            else:
                return True

        if char_type == Follower.__name__:
            for x in number_dice_list:
                if x == '1':
                    number_1_dice_skills += 1
            # print(number_1_dice_skills)
            if number_1_dice_skills != 6:
                try:
                    raise InputException("Incorrect dice number setting for "
                                         "the new character's skills. Please "
                                         "try again")
                except InputException as e:
                    print(e.value)
            else:
                return True

    @staticmethod
    def check_dice_type(char_type, dice_type_list):
        """
        This function will check whether the new character's skills going to
        be being assigned the correct dice types
        :param char_type: The character class (string)
        :param dice_type_list: list of strings which represent the type of
        die the user has inputted
        :return:
        """
        number_d6_dice = 0
        number_d8_dice = 0
        number_d10_dice = 0

        if char_type == Leader.__name__:
            for x in dice_type_list:
                if x == EDice.d10.name:
                    number_d10_dice += 1
                elif x == EDice.d8.name:
                    number_d8_dice += 1
            # print(number_d10_dice)
            # print(number_d8_dice)
            if number_d10_dice != 4 or number_d8_dice != 2:
                try:
                    raise InputException("Incorrect dice type for at least "
                                         "one of the new character's skills. "
                                         "Please try again")
                except InputException as e:
                    print(e.value)
            else:
                return True

        if char_type == SideKick.__name__:
            for x in dice_type_list:
                if x == EDice.d8.name:
                    number_d8_dice += 1
                elif x == EDice.d6.name:
                    number_d6_dice += 1
            # print(number_d8_dice)
            # print(number_d6_dice)
            if number_d8_dice != 3 or number_d6_dice != 3:
                try:
                    raise InputException("Incorrect dice type for at least "
                                         "one of the new character's skills. "
                                         "Please try again")
                except InputException as e:
                    print(e.value)
            else:
                return True

        if char_type == Ally.__name__:
            for x in dice_type_list:
                if x == EDice.d6.name:
                    number_d6_dice += 1
            # print(number_d6_dice)
            # If either of these are incorrect, so use 'or'
            if number_d6_dice != 6:
                try:
                    raise InputException("Incorrect dice type for at least one"
                                         " of the new character's skills. "
                                         "Please try again")
                except InputException as e:
                    print(e.value)
            else:
                return True

        if char_type == Follower.__name__:
            for x in dice_type_list:
                if x == EDice.d6.name:
                    number_d6_dice += 1
            # print(number_d6_dice)
            if number_d6_dice != 6:
                try:
                    raise InputException("Incorrect dice type for at least one"
                                         " of the new character's skills. "
                                         "Please try again")
                except InputException as e:
                    print(e.value)
            else:
                return True

    @staticmethod
    def get_skill_values(skill_input):
        """
        This function was actually initially created to check the skill input
        was in this format: 2d10brawl
        However, it can still handle this format: 2d10 ... I have now changed
        it so that it will only accept the latter format.
        :param skill_input: a string representing the number of dice and type
        of dice a user would like to assign to a character's skill
        :return:
        """
        number_dice = []
        alpha_array = []
        i = 0
        while i < len(skill_input):
            if skill_input[i].isdigit():
                number_dice.append(skill_input[i])
                i += 1
            elif skill_input[i].isalpha():
                j = i
                while j < len(skill_input):
                    if skill_input[j].isalpha():
                        alpha_array.append(j)
                        # print(alphaArray[len(alphaArray) - 1])
                    j += 1
                break

        # The following lines will get the number of dice, the type of dice,
        # and the skill type:
        number_dice_str = "".join(number_dice)
        type_dice_str = ""

        if len(alpha_array) == 0:
            type_dice_str = ""
        elif len(alpha_array) == 1:
            type_dice_str = skill_input[alpha_array[0]:]
        elif len(alpha_array) > 1:
            type_dice_str = ""

        results = [number_dice_str, type_dice_str]
        return results

    def check_duplicate_name(self, name):
        for c in self._all_my_characters:
            if name == c.get_name():
                print("User has tried to create a character with the name of"
                      " an existing character.")
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

    def check_abilities(self, abilities):
        """
        This method checks whether the abilities a user is trying to add are
        valid abilities
        :param abilities: a dictionary of strings which are names of abilities
        :return: Boolean result
        """
        abili_names = []
        invalid_abili = []
        for ab in self._my_league_model.get_all_abilities():
            abili_names.append(ab.get_name())

        for name in abilities:
            if not abilities[name] in abili_names:
                if abilities[name] != "":
                    invalid_abili.append(abilities[name])

        if len(invalid_abili) > 0:
            for ab in invalid_abili:
                print(ab + " is not a valid ability and cannot be added to the"
                           " character")
            return False
        else:
            return True

    @staticmethod
    def check_empty_arg(name, health, brawl, shoot, dodge, might, finesse,
                        cunning, **abilities):
        if name == "" or health == "" or brawl == "" or shoot == "" \
                or dodge == "" or might == "" or finesse == "" \
                or cunning == "" or len(abilities) == 0:
            print("At least one necessary character input value is missing")
            return False
        else:
            return True

    # Need to remove the default arguments for this to work:
    @staticmethod
    def check_number_arguments(health="", brawl="", shoot="", dodge="",
                               might="", finesse="", cunning=""):
        if health == "" or brawl == "" or shoot == "" or dodge == "" \
                or might == "" or finesse == "" or cunning == "":
            print("Not enough skill arguments")
            return

    @staticmethod
    def check_number_skill_dice(new_char):
        """
        This function checks the number of dice assigned to the skills has
        been done correctly
        according to the class of the character to be created
        :param new_char: an instance of a subclass of the Character class
        """
        number_3_dice_skills = 0
        number_2_dice_skills = 0
        number_1_dice_skills = 0

        # In case one or more of the skills have been set with invalid values,
        #  eg "" or None
        try:
            skills_list = [new_char.get_brawl().get_number_dice(),
                           new_char.get_cunning().get_number_dice(),
                           new_char.get_might().get_number_dice(),
                           new_char.get_dodge().get_number_dice(),
                           new_char.get_finesse().get_number_dice(),
                           new_char.get_shoot().get_number_dice()]
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
            # print(number_2_dice_skills)
            # print(number_3_dice_skills)
            if number_3_dice_skills != 4 or number_2_dice_skills != 2:
                try:
                    raise InputException("Incorrect dice number setting for "
                                         "the new character's skills. Please "
                                         "try again")
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
            # print(number_2_dice_skills)
            # print(number_3_dice_skills)
            if number_3_dice_skills != 3 or number_2_dice_skills != 3:
                try:
                    raise InputException("Incorrect dice number setting for"
                                         " the new character's skills. "
                                         "Please try again")
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
            # print(number_2_dice_skills)
            # print(number_1_dice_skills)
            # If either of these are incorrect, so use 'or'
            if number_2_dice_skills != 2 or number_1_dice_skills != 4:
                try:
                    raise InputException("Incorrect dice number setting for "
                                         "the new character's skills. "
                                         "Please try again")
                except InputException as e:
                    print(e.value)
            else:
                return True

        if new_char.__class__.__name__ == "Follower":
            for x in skills_list:
                if x == '1':
                    number_1_dice_skills += 1
            # print(number_1_dice_skills)
            if number_1_dice_skills != 6:
                try:
                    raise InputException("Incorrect dice number setting for "
                                         "the new character's skills. "
                                         "Please try again")
                except InputException as e:
                    print(e.value)
            else:
                return True

    @staticmethod
    def check_type_skill_dice(new_char):
        """
        This function checks the type of dice assigned to the skills has been
        done correctly
        according to the class of the character to be created
        :param new_char: an instance of a subclass of the Character class
        """
        number_d6_dice = 0
        number_d8_dice = 0
        number_d10_dice = 0
        skills_list = [new_char.get_brawl().get_dice_type().name,
                       new_char.get_cunning().get_dice_type().name,
                       new_char.get_might().get_dice_type().name,
                       new_char.get_dodge().get_dice_type().name,
                       new_char.get_finesse().get_dice_type().name,
                       new_char.get_shoot().get_dice_type().name]
        print("skills dice type list: " + str(skills_list))
        # print(isinstance(new_char.get_brawl().get_dice_type(), EDice))

        if new_char.__class__.__name__ == "Leader":
            for x in skills_list:
                if x == EDice.d10.name:
                    number_d10_dice += 1
                elif x == EDice.d8.name:
                    number_d8_dice += 1
            # print(number_d10_dice)
            # print(number_d8_dice)
            if number_d10_dice != 4 or number_d8_dice != 2:
                try:
                    raise InputException("Incorrect dice type for at least one"
                                         " of the new character's skills. "
                                         "Please try again")
                except InputException as e:
                    print(e.value)
            else:
                return True

        if new_char.__class__.__name__ == "SideKick":
            for x in skills_list:
                if x == EDice.d8.name:
                    number_d8_dice += 1
                elif x == EDice.d6.name:
                    number_d6_dice += 1
            # print(number_d8_dice)
            # print(number_d6_dice)
            if number_d8_dice != 3 or number_d6_dice != 3:
                try:
                    raise InputException("Incorrect dice type for at least "
                                         "one of the new character's skills. "
                                         "Please try again")
                except InputException as e:
                    print(e.value)
            else:
                return True

        if new_char.__class__.__name__ == "Ally":
            for x in skills_list:
                if x == EDice.d6.name:
                    number_d6_dice += 1
            # print(number_d6_dice)
            # If either of these are incorrect, so use 'or'
            if number_d6_dice != 6:
                try:
                    raise InputException("Incorrect dice type for at least "
                                         "one of the new character's skills. "
                                         "Please try again")
                except InputException as e:
                    print(e.value)
            else:
                return True

        if new_char.__class__.__name__ == "Follower":
            for x in skills_list:
                if x == EDice.d6.name:
                    number_d6_dice += 1
            # print(number_d6_dice)
            if number_d6_dice != 6:
                try:
                    raise InputException("Incorrect dice type for at least "
                                         "one of the new character's skills. "
                                         "Please try again")
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
                print("The leader does not have the maximum number of "
                      "abilities")
                return False
            elif len(abilities_list) > 3:
                print("The leader has been given too many abilities")
                return False

        if character.__class__.__name__ == "SideKick":
            if len(abilities_list) == 2:
                return True
            elif len(abilities_list) < 2:
                print("The side kick does not have the maximum number of "
                      "abilities")
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
                print("The follower does not have the maximum number of "
                      "abilities")
                return False
            elif len(abilities_list) > 1:
                print("The follower has been given too many abilities")
                return False

    @staticmethod
    def check_level_abili(character, input_level):
        """
        This method checks the level(s) of the ability or abilities which the
        user has been given are legal according
        to the character creation rules
        :param new_char: an instance of a subclass of the Character class
        :param ability: an ability the character has
        :return: A boolean value which indicates whether the character be given
        an ability of a certain level
        """

        if character.__class__.__name__ == "Leader":
            # Leaders are allowed to choose an ability of any level
            # Just in case an ability has a level less than 1:
            if input_level > 0:
                return True
            else:
                print(character.get_name() + " the leader cannot be given an"
                                             " ability with this level number")
                return False

        elif character.__class__.__name__ == "SideKick":
            if 0 < input_level <= 3:
                return True
            else:
                print(character.get_name() + " the side kick cannot be given "
                                             "an ability with this level "
                                             "number")
                return False

        elif character.__class__.__name__ == "Ally":
            if 0 < input_level <= 2:
                return True
            else:
                print(character.get_name() + " the ally cannot be given "
                                             "an ability with this level "
                                             "number")
                return False

        elif character.__class__.__name__ == "Follower":
            if input_level == 1:
                return True
            else:
                print(character.get_name() + " the follower cannot be given "
                                             "an ability with this level "
                                             "number")
                return False

    def char_remove_ability(self, ability_name, char_name):
        """
        This function will check that a character exists in the league. If so,
         then the method attempt to remove an
        ability from the character's abilities list
        :param ability_name: the String name of an ability the user would like
         to remove
        :param char: the String name of a char
        :return: A boolean value to indicate whether the removal has been
        successful or not
        """
        for ch in self._all_my_characters:

            if ch.get_name() == char_name:
                bool_result = False
                for abili in ch.get_abilities():
                    if abili.get_name() == ability_name:
                        bool_result = True
                if bool_result:
                    if ch.remove_ability(ability_name):
                        print(char_name + "'s '" + ability_name + "' ability"
                                                                  " has been"
                                                                  " removed")
                        return True
                    else:
                        print(char_name + " does have an ability called " +
                              ability_name + ", but it has not been removed.")
                # Instead of the else statement, an exception could be raised.
                else:
                    print(char_name + " does not have an ability called " +
                          ability_name + ", so it cannot be removed.")
                    return False

        # If a return statement has not been run then:
        print("A character called " + char_name + " does not exist in the " +
              self._name + " league")
        return False

    @staticmethod
    def check_add_ability(character):
        """
        This is a function to add an ability to a new character
        :param character: an instance of a subclass of the Character class
        :return:
        """
        # Perhaps the error message printed here should be called from the
        # method which calls this method
        abilities_list = character.get_abilities()

        if character.__class__.__name__ == "Leader":
            if len(abilities_list) < 3:
                return True
            else:
                print(character.get_name() + " the leader cannot add anymore "
                                             "abilities")
                return False

        if character.__class__.__name__ == "SideKick":
            if len(abilities_list) < 2:
                return True
            else:
                print(character.get_name() + " the side kick cannot add"
                                             " anymore abilities")
                return False

        if character.__class__.__name__ == "Ally":
            if len(abilities_list) < 1:
                return True
            else:
                print(character.get_name() + " the ally cannot add anymore"
                                             " abilities")
                return False

        if character.__class__.__name__ == "Follower":
            if len(abilities_list) < 1:
                return True
            else:
                print(character.get_name() + " the follower cannot add anymore"
                                             " abilities")
                return False

    @staticmethod
    def check_add_ability_level(character):
        """
        This method checks the level(s) of the ability or abilities which the
        user has been given are legal according
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
                    print("The leader cannot add an ability with an invalid "
                          "level number")
                    return False

        elif character.__class__.__name__ == "SideKick":
            for ab in abilities_list:
                if abilities_list[ab].get_level() > 0 \
                        or abilities_list[ab].get_level() <= 3:
                    return True
                else:
                    print("The side kick has been given an ability with an "
                          "invalid level number")
                    return False

        elif character.__class__.__name__ == "Ally":
            for ab in abilities_list:
                if abilities_list[ab].get_level() > 0 \
                        or abilities_list[ab].get_level() <= 2:
                    return True
                else:
                    print("The ally has been given an ability with an invalid"
                          " level number")
                    return False

        elif character.__class__.__name__ == "Follower":
            for ab in abilities_list:
                if abilities_list[ab].get_level() > 0 \
                        or abilities_list[ab].get_level() <= 1:
                    return True
                else:
                    print("The follower has been given an ability with an"
                          " invalid level number")
                    return False

    def char_add_ability(self, ability_name, char_name):
        """
        This function will first check that a character exists in the league.
        If so, then the method attempt to add an ability
        to the character's abilities list
        :param ability_name: the String name of an ability the user would like
         to remove
        :return: A boolean value to indicate whether the removal has been
         successful or not
        """
        # Instead of the else statements, exceptions could be raised.

        for ch in self._all_my_characters:
            if ch.get_name() == char_name:
                # Check whether the ability entered is a valid ability
                for abili in self._my_league_model.get_all_abilities():
                    if abili.get_name() == ability_name:
                        # Check whether the character is allowed to add a new
                        #  ability (ie does not have a max number of abilities)

                        if self.check_add_ability(ch):
                            # Check whether the character can add this level
                            # of ability
                            # print("Level ability: " + abili.get_level())
                            # print("Level name: " + abili.get_name())
                            if self.check_level_abili(ch,
                                                      int(abili.get_level())):
                                # Check whether the character already has this
                                #  particular ability
                                for ab in ch.get_abilities():
                                    if ab.get_name() == ability_name:
                                        print(char_name + " already has the"
                                                          " ability you would"
                                                          " like to add. '" +
                                              ability_name + "' has not been"
                                                             " added again.")
                                        return False

                                ch.add_ability(abili)
                                print(char_name + " has had this ability"
                                                  " added: " + ability_name)
                                return True
                            else:
                                return False
                        else:
                            # print("The character cannot add another ability")
                            return False

                # This code will only run if the ability passed into this
                #  method is not in the list of legit abilities
                print("Attempting to add an unrecognised ability")
                return False
        # Or could raise an exception here?:
        # This code will only run if the loop above has not found the character
        #  name in the list of characters:
        print("A character called " + char_name + " does not exist in the " +
              self._name + " league")
        return False

# if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
