from abc import ABCMeta
from skill import Skill
from eskill import ESkill
from edice import EDice
from input_exception import InputException
from character_exception import CharacterException
import re


class Character(metaclass=ABCMeta):
    """The Character class"""
    __metaclass__ = ABCMeta

    # Class attributes
    _level = 0
    _size = 1
    _number_abilities = 0
    _base_health = 0
    # Dice type - values: 1) Edice 2) number of these Edice
    _dice_type_1 = [0, 0]
    _dice_type_2 = [0, 0]
    # Dice numbers - values: 1) dice numbers 2) numbers of these dice numbers
    _dice_numbers_1 = [0, 0]
    _dice_numbers_2 = [0, 0]

    def __init__(self, league, name, health, brawl, shoot, dodge, might,
                 finesse, cunning, **abilities):
        self.__my_league = league
        self.__name = name
        self.__health = self.set_skill(ESkill.health, health)
        self.__brawl = self.set_skill(ESkill.brawl, brawl)
        self.__shoot = self.set_skill(ESkill.shoot, shoot)
        self.__dodge = self.set_skill(ESkill.dodge, dodge)
        self.__might = self.set_skill(ESkill.might, might)
        self.__finesse = self.set_skill(ESkill.finesse, finesse)
        self.__cunning = self.set_skill(ESkill.cunning, cunning)
        # __abilities is a list of Ability objects
        self.__all_my_abilities = self.set_abilities(**abilities)

    def __str__(self):
        return self.__name

    @staticmethod
    def obtain_dice_data(skill_input):
        """
        Obtains the number of dice and the dice type from a string which is
        passed to this method.
        This method is used to test skill values as well as the health value
        :param skill_input: string input
        :return: 2 strings: 1) The number of dice 2) The type of dice
        """

        # This will return the first match of zero (in case the health
        # attribute is being tested) or any number of numbers at the start of
        # the string:
        match = re.search(r'^\d?\d*', skill_input)
        if match is not None:
            number_dice_str = match.group(0)
        else:
            number_dice_str = ""

        # This will return the first match of a letter followed by any
        # alphanumeric characters in the string:
        match = re.search(r'[a-zA-Z]\w*', skill_input)
        if match is not None:
            type_dice_str = match.group(0)
        else:
            type_dice_str = ""

        return [number_dice_str, type_dice_str]

    def find_edice(self, input_string):
        """
        This method will try to find if the input string matches a valid
        EDice type
        :param input_string:
        :return: An Edice type if a match is made
        """
        for x in EDice:
            if input_string == x.name:
                return x
        raise InputException("You have not entered a valid dice type for a "
                             "skill. Please try again")

    def set_skill(self, skill_type, skill_input):
        """
        :param skill_type: Type of skill which the user would like to add, as a
        string
        :param skill_input: The number of dice, and the type of die, of the
        skill to be set, as a string
        :return:
        """
        dice_str_data = Character.obtain_dice_data(skill_input)

        # When passing the dice-type to the Skill constructor, it should be an
        # EDice type instead of just a string

        type_dice = self.find_edice(dice_str_data[1])

        if skill_type == ESkill.health:
            # print("Adding a health skill")
            return Skill(ESkill.health, type_dice, dice_str_data[0])
        elif skill_type == ESkill.brawl:
            return Skill(ESkill.brawl, type_dice, dice_str_data[0])
        elif skill_type == ESkill.shoot:
            return Skill(ESkill.shoot, type_dice, dice_str_data[0])
        elif skill_type == ESkill.dodge:
            return Skill(ESkill.dodge, type_dice, dice_str_data[0])
        elif skill_type == ESkill.might:
            return Skill(ESkill.might, type_dice, dice_str_data[0])
        elif skill_type == ESkill.finesse:
            return Skill(ESkill.finesse, type_dice, dice_str_data[0])
        elif skill_type == ESkill.cunning:
            return Skill(ESkill.cunning, type_dice, dice_str_data[0])
        else:
            # An exception should actually never occur here
            try:
                raise InputException("'" + skill_type + "' is an unknown skill"
                                                        " type")
            except InputException as e:
                print(e.value)

        print()

    @staticmethod
    def get_skill_values(skill_input):
        """
        :skill_input: handles input in this format: 2d10
        :param skill_input: a string representing the number of dice and type
        of dice a user would like to assign to a character's skill
        :return:
        """
        number_dice_str = ""
        type_dice_str = ""
        i = 0

        if skill_input[0].isdigit():
            number_dice_str = skill_input[0]
        else:
            # raise an exception
            pass

        if skill_input[1].isalpha():
            type_dice_str = skill_input[1:]
        else:
            # raise an exception
            pass

        results = [number_dice_str, type_dice_str]
        return results

    def get_skills_input(self, brawl, shoot, dodge, might, finesse, cunning):
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

        results = [number_dice_list, dice_type_list]
        return results

    def set_abilities(self, **abilities):
        """
        This is a function to set the abilities of a character
        :param abilities: A dictionary of strings of the names of abilities.
        The keys are: 'arg1', 'arg2', 'arg3'
        :return: A list of Ability objects (unless no valid ability names have
        been passed to this method)
        """
        abil_coll = self.__my_league.get_my_league_model().get_all_abilities()
        new_abilities = []

        # abilities is a dictionary ? yes
        for new_ab in abilities:
            for existing_ab in abil_coll:
                if abilities[new_ab] == existing_ab.get_name():
                    new_abilities.append(existing_ab)
                    break

        self.__all_my_abilities = new_abilities
        return new_abilities

    def check_abilities(self, name, char_class, ability_level, number_allowed,
                        **abilities):
        """
        This is a function to check the abilities of a character
        :param abilities: A dictionary of strings of the names of abilities.
        The keys are: 'arg1', 'arg2', 'arg3'
        :return: A boolean value, which is True if the user has entered valid
        abilities for the new character
        """
        abil_coll = self.__my_league.get_my_league_model().get_all_abilities()
        new_abilities = []
        result = True

        # abilities is a dictionary ? yes
        for new_ab in abilities:
            for existing_ab in abil_coll:
                if abilities[new_ab] == existing_ab.get_name():
                    new_abilities.append(existing_ab)
                    break
            # call an exception here if the loop ends and it hasn't found
            # that the ability name is a valid ability? Not necessary - as
            # the input-view does this validation

        if len(new_abilities) > number_allowed:
            # Raise an exception
            raise CharacterException(name + " the " + char_class + " cannot "
                                                                   "have more "
                                                                   "than " +
                                     str(self._number_abilities) + " " +
                                     " abilities. Please try again.")

        if len(new_abilities) != number_allowed:
            # Raise an exception
            raise CharacterException(name + " the " + char_class +
                                     " does not have the correct number of " +
                                     "abilities: " +
                                     str(self._number_abilities) +
                                     ". Please try again.")

        # Check the level of the abilities which the user has entered
        for abili in new_abilities:
            if int(abili.get_level()) > ability_level:
                # raise an exception
                raise CharacterException("The " + char_class + " cannot have "
                                         "an ability with a level higher "
                                         "than " + str(self._level))

        return result

    def remove_ability(self, ability_name):
        """
        This function will attempt to remove an ability from the character's
        abilities list
        :param ability_name: the String name of an ability the user would like
        to remove
        :return: A boolean value to indicate whether the removal has been
        successful or not
        """
        for ability in self.__all_my_abilities:
            if ability.get_name() == ability_name:
                self.__all_my_abilities.remove(ability)
                return True
        return False

    # def

    def add_ability(self, ability):
        self.__all_my_abilities.append(ability)

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_health(self):
        return self.__health

    def get_brawl(self):
        return self.__brawl

    def set_brawl(self, input):
        self.__brawl = input

    def get_dodge(self):
        return self.__dodge

    def set_dodge(self, input):
        self.__dodge = input

    def get_might(self):
        return self.__might

    def set_might(self, input):
        self.__might = input

    def get_shoot(self):
        return self.__shoot

    def set_shoot(self, input):
        self.__shoot = input

    def get_finesse(self):
        return self.__finesse

    def set_finesse(self, input):
        self.__finesse = input

    def get_cunning(self):
        return self.__cunning

    def set_cunning(self, input):
        self.__cunning = input

    def get_my_league(self):
        return self.__my_league

    def get_abilities(self):
        return self.__all_my_abilities

    def get_level(self):
        return self._level

    def get_size(self):
        return self._size

    def get_number_abilities(self):
        return self._number_abilities

    def get_base_health(self):
        return self._base_health

    def export_character(self):
        """
        # Method used to export the current character into an array
        # formatted like a character sheet
        :return: An array containing the characters name, skills, and abilities
        """

        output = []
        output_key_pair = dict()

        output_key_pair["brawl"] = str(self.get_brawl().get_number_dice() +
                                       self.get_brawl().get_dice_type().name)
        output_key_pair["shoot"] = str(self.get_shoot().get_number_dice() +
                                       self.get_shoot().get_dice_type().name)
        output_key_pair["dodge"] = str(self.get_dodge().get_number_dice() +
                                       self.get_dodge().get_dice_type().name)
        output_key_pair["might"] = str(self.get_might().get_number_dice() +
                                       self.get_might().get_dice_type().name)
        output_key_pair["finesse"] = str(self.get_finesse().get_number_dice() +
                                         self.get_finesse().
                                         get_dice_type().name)
        output_key_pair["cunning"] = str(self.get_cunning().get_number_dice() +
                                         self.get_cunning().
                                         get_dice_type().name)

        for ability in self.__all_my_abilities:
            if ability.get_modifier() != 0:
                # find dict value die count
                base_die_count = int(output_key_pair[ability.
                                     get_effected_skill()][0])
                base_die_count += ability.get_modifier()
                # output_key_pair[ability.get_effected_skill()][0]
                # = str(base_die_count)
                slice_bit = output_key_pair[ability.get_effected_skill()][1:]
                output_key_pair[ability.get_effected_skill()] \
                    = str(base_die_count) + slice_bit
                output_key_pair[ability.get_effected_skill()] += "*"

        output.append(str(type(self).__name__))
        output.append(str(self.get_name()))
        output.append(str(self.get_health().get_dice_type().name))

        output.append(output_key_pair["brawl"])
        output.append(output_key_pair["shoot"])
        output.append(output_key_pair["dodge"])
        output.append(output_key_pair["might"])
        output.append(output_key_pair["finesse"])
        output.append(output_key_pair["cunning"])

        '''
        #Old Way
        output.append(str(self.get_brawl().get_number_dice()) +
         str(self.get_brawl().get_dice_type().name))
        output.append(str(self.get_shoot().get_number_dice()) +
         str(self.get_shoot().get_dice_type().name))
        output.append(str(self.get_dodge().get_number_dice()) +
         str(self.get_dodge().get_dice_type().name))
        output.append(str(self.get_might().get_number_dice()) +
         str(self.get_might().get_dice_type().name))
        output.append(str(self.get_finesse().get_number_dice()) +
         str(self.get_finesse().get_dice_type().name))
        output.append(str(self.get_cunning().get_number_dice()) +
         str(self.get_cunning().get_dice_type().name))
        '''

        skill_string = ""
        for ability in self.__all_my_abilities:
            # output.append(str(ability.get_name()))
            skill_string += str(ability.get_name()) + ", "
        # remove the trailing comma
        skill_string = skill_string[:(len(skill_string) - 2)]
        output.append(skill_string)

        return output

    def find_ability(self, character, ability_name, abilities_list):
        # Check that the character has the old ability
        for abili in abilities_list:
            if abili.get_name() == ability_name:
                return abili
        return None
        # Or could call an exception here?

    def get_subclass_abili_allowed(self, character_obj):
        """
        This method will get the value of _number_abilities for a subclass of
        Character
        :param character: an instance of a Character subclass
        :return: The value of _level
        """
        class_name = character_obj.__class__.__name__
        result = 0
        # Probably don't need to include error handling here ...?
        for subChar in Character.__subclasses__():
            if class_name == subChar.__name__:
                return subChar.get_number_abilities(self)
        return result

    def get_subclass_size(self, character_obj):
        """
        This method will get the value of _level for a subclass of Character
        :param character: an instance of a Character subclass
        :return: The value of _level
        """
        class_name = character_obj.__class__.__name__
        result = 0
        # Probably don't need to include error handling here ...?
        for subChar in Character.__subclasses__():
            if class_name == subChar.__name__:
                return subChar.get_size(self)
        return result

    def get_subclass_level(self, character_obj):
        """
        This method will get the value of _level for a subclass of Character
        :param character: an instance of a Character subclass
        :return: The value of _level
        """
        class_name = character_obj.__class__.__name__
        result = 0
        # Probably don't need to include error handling here ...?
        for subChar in Character.__subclasses__():
            if class_name == subChar.__name__:
                return subChar.get_level(self)
        return result

    def replace_ability(self, charac, old_ability_name, new_ability_name):
        """
        This function will replace one of a character's abilities with another
        one.
        Preconditions: 1) the name of the character has been checked as
        belonging to a character who exists in the league.
        2) the names of both the old ability and new ability have been checked
        as being valid abilities.
        :param charac: the instance of the character
        :param old_ability_name: the name of the old ability
        :param new_ability_name: the name of the new ability
        :return: ? A Boolean to indicate that the change has been successful ?
        """

        # First we really need to check that both the old ability and the new
        # ability are valid abilities
        old_abili = charac.find_ability(charac, old_ability_name,
                                        self.__all_my_abilities)
        abilities = self.__my_league.get_my_league_model().get_all_abilities()
        new_abili = charac.find_ability(charac, new_ability_name, abilities)

        max_level = self.get_subclass_level(charac)
        # print("Max level of " + charac.get_name() + ": " + str(max_level))

        if old_abili:
            if new_abili:
                # check the level of the new ability
                if int(new_abili.get_level()) <= max_level:
                    # Remove the unwanted ability from the character
                    self.__all_my_abilities.remove(old_abili)
                    # Add the new ability to the character
                    self.__all_my_abilities.append(new_abili)
                    print(charac.get_name() + "'s ability, " +
                          old_ability_name + ", has been removed and the "
                                             "character now has a new "
                          "ability: " + new_ability_name)
                else:
                    print(charac.get_name() + " cannot have the ability, " +
                          new_ability_name + ", because its level is too "
                                             "high. The attempt to replace "
                                             "abilities has failed.")
            else:
                print(new_ability_name + " is not a valid ability. The attempt"
                                         " to replace abilities has failed.")
        else:
            print(charac.get_name() + " does not the ability, " +
                  old_ability_name + ". The attempt to replace abilities has "
                                     "failed.")

    def clear_abilities(self):
        self.__all_my_abilities = []

    def check_number_dice(self, char_instance, num_dice_list):
        """
        :param char_instance: instance of a character
        :param num_dice_list: contains: 1) dice numbers 2) numbers of these
        dice numbers
        :return: none
        """

        # I'm just getting these values atm without using get() methods
        dice_number_1 = char_instance.__class__._dice_numbers_1
        dice_number_2 = char_instance.__class__._dice_numbers_2

        count_1 = 0
        count_2 = 0

        # Check the first set of dice numbers
        for x in num_dice_list:
            if x == str(dice_number_1[0]):
                # print("dice_number_1[0]: " + str(dice_number_1[0]))
                count_1 += 1
        # print("Count: " + str(count_1))
        if count_1 != dice_number_1[1]:
            # raise an exception
            raise CharacterException("Incorrect dice numbers have been set for"
                                     " " + char_instance.get_name() + " the " +
                                     self.__class__.__name__ + ". Please try "
                                                               "again")

        # Check the second set of dice numbers (if applicable)
        if dice_number_2 is not None:
            for x in num_dice_list:
                if x == str(dice_number_2[0]):
                    count_2 += 1
            # print(count_2)
            if count_2 != dice_number_2[1]:
                # raise an exception
                raise CharacterException("Incorrect dice numbers have been set"
                                         " for " + char_instance.get_name() +
                                         " the " + self.__class__.__name__ +
                                         ". Please try again")

    def check_type_dice(self, char_instance, dice_type_list):
        """
        :param char_instance: instance od a character
        :param dice_type_list: contains: 1) Edice 2) number of these Edice
        :return: none
        """

        # I'm just getting these values atm without get() methods
        dice_type_1 = char_instance.__class__._dice_type_1
        dice_type_2 = char_instance.__class__._dice_type_2
        # print("dice_type_1[0]: " + str(dice_type_1[0]))
        # if dice_type_2 is not None:
        # print("dice_type_2[0]: " + str(dice_type_2[0]))

        count_1 = 0
        count_2 = 0

        # Check the first set of dice type
        for x in dice_type_list:
            if x == dice_type_1[0].name:
                count_1 += 1
        # print(count_1)
        if count_1 != dice_type_1[1]:
            # raise an exception
            raise CharacterException("Incorrect dice type have been set for" +
                                     char_instance.get_name() + " the " +
                                     self.__class__.__name__ + ". Please try "
                                                               "again")

        # Check the second set of dice type (if applicable)
        if dice_type_2 is not None:
            for x in dice_type_list:
                if x == dice_type_1[0].name:
                    count_2 += 1
            # print(count_1)
            if count_2 != dice_type_1[1]:
                # raise an exception
                raise CharacterException("Incorrect dice type have been set "
                                         "for" + char_instance.get_name() +
                                         " the " + self.__class__.__name__ +
                                         ". Please try again")

    def check_health(self, health, base_health):
        # Check the health type
        if health != base_health:
            # raise an exception
            raise CharacterException("Incorrect health input")
